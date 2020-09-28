import subprocess
import re
import optparse

def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest = "interface",help = "interface whose mac is to be changesd such as eth0 and wlan0")
    parser.add_option("-m","--mac",dest = "new_mac",help = "mac address to be changed")
    options,arguments = parser.parse_args()
    return options

def changing_mac(interface , new_mac):
    print("[+] changing to mac address :" + new_mac)
    subprocess.call("ifconfig " + interface +" down",shell = True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig "+ interface + " up ",shell = True)
    print(" mac address changed to mac : "+ new_mac)
    ifconfig_results = subprocess.check_output("ifconfig "+ interface,shell=True)
    new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" ,str(ifconfig_results))
    print("\n\n" + new_mac_address.group(0))

options = arguments()
changing_mac(options.interface,options.new_mac)

