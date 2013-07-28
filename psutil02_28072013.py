##########################################################
## this programm reads and prints system varibles using ##
##      -- psutil from Giampaolo Rodola' --             ##
##########################################################
import psutil

__version__ = 'ver. 1.0 - beta'
__date__ = 2013, 7, 28

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
sol = """system u - show user info,\nsystem b - show boot time
system d - list pid,\nsystem p - list process"""
print("\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n")
def Processor(self):
  if "cpu" in new:
    if "cpu c" in new:
      print("system run's at", cpuc, "%\n")
    elif "cpu s" in new:
      print("your system has", cpus, "cpu's\n")
    else:
      print("noch leer")
      
      
