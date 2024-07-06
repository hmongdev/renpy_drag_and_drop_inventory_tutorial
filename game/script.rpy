label start:
    scene image Solid("#fff")
    show screen player_hud
    
    # show env_screen
    show screen env_screen

    # menu One:
    #     "What do you want to do?"

    #     "Increase Health":
    #         $ player_hp += 10
    #         jump start
    #     "Decrease Health":
    #         $ player_hp -= 10
    #         jump start
    #     "Increase Gold":
    #         $ player_gold += 10
    #         jump start
    #     "Decrease Gold":
    #         $ player_gold -= 10
    #         jump start
    #     "Add Iron Armor":
    #         $ player_inventory.append("leather h")
    #         jump start
    #     "Remove Iron Armor":
    #         $ player_inventory.remove("leather h")
    #         jump start
    pause
    return
