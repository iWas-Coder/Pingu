# === Qtile (LAYOUTS) Configuration by iWas <3 === #


from libqtile import layout


# === General properties === #
layout_conf = {
     "border_focus": "#a151d3",
     "border_width": 3,
     "margin": 25
}

# === Layouts === #
layouts = [
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf)
]
