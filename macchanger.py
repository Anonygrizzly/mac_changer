import subprocess
#this was the only change
interface=input("input interface> ")
new_mac = input("enter mac address such as 00:11:22:33:44:55> ")
print("[+] chanding mac address of "+interface+" to "+new_mac+" >")
subprocess.call("ifconfig "+ interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+new_mac+"",shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)
subprocess.call("ifconfig",shell=True)
print("congo your mac address changes > ")
