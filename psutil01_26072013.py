##########################################################
## this programm reads and prints system varibles using ##
##      -- psutil from Giampaolo Rodola' --             ##
##########################################################
import psutil

__version__ = 'ver. 0.7 - beta'

print("-- for help type -- info --")
new = input(" what do you wanna know about the system?: ")
##############################################################################
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
dskm = psutil.disk_io_counters(perdisk=True)
dskc = psutil.disk_usage("C:")
dskd = psutil.disk_usage("D:")
dske = psutil.disk_usage("E:")
dskg = psutil.disk_usage("G:")
dskk = psutil.disk_usage("K:")
##############################################################################
inf = """you can get infos about your system,
just by give in mem, system, cpu, disk or network"""
quest = """cpu c - show's cpu load in %,\ncpu s - show's number of cpu's,
cpu v - show's cpu load"""
hint = """mem a - show's memory info,\nmem s - show's swap info"""
faq = """disk c - show's C: info,\ndisk d - show's D: info,
disk e - show's E: info,\ndisk g - show's G: info,
disk k - show's K: info"""
helf = """network s - show some stats,\nnetwork w - show some stats"""
sol = """system u - show user info,\nsystem b - show boot time"""
print("\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n")
if "cpu" in new:
  if "cpu c" in new:
    print("system run's at",cpuc,"%\n")
  elif "cpu s" in new:
    print("your system has", cpus,"cpu's\n")
  elif "cpu v" in new:
    print(cpuv,"\n")
  else:
    print("cpu has more options, type -- help processor --")
elif "disk" in new:
  if "disk c" in new:
    print(dskc,"\n")
  elif "disk d" in new:
    print(dskd,"\n")
  elif "disk e" in new:
    print(dske,"\n")
  elif "disk g" in new:
    print(dskg,"\n")
  elif "disk k" in new:
    print(dskk,"\n")
  else:
    print("disk has more options, type -- help hdd --")
elif "system" in new:
  if "system u" in new:
    print(user,"\n")
  elif "system b" in new:
    print(boot,"\n")
  else:
    print("system has more options, type -- help sys --")
elif "memory" in new:
  if "memory a" in new:
    print(memo,"\n")
  elif "memory s" in new:
    print(swap,"\n")
  else:
    print("memory has more options, type -- help mem --")
elif "network" in new:
  if "network s" in new:
    print(nets,"\n")
  elif "network w" in new:
    print(netw,"\n")
  else:
    print("network has more options, type -- help net --")
elif "help sys" in new:
  print(sol,"\n")
elif "help net" in new:
  print(helf,"\n")
elif "help hdd" in new:
  print(faq,"\n")
elif "help mem" in new:
  print(hint,"\n")
elif "help processor" in new:
  print(quest,"\n")
elif "info" in new:
  print(inf,"\n")
elif "version" in new:
  print(__version__, "\n")
elif "autor" in new:
  print("idear and codings are from\nSebastian Weigl at 26.July.2013\n")
else:
  print("!!! Fail! value not on list !!!")
  print("  !!! Please change value !!!\n")
