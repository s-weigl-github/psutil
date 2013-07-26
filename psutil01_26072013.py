import psutil

__version__ = 'ver. 0.1 - alpha'

print("-- for help type -- info --")
new = input(" what do you wanna know about the system?: ")
#########################################################
## memory ##
memo = psutil.virtual_memory()
pyme = psutil.phymem_usage()
tome = psutil.TOTAL_PHYMEM
swap = psutil.swap_memory()
## systm ##
user = psutil.get_users()
boot = psutil.get_boot_time()
syst = psutil.get_pid_list()
sysl = psutil.get_process_list()
## cpu ##
cpus = psutil.NUM_CPUS
cpuf = psutil.cpu_percent()
cpuc = psutil.cpu_percent(interval=1, percpu=True)
cpuv = psutil.cpu_times(percpu=False)
cpul = psutil.cpu_times_percent(interval=1, percpu=False)
## network ##
netw = psutil.network_io_counters()
nets = psutil.network_io_counters(pernic=True)
## disk ##
dska = psutil.disk_partitions(all=False)
dskb = psutil.disk_io_counters(perdisk=False)
dskc = psutil.disk_io_counters(perdisk=True)
dskd = psutil.disk_usage('/')
#########################################################

inf = """you can get infos about your system,
just by give in memory, system, cpu, disk or network"""

print("\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n")

if "cpu" in new:
  if "cpu c" in new:
    print(cpuc,"\n")
  elif "cpu s" in new:
    print(cpus,"\n")
#########################    
elif "disk" in new:
  if "disk d" in new:
    print(dskd,"\n")
#########################   
elif "system" in new:
  print(user,"\n")
#########################
elif "memory" in new:
  print(tome,"\n")
#########################
elif "network" in new:
  print(nets,"\n")
#########################  
elif "info" in new:
  print(inf,"\n")
elif "ver" in new:
  print(__version__, "\n")
elif "autor" in new:
  print("idear and codings are from\nSebastian Weigl at 26.July.2013\n")
else:
  print("!!! Fail! value not on list !!!")
  print("  !!! Please change value !!!\n")
