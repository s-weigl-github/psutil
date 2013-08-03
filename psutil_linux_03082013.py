import psutil

__version__ = 'ver. 2 - linux'
__date__ = 2013, 8, 3

#####################################################
## cpu ##
cpus = psutil.NUM_CPUS
cpul = psutil.cpu_percent(interval=1, percpu=True)
cpuv = psutil.cpu_times(percpu=True)
## memory ##
mema = psutil.virtual_memory()
memw = psutil.swap_memory()
## disk ##
dskc = psutil.disk_usage("/root/")
dskd = psutil.disk_usage("/")
## systm ##
sysz = psutil.get_users()
sysy = psutil.get_boot_time()
sysr = psutil.get_pid_list()
sysh = psutil.get_process_list()
## network ##
netn = psutil.network_io_counters()
netm = psutil.network_io_counters(pernic=True)
#####################################################
def print_options():
  print("Options:")
  print("  CPU info's")
  print("    'l' cpu load in %")
  print("    's' cpu's in systm")
  print("    'v' cpu load")
  print("  RAM info's")
  print("    'a' ram info")
  print("    'w' swap info")
  print("  HDD info's")
  print("    'c' info /root/ drive")
  print("    'd' info / drive")
  print("  SYS info's")
  print("    'z' get user info")
  print("    'y' boot time info")
  print("    'r' PID list info")
  print("    'h' Process list")
  print("  NET info's")
  print("    'n' network io info")
  print("    'm' network io info")
  print(" other info's")
  print("   'ver' version")
  print("   'aut' autor")
  print("  'q' quit")
#####################################################
def output_processor_s(cpus):
  return psutil.NUM_CPUS
def output_processor_l(cpul):
  return psutil.cpu_percent(interval=1, percpu=True)
def output_processor_v(cpuv):
  return psutil.cpu_times(percpu=True)
def output_mem_a(mema):
  return psutil.virtual_memory()
def output_mem_w(memw):
  return psutil.swap_memory()
def output_hdd_c(dskc):
  return psutil.disk_usage("/root/")
def output_hdd_d(dskd):
  return psutil.disk_usage("/")
def output_sys_z(sysz):
  return psutil.get_users()
def output_sys_y(sysy):
  return psutil.get_boot_time()
def output_sys_r(sysr):
  return psutil.get_pid_list()
def output_sys_h(sysh):
  return psutil.get_process_list()
def output_net_n(netn):
  return psutil.network_io_counters()
def output_net_m(netm):
  return psutil.network_io_counters(pernic=True)
#####################################################
choice = "x"
while choice != "q":
  if choice == "s":
    print(output_processor_s(cpus))
    choice = input("option: ")
  elif choice == "l":
    print(output_processor_l(cpul))
    choice = input("option: ")
  elif choice == "v":
    print(output_processor_v(cpuv))
    choice = input("option: ")
  elif choice == "a":
    print(output_mem_a(mema))
    choice = input("option: ")
  elif choice == "w":
    print(output_mem_w(memw))
    choice = input("option: ")
  elif choice == "c":
    print(output_hdd_c(dskc))
    choice = input("option: ")
  elif choice == "d":
    print(output_hdd_d(dskd))
    choice = input("option: ")
  elif choice == "z":
    print(output_sys_z(sysz))
    choice = input("option: ")
  elif choice == "y":
    print(output_sys_y(sysy))
    choice = input("option: ")
  elif choice == "r":
    print(output_sys_r(sysr))
    choice = input("option: ")
  elif choice == "h":
    print(output_sys_h(sysh))
    choice = input("option: ")
  elif choice == "n":
    print(output_net_n(netn))
    choice = input("option: ")
  elif choice == "m":
    print(output_net_m(netm))
    choice = input("option: ")
  elif choice == "x":
    print_options()
    choice = input("option: ")
##-EOF-##
