from django.db import models

# Create your models here.
class ServerFunCateg(models.Model):
	id = models.IntegerField(primary_key=True,db_column='ID')
	server_categ_name = models.CharField(max_length=100)
	class Meta:
		db_table = u'server_fun_categ'

class ServerAppCateg(models.Model):
	id = models.IntegerField(primary_key=True,db_column='ID')
	server_categ_id = models.ForeignKey(ServerFunCateg)
	app_categ_name = models.CharField(max_length=100)
	class Meta:
		db_table = u'server_app_categ'
		
class ServerList(models.Model):
	server_name = models.CharField(primary_key=True,max_length=50)
	server_extip = models.CharField(max_length=45)
	server_intip = models.CharField(max_length=45)
	server_os = models.CharField(max_length=50)
	server_app_id = models.ForeignKey(ServerAppCateg)
	class Meta:
		db_table = u'server_list'
		
class ModuleList(models.Model):
	id = models.IntegerField(primary_key=True,db_column='ID')
	module_name = models.CharField(max_length=100)
	module_fun_desc = models.CharField(max_length=500)
	module_fun_ext = models.CharField(max_length=5000)
	class Meta:
		db_table = u'module_list'

