#!/bin/bash
# Example Bar Action Script for Linux.
# Requires: acpi, iostat, lm-sensors, aptitude.
# Tested on: Debian Testing
# This config can be found on github.com/linuxdabbler

############################## 
#	    DATE
##############################

date() {
	  date="$(date +"%r")"
	    echo -e " $dte "
    }

############################## 
#	    DISK
##############################

hdd() {
	  hdd="$(df -h /home | grep /dev | awk '{print $3 " / " $5}')"
	    echo -e " $hdd "
    }
##############################
#	    RAM
##############################

mem() {
	mem="$(free -h | awk '/Mem:/ {printf $3 "/" $2}')"
	echo -e " $mem "
}
##############################	
#	    CPU
##############################

cpu() {
	  read cpu a b c previdle rest < /proc/stat
	    prevtotal=$((a+b+c+previdle))
	      sleep 0.5
	        read cpu a b c idle rest < /proc/stat
		  total=$((a+b+c+idle))
		    cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
		      echo -e " $cpu% "
	      }
##############################
#	    VOLUME
##############################

vol() {
	vol="$(amixer -D pulse get Master | awk -F'[][]' 'END{ print $4":"$2 }')"
	echo -e " $vol "
}
##############################
#	    VPN
##############################

vpn() {
	vpn="$(ip a | grep tun0 | grep inet | wc -l)"
	echo -e " $vpn "
}
## TEMP
temp() {
	tmp="$(grep temp_F ~/.config/weather.txt | awk '{print $2}' | sed 's/"//g' | sed 's/,/ F/g')"
	echo " $tmp"
}


      SLEEP_SEC=1
      #loops forever outputting a line every SLEEP_SEC secs
      while :; do     
	      echo "+@fg=3;+@fn=1; +@fn=0;$(cpu)| +@fg=5;+@fn=1; +@fn=0;$(mem)| +@fg=4;+@fn=1;+@fn=0;$(hdd)|+@fg=2; VPN +@fn=1;+@fn=0;$(vpn)| +@fg=6;+@fn=1;+@fn=0;$(vol)|"
   sleep $SLEEP_SEC
		done
