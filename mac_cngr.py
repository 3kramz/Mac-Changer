import subprocess
import optparse


def user_opt():
    obj = optparse.OptionParser()
    obj.add_option("-i", "--interface", dest="iface", help="Interface new")
    obj.add_option("-m", "--mac", dest="mac", help="Add new mac adrs")
    (user_input, arg) = obj.parse_args()
    return user_input


def mac_changer(interface, new_mac):
    ifconfig = "ifconfig"
    subprocess.call([ ifconfig, interface, "down"])
    subprocess.call([ifconfig, interface, "hw", "ether", new_mac])
    subprocess.call([ifconfig, interface, "up"])
    subprocess.check_call(["ifconfig", interface])


input = user_opt()
iface = input.iface
mac = input.mac
mac_changer(iface, mac)




