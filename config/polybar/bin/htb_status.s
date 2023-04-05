#!/bin/sh

VPN=$(/usr/sbin/ifconfig | grep -iE "tun0|tun1" | awk '{print $1}' | tr -d ':')

if [ "$VPN" = "tun0" ]; then
	echo "%{T0}%{F#13FF00} %{F#888A}%{T2} %{T4}%{F#13FF00} $(/usr/sbin/ifconfig tun0 | grep "inet " | awk '{print $2}')%{u-}%{F#888A}%{T4}  ~"
fi

if [ "$VPN" = "tun1" ]; then
        echo "%{T0}%{F#13FF00}  %{F#888A}%{T2} %{T3}%{F#13FF00} $(/usr/sbin/ifconfig tun1 | grep "inet " | awk '{print $2}')%{u-}  "

else
	echo "%{T0}%{F#00A409}  %{u-}%{T2}%{F#888A} %{T2}%{F#00A409} Disconected  "
fi

