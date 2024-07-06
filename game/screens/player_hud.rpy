default player_hp = 100
default player_hp_max = 100
default player_gold = 100

screen player_hud():
    # health bar
    vbox:
        align((0.05, 0.025))
        bar:
            value AnimatedValue(player_hp, player_hp_max, delay=1.0)
            left_bar "/gui/bar/left.png"
            right_bar "/gui/bar/right.png"
            maximum(525, 38)

    # gold count
    frame:
        align(0.97, 0.025)
        xysize((500, 100))
        padding(30, 10)
        hbox:
            spacing 100
            align(0.5, 0.5)
            image Solid("#ffcc00"):
                align(0.5, 0.5)
                xysize(75, 75)
            text "Gold [player_gold]" size 50

    # inventory button
    