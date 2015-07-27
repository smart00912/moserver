__author__ = 'win7vm'
import psutil
import datetime

'''
disk
'''
print psutil.disk_partitions()
print psutil.disk_usage('c:/')
print psutil.disk_io_counters()
'''
cpu
'''
print psutil.cpu_times(percpu=True)
print psutil.cpu_times().idle
print psutil.cpu_count()
print psutil.cpu_count(logical=False)
'''
memory
'''
print psutil.virtual_memory().used
print psutil.swap_memory()

'''
network
'''
print psutil.net_if_addrs()
print psutil.net_connections()
print psutil.net_io_counters()

'''
user
'''
# list current login user
print psutil.users()
psutil.process_iter()
'''
system
'''
print psutil.boot_time()
print  datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H: %M: %S')

'''
process
'''
print psutil.pids()
print psutil.Process()
print psutil.Process(psutil.pids()[0]).name()
print psutil.Process(psutil.pids()[-1]).exe()
print psutil.Process(psutil.pids()[-9]).cwd()
#print psutil.Process(psutil.pids()[-9]).uids()
#print psutil.Process(psutil.pids()[-9]).gids()
print psutil.Process(psutil.pids()[-9]).cpu_times()
print psutil.Process(psutil.pids()[-9]).memory_info()
print psutil.Process(psutil.pids()[-9]).memory_percent()
print psutil.Process(psutil.pids()[-9]).connections()
print psutil.Process(psutil.pids()[-9]).num_threads()

'''
popen
starting application and get its info
'''
from subprocess import PIPE
p=psutil.Popen(['ping','-t','localhost'],stdout=PIPE)
print p.name()
#print p.username()













