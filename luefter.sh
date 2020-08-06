#!/bin/bash
sleep 10
sudo /usr/bin/jetson_clocks
echo 0 > /sys/devices/pwm-fan/target_pwm

exit 0
