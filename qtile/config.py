from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Change Focus:
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Swap places:
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    Key([mod, "control"], "j", lazy.layout.grow_down(), lazy.layout.shrink().when('xmonad-tall')),
    Key([mod, "control"], "k", lazy.layout.grow_up(), lazy.layout.grow().when('xmonad-tall')),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),

    Key([mod], "w", lazy.to_screen(0)),
    Key([mod], "y", lazy.to_screen(1)),
    Key([mod, "shift"], "w", lazy.window.to_screen(0)),
    Key([mod, "shift"], "y",lazy.window.to_screen(1)),

    # Move the master pane Left/Right:
    Key([mod, "shift"], "space", lazy.layout.flip()),

    Key([mod, "shift"], "h", lazy.layout.client_to_previous()),
    Key([mod, "shift"], "l", lazy.layout.client_to_next()),

    # Toggel fullscreen on/off:
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Change Layout:
    Key([mod], "Tab", lazy.next_layout()),

    # Close focused window:
    Key([mod], "q", lazy.window.kill()),

    # Restart qtile in place:
    Key([mod, "control"], "r", lazy.restart()),

    # Open a run prompt:
    Key([mod], "r", lazy.spawncmd()),

    # Applications/Scripts Shortcuts:
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], 'x', lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu")),
    Key([mod, "shift"], "f", lazy.spawn("firefox")),
    Key([mod, "shift"], "c", lazy.spawn("code-oss")),
    Key([mod, "shift"], "t", lazy.spawn("thunderbird")),
    Key([mod, "shift"], "b", lazy.spawn("thunar")),

    # Audio buttons
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%-")),

    Key([], "XF86AudioMute", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioMute", lazy.spawn("playerctl next")),
    Key([], "XF86AudioMute", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioMute", lazy.spawn("playerctl stop")),
]

groups = [
    Group("1", matches=[Match(wm_class=["firefox"])], label=""),
    Group("2", matches=[Match(wm_class=["alacritty"])], label=""),
    Group("3", matches=[Match(wm_class=["code", "code-oss", "atom"])], label=""),
    Group("4", matches=[Match(wm_class=["vim"])], label=""),
    Group("5", matches=[Match(wm_class=["libreoffice"])], label=""),
    Group("6", matches=[Match(wm_class=["thunderbird"])], label=""),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        #     desc="move focused window to group {}".format(i.name)),
        ])

layouts = [
        layout.Columns(border_focus_stack='#fa6000', margin=0),
        # layout.Max(),
        layout.Stack(num_stacks=2, margin=0),
        # layout.Bsp(),
        # layout.Matrix(),
        layout.MonadTall(margin=0),
        # layout.MonadWide(),
        # layout.RatioTile(),
        layout.Tile(margin=0),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        ]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()

topBar = bar.Bar([
    widget.CurrentLayoutIcon(scale=0.5),
    widget.GroupBox(),
    widget.Prompt(),
    widget.WindowName(),
    widget.Chord(
        chords_colors={
            'launch': ("#fa6000", "#ffffff"),
            },
        name_transform=lambda name: name.upper(),
        ),
    widget.Systray(),
    widget.Volume(cardid=2, device=12, channel='Master', emoji=True),

    widget.TextBox(text='|', foreground="d08770"),
    widget.Net(foreground="d08770"),

    widget.TextBox(text='|  ', foreground="a3be8c"),
    widget.Wlan(
        foreground="a3be8c",
        interface="wlp5s0",
        format="{essid} ",
    ),

    widget.TextBox(text='|  ', foreground="ebcb8b"),
    widget.Clock(format='%a %d.%m.%Y %H:%M', foreground="ebcb8b"),

    widget.TextBox(text='|   ', foreground="b48ead"),
    widget.QuickExit(default_text='Shutdown', countdown_format="{} seconds", foreground="b48ead"),
    widget.TextBox(text=' '),
], 32, background="#1f262a") # margin=[10,10,0,10]

screens = [
        Screen(
            top=topBar,
            wallpaper='~/Pictures/wallpapers/carina-nebula.jpg',
            wallpaper_mode='fill',
            ),
        Screen(
            top=bar.Bar([
                widget.CurrentLayoutIcon(scale=0.5),
                widget.GroupBox(),
                widget.WindowName(),
            ], 32, background="1f262a"),
            wallpaper='~/Pictures/wallpapers/carina-nebula.jpg',
            wallpaper_mode='fill',
            ),
        Screen(
            top=bar.Bar([
                widget.CurrentLayoutIcon(scale=0.5),
                widget.GroupBox(),
                widget.WindowName(),
            ], 32, background="1f262a"),
            wallpaper='~/Pictures/wallpapers/carina-nebula.jpg',
            wallpaper_mode='fill',
            ),
        Screen(
            top=bar.Bar([
                widget.CurrentLayoutIcon(scale=0.5),
                widget.GroupBox(),
                widget.WindowName(),
                ], 32, background="1f262a"),
            wallpaper='~/Pictures/wallpapers/carina-nebula.jpg',
            wallpaper_mode='fill',
            )
        ]

# Drag floating layouts.
mouse = [
        #Drag([mod], "Button1", lazy.window.set_position_floating(),
        #     start=lazy.window.get_position()),
        Drag([mod], "Button1", lazy.window.set_position(),
            start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
            start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
        ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    subprocess.call([os.path.expanduser('~') + '/.local/bin/autostart.sh'])
