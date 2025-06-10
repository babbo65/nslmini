#!/bin/bash
ip=$(ip -o -f inet addr show | awk '$2 != "lo" {print $4; exit}')
#sudo nmap -sn -PR $ip -oX out.xml
nmap -sn -PR $ip -oG - | awk '/Up$/{print $2, $3}'
