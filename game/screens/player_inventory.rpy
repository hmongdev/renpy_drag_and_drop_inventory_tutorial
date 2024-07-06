default slot_count = 16
default player_inventory = []

screen player_inventory():
    modal True

    # button => close player inventory
    imagebutton:
        align(0.0, 1.0)
        auto "/images/bag %s.png"
        action [Hide(), ToggleScreen('player_hud')]
        at transform:
            xysize(150, 150)

    # inventory frame => grid
    frame:
        background "#000000a4"
        xysize(1280, 720)
        align(0.5, 0.5)

        # grid
        vpgrid cols 4:
            spacing 10
            align(0.5, 0.5)
            for slot in range(slot_count):
                frame:
                    maximum(150, 150)
                    if slot < len(player_inventory):
                        add Image("/images/" + player_inventory[slot] + ".png") align((0.5, 0.5)) xysize((150, 150))
                    else:
                        pass