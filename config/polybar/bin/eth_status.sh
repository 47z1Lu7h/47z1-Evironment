#!/bin/bash

IFACE=$(/usr/sbin/ifconfig  | grep -Ei "wlan|eth0|ens33|ens36|emp0s3" | awk '{print $1}')
IP=$(/usr/sbin/ifconfig |  grep -Ei "wlan|eth0|ens33|ens36|emp0s3"  | grep "inet 192")

if [ "$IFACE" = "wlan0:" ]; then
	echo "%{T0}%{F#bbe0ff}  %{T3}%{F#888A}  %{T2}%{F#888AAF}$(echo $(/usr/sbin/ifconfig | grep wlan -b1 | grep inet | awk '{print $3}'))"
fi

if [ "$IFACE" = "eth0:" ]; then
        echo "%{T0}%{F#bbe0ff}  %{T4}%{F#888A}    %{T2}%{F#888AAF}$(echo $(/usr/sbin/ifconfig | grep eth0 -b1 | grep inet | awk '{print $3}'))"
fi

if [ "$IFACE" = "ens33:" ]; then
        echo "%{T0}%{F#bbe0ff}  %{T4}%{F#888A}  %{T2}%{F#888AAF}$(echo $(/usr/sbin/ifconfig | grep ens33 -b1 | grep inet | awk '{print $3}'))"
fi

if [ "$IFACE" = "ens36" ]; then
        echo "%{T0}%{F#bbe0ff}  %{T4}%{F#888A}  %{T2}%{F#888AAF}$(echo $(/usr/sbin/ifconfig | grep ens36 -b1 | grep inet | awk '{print $3}'))"
fi

if [ "$IP" = " " ]; then
	echo "%{T0}%{F#bbe0ff} %{T4}%{F#888A}%{T3}%{F#888AAF} Conecting.."
else
        echo "%{T0}%{F#bbe0ff}睊%{u-}%{T2}%{F#888A}  %{F#218889} Disconected!"
fi
