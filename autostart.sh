#!/bin/sh
nitrogen --restore &
picom &
light-locker --lock-after-screensaver=0 &
xinput set-prop "ELAN1205:00 04F3:30E9 Touchpad" "libinput Natural Scrolling Enabled" 1
xinput set-prop "ELAN1205:00 04F3:30E9 Touchpad" "libinput Tapping Enabled" 1
xinput set-prop "ELAN1205:00 04F3:30E9 Touchpad" "libinput Scrolling Pixel Distance" 40
xinput set-prop "ELAN1205:00 04F3:30E9 Mouse" "libinput Natural Scrolling Enabled" 1
xinput set-prop "ELAN1205:00 04F3:30E9 Mouse" "libinput Scrolling Pixel Distance" 40
xinput set-prop "ELAN1205:00 04F3:30E9 Touchpad" "libinput Accel Speed" -0.018
xinput set-prop "ELAN1205:00 04F3:30E9 Mouse" "libinput Accel Speed" -1
udisksctl mount -b /dev/nvme0n1p6
