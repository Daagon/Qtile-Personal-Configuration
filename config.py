# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook

mod = "mod4"
terminal = guess_terminal()
fileManager = "thunar"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn search application cmd"),
    Key([mod], "b", lazy.spawn("rofi -show"), desc="Find open app"),
    Key([mod], "e", lazy.spawn(fileManager), desc="Launch file manager"),
    Key([mod], "s", lazy.spawn("scrot /home/dagon/Imagenes/screenshots/.png --format png"), desc="Full Screenshot"),
    Key([mod, "shift"], "s", lazy.spawn("scrot /home/dagon/Imagenes/screenshots/.png -f -s --format png"), desc="Area Screenshot diff"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen window"),

    #SYSTEM ACTIONS
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),

    #QTILE ACTIONS
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    #SWITCH FOCUS TO SPECIFIC MONITOR (OUT OF THREE)
    Key([mod], "i", lazy.to_screen(0)),
    Key([mod], "o", lazy.to_screen(1)),

    #SWITCH FOCUS OF MONITORS
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    #HARDWARE CONFIGS
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]


#groups = [Group(i) for i in ["", "", "󰈮", "", "󰈬", "󱎓", "", "", ""]]
groups = [
    Group(""),
    Group("", matches=[Match(wm_class=["firefox"])]),
    Group("󰈮", matches=[Match(wm_class=["VSCodium", "geany","Godot_Engine"])]),
    Group("", matches=[Match(wm_class=["Thunar"])]),
    Group("󰈬", matches=[Match(wm_class=["libreoffice-calc", "libreoffice", "LibreOffice Calc", "LibreOffice-Calc", "libreoffice-startcenter", "libreoffice calc", "LibreOffice calc", "LibreOffice-calc"])]),
    Group("", matches=[Match(wm_class=["krita", "Gcolor3", "obs"])]),
    Group(""),
    Group("", matches=[Match(wm_class=["timeshift-gtk", "Nitrogen", "Lxappearance", "nvidia-settings", "pavucontrol"])]),
    Group("", matches=[Match(wm_class=["btop"])]), #ANTES ESTABA "vmplayer"
]


for index, i in enumerate(groups):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],str(index+1),lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name)),
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],str(index+1),lazy.window.togroup(i.name, switch_group=True),desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod], "Tab", lazy.screen.next_group(), desc="Move to next group"),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Move to previous group")
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

#SCRATCHPAD CONFIGURATION
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "alacritty --class=scratch", width=0.6, height=0.6, x=0.2, y=0.2, opacity=1),
    DropDown("term2", "alacritty --class=scratch", width=0.6, height=0.6, x=0.2, y=0.2, opacity=1),
    DropDown("ranger", "alacritty --class=ranger -e ranger", width=0.6, height=0.6, x=0.2, y=0.2, opacity=1),
    DropDown("spotify-tui", "alacritty --class=spt -e spt", width=0.6, height=0.6, x=0.2, y=0.2, opacity=1),

    DropDown("notas", "alacritty --class=notas", width=0.3, height=0.4, opacity=1),
    DropDown("reloj", "alacritty --class=reloj", width=0.3, height=0.2, x=0.6, y=0.75, opacity=1),
]))

#SCRATCHPAD KEYBINDINGS
keys.extend((
  # toggle visibiliy of above defined DropDown named "term"
  Key([mod], 'F1', lazy.group['scratchpad'].dropdown_toggle('term')),
  Key([mod], 'F2', lazy.group['scratchpad'].dropdown_toggle('term2')),
  Key([mod], 'F3', lazy.group['scratchpad'].dropdown_toggle('ranger')),
  Key([mod], 'F4', lazy.group['scratchpad'].dropdown_toggle('spotify-tui')),
  Key([mod], 'F11', lazy.group['scratchpad'].dropdown_toggle('notas')),
  Key([mod], 'F12', lazy.group['scratchpad'].dropdown_toggle('reloj')),
))

layout_theme = {
        "border_width":2,
        "margin":15,
        "border_focus":"FFFFFF",
        "ratio": 0.5415
        #"border_normal":"CCCCCC"
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=8),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
      layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#mymy = [
#    "sans"
#]

myFonts = [
    "sans",
    "3270 Nerd Font",
    "Agave Nerd Font",
    "Arimo Nerd Font",
    "BlexMono Nerd Font",
    "EnvyCodeR Nerd Font",
    "Iosevka Nerd Font",
    #"ProFont Nerd Font",
    "ShureTechMono Nerd Font"
]
#1,2,6,7
widget_defaults = dict(
    font=myFonts[2],
    fontsize=20,
    padding=5,
)
extension_defaults = widget_defaults.copy()

bgColors = {
        "black": "#000000",
        "white": "#ffffff",
        "gray": "#2f343f",
        "other": "#6f6f6f"
        }

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                #widget.TextBox("", fontsize=22),
                widget.GroupBox(inactive=bgColors["other"], highlight_method="line"),
                #widget.TextBox("", fontsize=22),
                widget.Prompt(),
                widget.Spacer(),
                widget.CheckUpdates(distro="Arch_checkupdates", no_update_string="\[T]/", update_interval=10),
                widget.Spacer(),
                #widget.WindowName(),
                #widget.Systray(),
                widget.TextBox("", padding=0, fontsize=43),
                widget.Clock(background=bgColors["white"], foreground=bgColors["black"], format="%d-%m-%Y %a %I:%M %p"),
                widget.TextBox("", padding=0, fontsize=45,background=bgColors["white"], foreground=bgColors["gray"]),
                widget.TextBox("󰕾"),
                widget.PulseVolume(update_interval=0.04),
                widget.TextBox("", padding=0, fontsize=43), 
                widget.Battery(background=bgColors["white"], foreground=bgColors["black"], full_char="󰂅", charge_char="󰢞",discharge_char="󰂀", unknown_char="󰂑", format="{char}{percent: 0.0%} ", update_interval=2),
                #widget.QuickExit(),
            ],
            28,
            #border_width=[2, 10, 5, 10],  # Draw top and bottom border
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background=bgColors["gray"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Godot_Engine"),
        Match(wm_class="feh"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus" #smart
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.client_managed
def show_window(window):
    window.group.cmd_toscreen()
