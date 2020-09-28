import subprocess
import optparse
import re
def arguments():
    parse =optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="choose an interface shown by ifconfig")
    parse.add_option("-m","--mac",dest="new_mac",help="new mac address")
    (options,arguments) = parse.parse_args()
    if not options.interface:
        parse.error("!!! enter interface -i or --interface")
    elif not options.new_mac:
        parse.error("!!! enter mac adress -m or --mac xx:xx:xx:xx:xx:xx ")
    else:
        return options
def changing_mac_address(interface,new_mac):
    print("[+] changing mac address to" + new_mac)
    subprocess.call("ifconfig " + interface + " down",shell=True)
    subprocess.call("ifconfig " + interface +" hw ether "+new_mac,shell=True)
    subprocess.call("ifconfig "+interface+" up",shell=True)
    ifconfig_results = subprocess.check_output("ifconfig "+interface ,shell=True)
    new_mac_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_results))
    return new_mac_address.group(0)
def main():
    options=arguments()
    new_mac_address = changing_mac_address(options.interface,options.new_mac)
    if options.new_mac == new_mac_address:
        print("[+]   mac address changes succesfuly")
        print("New mac address = " + new_mac_address)
    else:
        print("mac address didnt change successfully")

main()