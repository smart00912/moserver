from django.shortcuts import render,render_to_response
from moadmin.models import *
from django.http import HttpResponse
import logger
from public.encry import tencode,tdecode
from django.conf import settings

# Create your views here.

'''
main page
'''
def index(req):
	res_template_dist={'system_name':settings.SYSTEM_NAME}
	return render_to_response('moadmin/main.html',res_template_dist)

def module_add(req):
	res_template_dist={'system_name':settings.SYSTEM_NAME}
	return render_to_response('moadmin/module_add.html')

'''
return function list
'''
def server_fun_categ(req):
	categ_id='-1'
	categ_name=u'<select function>'
	ServerFunObj=ServerFunCateg.objects.order_by('id')
	for k in ServerFunObj:
		categ_id+=','+str(k.id)
		categ_name+=',' +k.server_categ_name
	server_categ_string=categ_name+'|'+categ_id
	return HttpResponse(server_categ_string)

'''
return server app categ
'''
def server_app_categ(req):
	categ_id='-1'
	categ_name=u'<select APP>'
	
	if not 'fun_categId' in req.GET.get():
		fun_categId=''
	else:
		fun_categId=req.GET['fun_categId']
	
	ServerAppObj =ServerAppCateg.objects.filter(server_categ_id=fun_categId)
	for k in ServerAppObj:
		categ_id+=','+str(k.id)
		categ_name+=','+k.app_categ_name
	app_categ_string=categ_name+'|'+categ_id
	return HttpResponse(app_categ_string)


		
	

'''
server ip list
'''
def server_list(req):
	ip =''
	ip_hostname=''
	if not 'app_categId' in req.GET.get():
		app_categId = ''
	else:
		app_categId = req.GET.get('app_categId')
		serverListObj = ServerList.objects.filter(server_app_id=app_categId)
		for str in serverListObj:
			ip+=','+str.server_intip
			ip_hostname+=','+str.server_intip+'*'+str.server_name
		server_list_str=ip[1:]+'|'+ip_hostname[1:]
		return HttpResponse(server_list_str)
	

'''
return modules list
'''
def module_list(req):
	module_id='-1'
	module_name=u'Select module...'
	ModuleOjb = ModuleList.objects.order_by('id')
	for mo in ModuleOjb:
		module_id+=','+str(mo.id)
		module_name=','+mo.module_name
	module_list_str = module_name+'|'+module_id
	return HttpResponse(module_list_str)

'''
return module info
'''
def module_info(req):
	if not 'ModuleId' in req.GET.get():
		Module_Id=''
	else:
		Module_Id=req.GET.get('Module_Id')
	ModuleObj = ModuleList.objects.get(id=Module_Id)
	module_info_string=str(Module_Id)+'@@'+ModuleObj.module_name+'@@'+ModuleObj.module_fun_desc+'@@'+ModuleObj.module_fun_ext
	return HttpResponse(module_info_string)


def module_run(req):
	import rpyc
	put_string=''
	if not 'ModuleID' in req.GET.get():
		Module_Id=''
	else:
		Module_Id = req.GET.get('ModuleID')
		put_string +=Module_Id+"@@"
	if not 'hosts' in req.GET.get():
		Hosts=''
	else:
		Hosts=req.GET.get('hosts')
		put_string=Hosts+'@@'
	'''
	module extend params recive
	'''
	if not 'sys_param_1' in req.GET.get():
		Sys_param_1=''
	else:
		Sys_param_1=req.GET.get('sys_param_1')
		put_string=Sys_param_1+'@@'
	if not 'sys_param_2' in req.GET.get():
		Sys_param_2=''
	else:
		Sys_param_2=req.GET.get('sys_param_1')
		put_string=Sys_param_2+'@@'
	try:
		conn = rpyc.connect('127.0.0.1',11511)
		conn.root.login('sean','htbenet100')
	except Exception,e:
		logger.error('connect to rpyc server failed'+str(e))
		return HttpResponse('connect to rpyc server failed'+str(e))
	put_string=tencode(put_string,settings.SECRET_KEY)
	OPresult=tdecode(conn.root.Runcommands(put_string),settings.SECRET_KE)
	return HttpResponse(OPresult)

'''
Add module
'''
def module_add_post(req):
	if req.method=='GET':
		
		if not req.GET.get('module_name',''):
			return HttpResponse('App name can not be null')
		
		if not req.GET.get('module_fun_desc',''):
			return HttpResponse('Fun name can not ne null')
		
		module_name=req.GET.get('module_name')
		module_fun_desc=req.GET.get('module_fun_desc')
		module_extend=req.GET.get('module_extend')
		
		moduleobj = ModuleList(module_name=module_name,module_fun_desc=module_fun_desc,module_extend=module_extend)
		try:
			moduleobj.save()
			lastId=ModuleList.objects.latest('id')
		except Exception,e:
			return HttpResponse('adding module failed!'+str(e))
		InfoList='Adding module successed,moudle ID: '+str(lastId.pk)
		return HttpResponse(InfoList)
	else:
		return HttpResponse('Invalid post')
	
			

		
	