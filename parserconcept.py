import subprocess
import optparse
import re

def getarguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its man address")
    parser.add_option("-m","--mac",dest="new_mac",help="New man address")
    (options,argumets) = parser.parse_args()
    if not options.interface:
        parser.error("[*] Please enter interface ")
    elif not options.new_mac:
        parser.error("[*] Please enter mac address ")
    else:
        return options


def newmac(interface,new_mac):
    print("[+] changing mac address to "+new_mac)
    subprocess.call("ifconfig "+interface+" down",shell=True)
    subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True )
    subprocess.call("ifconfig "+interface+" up",shell=True)
    ifconfig_result=subprocess.check_output(["ifconfig",interface])
    # print(ifconfig_result)
    new_mac_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    print(new_mac_address.group(0)) #group is used to avoid multiple search items error
    return new_mac



options = getarguments()
mac_address_entered=options.new_mac
newmac_address=newmac(options.interface,options.new_mac)
def mac_address_check():
    if mac_address_entered==newmac_address:
        print("[+] mac address changed successfully")
    else:
        print("mac address didn't changed or you typed some wrong mac address")
mac_address_check()
