#WLAN AP Uptime/Timestamp Listing
A minimalistic example of getting the WLAN acces point timestamp from sniffed beacon frames. The timestamp is often the uptime of an access point and might be of interest in certain cases.

## Get it running
* You need a WLAN adapter that works with [Aircrack-ng](http://www.aircrack-ng.org/)<br>
  Since we are only interested in beacon frames, most cards should do the job.
* Make sure [Scapy](http://www.secdev.org/projects/scapy/) is installed<br>
  `pip install scapy`
* Start __airmon-ng__<br>
  `sudo airmon-ng start wlanX 1` with wlanX being your WLAN device, "1" the channel<br>
  This should get you a monitor device __mon0__. If it has got a different name, change the line `WLAN_MONITOR_DEVICE = 'mon0'` in the script.
* Optional: Start __airodump-ng__ for channel selection or hopping. Example:<br>
  `sudo airodump-ng mon0`
* Run the script<br>
  ``sudo python AP-timestamps.py``<br>
	Needs to run as su. Is there a better solution?

## Example output
(sensible data has been randomized)
```
AP SSID              ESSID                                Timestamp
a0:4f:d4:xx:xx:xx    A1-z48209                           5814224077191us, up since 2016-11-30 15:28:24 (67 days, 7:03:44)
56:67:11:xx:xx:xx    UPC Wi-Free                         2726965350797us, up since 2017-01-05 09:02:43 (31 days, 13:29:25)
00:25:9c:xx:xx:xx    NeighboursWLAN                      2596208640387us, up since 2017-01-06 21:22:00 (30 days, 1:10:08)
56:67:31:xx:xx:xx    Some strange ESSID                  2726965350872us, up since 2017-01-05 09:02:43 (31 days, 13:29:25)
00:17:9a:xx:xx:xx    HOTSPOT                             7791921049987us, up since 2016-11-07 18:06:47 (90 days, 4:25:21)
aa:bb:cc:xx:xx:xx    tomelec.net                           27503821122us, up since 2017-02-05 14:53:45 (7:38:23)
06:7c:34:xx:xx:xx    UPC Wi-Free                         7151004877183us, up since 2016-11-15 04:08:44 (82 days, 18:23:24)
54:67:51:xx:xx:xx    Even stranger ESSID                 2726966067614us, up since 2017-01-05 09:02:43 (31 days, 13:29:26)
58:6d:8f:xx:xx:xx    Cisco39187                         10067567923587us, up since 2016-10-12 09:59:22 (116 days, 12:32:47)
00:1a:8c:xx:xx:xx    Company-Internal                   11074460467545us, up since 2016-09-30 18:17:49 (128 days, 4:14:20)
00:1a:8c:xx:xx:xx    Company-Guest                      11074460469531us, up since 2016-09-30 18:17:49 (128 days, 4:14:20)
00:26:f2:xx:xx:xx    NETGEAR                            22398269419905us, up since 2016-05-22 16:47:54 (259 days, 5:44:29)
```
* There are three APs with an uptime of 31 days, 13:29, probably running on the same hardware but with differeing vendor IDs. Same thing with the two _Company-*_ ones.
* The _NETGEAR_ one has not seen a power outage for some time.
* _tomelec.net_ spent the day messing around with his AP but got it running again about 7 hours ago ;)

