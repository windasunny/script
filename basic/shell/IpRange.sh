#!/bin/bash

for x in $(seq 13 16);
do
	for y in $(seq 255):
	do
		for z in $(seq 255):
		do
			ping -w 1 "172.$x.$y.$z" | grep "64 bytes from" > /home/sunny_tsai/IpRange.txt
		done
	done
done
