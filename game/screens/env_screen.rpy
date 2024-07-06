# list that holds all the armor
default armor_list = ['leather h', 'leather m', 'leather l']

init python:
    def add_item(player_inv, dragged_item):
        global player_inventory
        item_name = dragged_item[0].drag_name
        print(f"{item_name} was added to your inventory.")

        # add to player's inventory
        player_inventory.append(item_name)

        # remove item from screen
        dragged_item[0].set_child(Null())

screen env_screen():
    #draggroup
    draggroup:
        drag:
            align(0.0, 1.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item
            imagebutton:
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(150, 150)

    # for loop to list out drags
        for armor in armor_list:
            drag:
                align((0.5, 0.5))
                drag_name armor
                drag_raise True
                add f"/images/{armor}.png" xysize (300, 300)