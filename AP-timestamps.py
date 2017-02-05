#!/bin/python

# A minimalistic example of getting the WLAN acces point timestamp, 
# that often equals the uptime, from sniffed beacon frames.
#
# Channel hopping is not implemented. Either set the channel
# manually or run airmon-ng in parallel.
#
# You need Scapy for this to work!
# See: http://www.secdev.org/projects/scapy/
# Install: "pip install scapy"


# Airmon-ng monitor device.
# Created like: "sudo airmon_ng start wlan0 1"
WLAN_MONITOR_DEVICE = 'mon0'

# Show all sniffed WLAN beacons?
# If set to 'False', only the first received bacon is shown.
SHOW_ALL_BEACONS = False


from datetime import datetime, timedelta
from scapy.all import sniff
from scapy.layers.dot11 import Dot11
from scapy.layers.dot11 import Dot11Beacon

# List of already seen AP SSIDs
knownSsids = []


def snifferCallback(packet):
	'''Callback function for the Scapy packet sniffer'''
	# We are only interested in beacon frames
	if packet.haslayer(Dot11Beacon):

		if SHOW_ALL_BEACONS:
			printThisPacket = True
		else: 
			printThisPacket = False
	
		ssid = packet[Dot11].addr2
		if not ssid in knownSsids:
			knownSsids.append(ssid)
			printThisPacket = True

		if printThisPacket:
			# Filter out funny ESSIDs containing non-printable chars.
			essid = packet[Dot11].info.encode('string-escape')
			# These tend to be long when escaped, so truncate them.
			if len(essid) > 32:
				essid = essid[:28] + '...'

			# Here scapy gives us the wanted timestamp from the beacon frame. Too easy!
			# These are microseconds.
			timestamp = int(packet[Dot11].timestamp)
			
			# Calculate a few things for a nice output and remove the milliseconds
			delta = timedelta(microseconds = timestamp)
			upTime = str(delta).split('.')[0]
			upSince = str(datetime.now() - delta).split('.')[0]

			print '{:20} {:32} {:>16d}us, up since {} ({})'.format(
				ssid, essid, timestamp, upSince, upTime)

	return
	

### MAIN
# Q&D heading
print '{:20} {:30} {:>15}'.format('AP SSID', 'ESSID', 'Timestamp')

# Sniff packets till Ctrl+C ;)
sniff(iface='mon0', store=False, prn=snifferCallback)
