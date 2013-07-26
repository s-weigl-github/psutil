import psutil

__version__ = 'ver. 0.1 - alpha'

print("-- for help type -- info --")
new = input(" what do you wanna know about the system?: ")
#########################################################
## memory ##
memo = psutil.virtual_memory()
swap = psutil.swap_memory()
## systm ##
user = psutil.get_users()
boot = psutil.get_boot_time()
syst = psutil.get_pid_list()
sysl = psutil.get_process_list()
## cpu ##
cpus = psutil.NUM_CPUS
cpuc = psutil.cpu_percent(interval=1, percpu=True)
cpuv = psutil.cpu_times(percpu=True)
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
just by give in mem, system, cpu, disk or network"""

quest = """cpu c - show's cpu load in %,\ncpu s - show's number of cpu's,
cpu v - show's cpu load"""

hint = """mem a - show's memory info,\nmem s - show's swap info"""

print("\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n")

if "cpu" in new:
  if "cpu c" in new:
    print("system run's at",cpuc,"%\n")
  elif "cpu s" in new:
    print("your system has", cpus,"cpu's\n")
  elif "cpu v" in new:
    print(cpuv,"\n")
  else:
    print("cpu has more options, type -- quest --")
#########################    
elif "disk" in new:
  if "disk d" in new:
    print(dskd,"\n")
#########################   
elif "system" in new:
  print(user,"\n")
#########################
elif "mem" in new:
  if "mem a" in new:
    print(memo,"\n")
  elif "mem s" in new:
    print(swap,"\n")
  else:
    print("mem has more options, type -- hint --")
#########################
elif "network" in new:
  print(nets,"\n")
#########################
elif "hint" in new:
  print(hint,"\n")
elif "quest" in new:
  print(quest,"\n")
elif "info" in new:
  print(inf,"\n")
elif "ver" in new:
  print(__version__, "\n")
elif "autor" in new:
  print("idear and codings are from\nSebastian Weigl at 26.July.2013\n")
else:
  print("!!! Fail! value not on list !!!")
  print("  !!! Please change value !!!\n")
