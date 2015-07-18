from django.shortcuts import render,render_to_response
from moadmin.models import *
from django.http import HttpResponse
import logger
from public.encry import tencode,tdecode
from django.conf import settings

# Create your views here.

'''
server list
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



		
	