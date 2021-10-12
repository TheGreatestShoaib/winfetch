from winfetch.sysmfy import *
import winfetch.ascii_logos as logo
import emojis

#from winfetch.icons.chinese import *
from winfetch.icons.chinese import *

msg_type = "chinese"
#msg_type="chinese"

#banner_name = logo.arch
banner_name = logo.manjaro 

# Normal Icon
# uptime_text = emojis.encode(":clock130: Uptime")
# os_text = emojis.encode(":computer: OS")
# resolution_text = emojis.encode(":mag: Resolution")
# memory_text = emojis.encode(":cd: memory")
# cpu_text = emojis.encode(":paperclip: CPU")
# gpu_text = emojis.encode(":computer: OS")

#Japanese Characters
# resolution_text = f"{chr(36950)} Resolution"
# uptime_text = f"{chr(36786)} uptime"
# memory_text = f"{chr(36013)} memory"
# os_text = f"{chr(36783)} OS"
# cpu_text = f"{chr(36944)} CPU"
# gpu_text = f"{chr(36013)} GPU"



sysfo = {}


#sysfo["Platform"] = platform_name()
#sysfo["Host_name"] = host_name().node
sysfo[os_text] = os_version()
#sysfo["Host_name"] = host_name().node
#sysfo["Kernel"] = kernel()
sysfo[uptime_text] = uptime()
sysfo[resolution_text] = screensize()
#sysfo["Architecure"] = processor_architecture()
#sysfo["Cpus-Freq "] = f"{cpu_frequency()[2]/1000} gHZ"
#sysfo["Cpu_model "] = cpu_name()
sysfo[cpu_text] = f"{cpu_name()} @ {cpu_frequency()[2]/1000} GHz"
#sysfo[gpu_text] = gpu_name()

sysfo[memory_text] = f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"



#cpu threads
#battery
#data and time
#localip / public ip
#harddisk information
#shell name
