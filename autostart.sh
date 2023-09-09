#!/bin/sh
nitrogen --restore &
picom &
xinput set-prop "ELAN1205:00 04F3:30E9 Touchpad" "libinput Natural Scrolling Enabled" 1
xinput set-prop "ELAN1205:00 04F3:30E9 Touchpad" "libinput Tapping Enabled" 1

