"""
__author__ : sranjanr
__description__ : This creates the batches for the command_list which has to be processed.

"""
from itertools import islice, chain
from collections import OrderedDict

def batch(iterable, size):
    sourceiter = iter(iterable)
    while True:
        batchiter = islice(sourceiter, size)
        yield chain([batchiter.next()], batchiter)

commands_list = [
		"show controllers Gi0/0/0/1 phy | b Alarm High",
		"show ip route isis",
		"show controllers Hu0/18/0/4 phy | b Alarm High",
		"show isis topology",
		"show interface brief",
		"show interfaces Gi0/0/0/1 | i rate",
		"show mpls ldp neighbor detail",
		"show fabric er",
		"show controllers Gi0/0/0/0.1 phy | b Alarm High",
		"show bgp ipv6 unicast summary",
		"show controllers Gi0/0/0/1 internal | i Defects",
		"show aps group 1",
		"show run | in ^ aps group",
		"show fabric status",
		"show ip bgp ipv4 multicast summary",
		"show fabric errors",
		"show interfaces gi5/3 | i rate",
		"show aps group 2",
		"show crypto key mypubkey dsa",
		"show ip bgp ipv4 tunnel summary",
		"show environment alarm",
		"show pfm location all",
		"show run",
		"show interfaces brief",
		"show controllers fabric plane all",
		"show file systems",
		"show environment | section power-supply",
		"show module",
		"show ip bgp ipv4 mdt all summary",
		"show interfaces  description",
		"show mpls ldp neighbor graceful-restart",
		"show redundancy",
		"show hw-module all fpd",
		"show interfaces GigabitEthernet2/0/0 | i rate",
		"show controllers  GigabitEthernet2/0/0 phy | b Alarm High",
		"show interfaces description",
		"show cdp neighbor",
		"show crypto key mypubkey rss",
		"show nv satellite status",
		"sh int te3/4 transceiver detail"
	]

def remove_duplicates(command_list):
    command_list = list(OrderedDict.fromkeys(command_list))
    return command_list

for batchiter in batch(remove_duplicates(commands_list), 5):
    print "Batch: "
    for item in batchiter:
        print item
