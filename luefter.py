#!/usr/bin/python3
from os import remove
from subprocess import check_output, run

run(["sudo", "/usr/bin/jetson_clocks"])

temperatur = check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"])
temperatur = "{:.2f}".format(float(temperatur.decode("utf-8")) / 1000)
pwm = check_output(["cat", "/sys/devices/pwm-fan/target_pwm"])
pwm = pwm.rstrip()

temperatur_float = float(temperatur)

if temperatur_float < 35.0:
    run(["sudo", "sh", "-c", "echo 0 > /sys/devices/pwm-fan/target_pwm"])
if temperatur_float > 35.0 and temperatur_float < 36.0:
    run(["sudo", "sh", "-c", "echo 150 > /sys/devices/pwm-fan/target_pwm"])
if temperatur_float > 36.0 and temperatur_float < 37.0:
    run(["sudo", "sh",  "-c", "echo 170 > /sys/devices/pwm-fan/target_pwm"])
if temperatur_float > 37.0 and temperatur_float < 38.0:
    run(["sudo", "sh",  "-c", "echo 190 > /sys/devices/pwm-fan/target_pwm"])
if temperatur_float > 38.0 and temperatur_float < 39.0:
    run(["sudo", "sh",  "-c", "echo 210 > /sys/devices/pwm-fan/target_pwm"])
if temperatur_float > 39.0 and temperatur_float < 40.0:
    run(["sudo", "sh",  "-c", "echo 230 > /sys/devices/pwm-fan/target_pwm"])
if temperatur_float > 40.0:
    run(["sudo", "sh",  "-c", "echo 255 > /sys/devices/pwm-fan/target_pwm"])
