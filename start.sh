#!/bin/bash
# Block ip from blackip.txt

BLACKIP = "blackip.txt"
IPTABLES = /sbin/iptables
EGREP = /bin/egrep

if [ "$(id -u)" != "0" ]; then
	echo "[-] you must be root." 1>&2
	exit 1
fi

# clean iptables rules
resetrules() {
	$IPTABLES -F
	$IPTABLES -t nat -F
	$IPTABLES -t mangle -F
	$IPTABLES -X
}
resetrules

# 
IPS = $($EGREP -v "^#|^$" $BLACKIP)
for ip in $IPS
do
	echo "[+] blocking $ip"
	$IPTABLES -A INPUT -s $ip -j DROP
done
exit 0
