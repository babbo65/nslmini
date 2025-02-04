#!/bin/bash
ip=$(ip -o -f inet addr show | awk '$2 != "lo" {print $4; exit}')
nmap -sn $ip -oX out.xml
