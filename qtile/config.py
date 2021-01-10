# --- My personal Qtile config.--- #

# --- Imports
import os
import re
import socket
import subprocess

from libqtile import extension
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.widget import Spacer
from libqtile.log_utils import logger
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from powerline.bindings.qtile.widget import PowerlineTextBox
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click

# --- Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# --- Setting personal definitions
mod = "mod4"
terminal = "st"
editor = "emacs"
wmname = "Qtile"

# --- My nord colors 
nord0 = "#2E3440" ## Polar night
nord1 = "#3B4252" ## Brighter polar night
nord2 = "#434C5E" ## Even brighter polar night
nord3 = "#4C566A" ## Brightest polar night
nord4 = "#D8DEE9" ## Snow storm
nord5 = "#E5E9F0" ## Brighter snowstorm
nord6 = "#ECEFF4" ## Brightest snowstorm
nord7 = "#8FBCBB" ## Frost teal
nord8 = "#88C0D0" ## Frost Cyan
nord9 = "#81A1C1" ## Frost light blue
nord10 = "#5E81AC" ## Frost deep blue
nord11 = "#BF616A" ## Aurora red
nord12 = "#D08770" ## Aurora orange
nord13 = "#EBCB8B" ## Aurora yellow
nord14 = "#A3BE8C" ## Aurora green
nord15 = "#B48EAD" ## Aurora puprle

# --- Keybindings
keys = [

    # Logout/Restart Qtile and kill widoows
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Dmenu extension
    Key(['mod4'], 'p', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="Run ->",
        dmenu_font="terminus:size=8",
        background = "#2E3440",
        foreground = "#4C566A",
        selected_background = "#81A1C1",
        selected_foreground = "#2E3440",
        dmenu_height = 20,  # Only supported by some dmenu forks
    ))),

    # Monadtall keybindings 
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Editor keybindings
    Key([mod, "control"], "1", lazy.spawn(editor + " ~/.config/qtile/config.py"),
        desc="Edit my qtile config"),
    Key([mod, "control"], "2", lazy.spawn(editor + " ~/.config/qtile/autostart.sh"),
        desc="Edit my qtile autostart script"),
    Key([mod, "control"], "3", lazy.spawn(editor + " ~/.xinitrc"),
        desc="Edit my xinitrc"),
    Key([mod, "control"], "e", lazy.spawn(editor),
        desc="Launch my editor"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 2%+"),
        desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 2%-"),
        desc="Brightness down"),

    # Audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"),
        desc="Turning up volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute"),
        desc="Turning down volume"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"),
        desc="Toggling audio"),

    Key([mod, "control"], "d", lazy.spawn("discord --no-sandbox &"),
        desc="Launching discord without sandbox"),

    Key([mod, "control"], "b", lazy.spawn("firefox"),
        desc="launching my browser"),

    Key([mod, "control"], "n", lazy.spawn("nitrogen"),
        desc="launch nitrogen"),

    Key([mod, "control"], "h", lazy.spawn("st -e htop"),
        desc="Launch htop"),

    Key([mod, "control"], "w", lazy.spawn("st -e nmtui"),
        desc="Open ncurses nmtui configuration"),
    
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),
    
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

]

# --- Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# --- Default floating rules
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},
    {'wmclass': 'discord'},
    {'wmclass': 'Nitrogen'},
    {'wmclass': 'Pavucontrol'},
    {'wmclass': 'Gnome-screenshot'},
    {'wmclass': 'Gimp'},
    {'wmclass': 'Spotify'},
    {'wmclass': 'Gpick'},
    {'wmclass': 'Xarchiver'}, # ssh-askpass
    
], border_width = 2, border_focus = nord3, border_normal = nord0) 
auto_fullscreen = True
focus_on_window_activation = "smart"

# --- Defining groups 
group_names = [("TERM", {'layout': 'monadtall'}),
               ("WEB", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MEDIA", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'monadtall'}),
               ("VM", {'layout': 'monadtall'}),
               ("MISC", {'layout': 'monadtall'})]
               # ("VIII", {'layout': 'monadtall'}),
               # ("IX", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

# --- Default layout rules
layout_theme = {"border_width": 2,
                "margin": 16,
                "border_focus": "#4C566A",
                "border_normal": "#2E3440"
                }

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# --- Panel defaults
widget_defaults = dict(
    font="terminus",
    fontsize = 12,
    padding = 4,
    background = nord0,
    border_active = nord8,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                active = nord9,
                inactive = nord3,
                block_highlight_text_color = nord14,
                this_current_screen_border = nord9,
                highlight_color = nord0,
                highlight_method = 'line',
                background = nord0,
                borderwidth = 2,
                ),
                
                widget.TaskList(
                spacing = 5,
                foreground = nord0,
                border = nord8,
                fontsize = 10,
                unfocused_border = nord9,
                highlight_method = "block",
                max_title_width=125,
                title_width_method="uniform",
                icon_size = 0,
                rounded=False,
                padding = 3,
                padding_x = 0,
                padding_y = 3,
                # txt_floating = '>())>'
                ),

                Spacer(),

                widget.TextBox(
                text = "",
                fontsize = 30,
                background = nord0,
                foreground = nord7,
                padding = 0,
                ),
                
                widget.Net(
                format = '↓↑  {down} {up}',
                use_bits = True,
                padding = 10,
                fontsize = 12,
                foreground = nord0,
                background = nord7,
                ),

                widget.TextBox(
                text = "",
                fontsize = 30,
                background = nord7,
                foreground = nord9,
                padding = 0,
                ),

                widget.TextBox(
                background = nord9,
                padding = 0
                ),

                widget.TextBox(
                text = '',
                fontsize = 16,
                foreground = nord0,
                background = nord9,
                padding = 0,
                ),

                widget.Volume(
                background = nord9,
                foreground = nord0,
                padding = 10,
                ),

                widget.TextBox(
                text = "",
                fontsize = 30,
                background = nord9,
                foreground = nord7,
                padding = 0,
                ),
            
                widget.TextBox(
                text = '',
                fontsize = 14,
                foreground = nord0,
                background = nord7,
                padding = 2,
                ),
            
                widget.Battery(
                format = '{percent:2.0%}',
                fontsize = 12,
                background = nord7,
                foreground = nord0,
                padding = 5,
                ),

                widget.TextBox(
                text = "",
                fontsize = 30,
                background = nord7,
                foreground = nord9,
                padding = 0,
                ),
            
                widget.Clock(format='%I:%M %p',
                padding = 5,
                foreground = nord0,
                background = nord9,
                ),
              
                widget.CurrentLayout(
                padding = 5,
                foreground = nord0,
                background = nord9,
                ),
            ],
            24,
        ),
    ),
]

# --- End of config.
