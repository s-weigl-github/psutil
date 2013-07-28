import psutil

__version__ = 'ver. 1.1 - beta'
__date__ = 2013, 7, 28

#####################################################
## cpu ##
cpus = psutil.NUM_CPUS
cpuc = psutil.cpu_percent(interval=1, percpu=True)
cpuv = psutil.cpu_times(percpu=True)
## memory ##
memo = psutil.virtual_memory()
swap = psutil.swap_memory()
#####################################################
def print_options():
  print("Options:")
  print("  CPU info's")
  print("    'c' cpu load in %")
  print("    's' cpu's in systm")
  print("    'v' cpu load")
  print("  RAM info's")
  print("    'a' ram info")
  print("    'w' swap info")
  print("  HDD info's:")
  print("    'c' cpu load in %")
  print("    's' cpu's in systm")
  print("  SYS info's:")
  print("    'c' cpu load in %")
  print("    's' cpu's in systm")
  print("  NET info's:")
  print("    'c' cpu load in %")
  print("    's' cpu's in systm")
  print("  'q' quit")

def output_processor_s(cpus):
  return psutil.NUM_CPUS
def output_processor_c(cpuc):
  return psutil.cpu_percent(interval=1, percpu=True)

choice = "x"
while choice != "q":
  if choice == "s":
    print(output_processor_s(cpus))
    choice = input("option: ")
  elif choice == "c":
    print(output_processor_c(cpuc))
    choice = input("option: ")
  elif choice == "x":
    print_options()
    choice = input("option: ")



