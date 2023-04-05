#!/bin/sh

VPN=$(/usr/sbin/ifconfig | grep -iE "tun0|tun1|tun2|tun3" | awk '{print $1}' | tr -d ':')

if [ "$VPN" = "tun0" ]; then
	echo "%{T2}%{F#13FF00}  %{F#888A}%{T5}%{T4}%{F#13FF00}$(/usr/sbin/ifconfig tun0 | grep "inet" | awk '{print $2}')"o

else
	echo "%{T0}%{F#00A409} %{u-}%{T5}%{F#888A} %{T2}%{F#00A409} Disconected"
fi

