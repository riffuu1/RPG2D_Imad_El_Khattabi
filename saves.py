import json
import os
import pygame
from Items import *


def get_save_file(player):
    return f"save_{player.username}.json"


def saving(player, maps, current_map):
    maps_data = []

    for m in maps:
        objets_data = []

        all_objects = (
            m.pickable_objects
            + m.door_objects
            + m.treasure_objects
            + m.pearls_objects
            + m.traps_objects
        )

        for obj in all_objects:
            obj_dict = {
                "obj_id": obj.obj_id,
                "active": obj.active,
                "x": obj.rect.x,
                "y": obj.rect.y,

                "door": getattr(obj, "door", None),
                "finished": getattr(obj, "finished", None),
                "item_taken": getattr(obj, "item_taken", None),
            }

            objets_data.append(obj_dict)

        maps_data.append({
            "bg_name": m.bg_name,
            "objects": objets_data
        })

    data = {
        "player": {
            "id": player.username,
            "x": player.rect.x,
            "y": player.rect.y,
            "hp": player.hp,
            "score": player.score,
            "time_left": player.count,
            "inventory": [item.name for item in player.inventory]
        },

        "maps": maps_data,
        "current_map": current_map.bg_name
    }

    with open(get_save_file(player), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Jeu sauvegardé !")


def charging(player, maps):

    try:
        with open(get_save_file(player), "r", encoding="utf-8") as f:
            data = json.load(f)

        # -------------------
        # Player
        # -------------------
        player.rect.x = data["player"]["x"]
        player.rect.y = data["player"]["y"]
        player.hp = data["player"]["hp"]
        player.score = data["player"]["score"]
        player.count = data["player"]["time_left"]
        player.inventory = []

        for item_name in data["player"]["inventory"]:

            if item_name == "Potion":
                potion_image = pygame.image.load(
                    "assets/Items/heal potion.png"
                )
                potion_image = pygame.transform.scale(
                    potion_image,
                    (50, 50)
                )

                player.inventory.append(
                    Potion("Potion", potion_image)
                )

            elif item_name == "skull_key":
                key_image = pygame.image.load(
                    "assets/Items/Skull_key.png"
                )
                key_image = pygame.transform.scale(
                    key_image,
                    (50, 50)
                )

                player.inventory.append(
                    Key(
                        "skull_key",
                        "skull_key",
                        key_image
                    )
                )

        # -------------------
        # Current Map
        # -------------------
        map_name = data["current_map"]

        current_map = next(
            (m for m in maps if m.bg_name == map_name),
            maps[0]
        )

        # -------------------
        # Objects
        # -------------------
        saved_maps = {
            m["bg_name"]: m
            for m in data["maps"]
        }

        for m in maps:

            if m.bg_name not in saved_maps:
                continue

            saved_objects = {
                obj["obj_id"]: obj
                for obj in saved_maps[m.bg_name]["objects"]
            }

            all_objects = (
                m.pickable_objects
                + m.door_objects
                + m.treasure_objects
                + m.pearls_objects
                + m.traps_objects
            )

            for obj in all_objects:

                if obj.obj_id in saved_objects:

                    saved_obj = saved_objects[obj.obj_id]

                    obj.active = saved_obj["active"]
                    obj.rect.x = saved_obj["x"]
                    obj.rect.y = saved_obj["y"]

                    if hasattr(obj, "door"):
                        obj.door = saved_obj["door"]

                    if hasattr(obj, "finished"):
                        obj.finished = saved_obj["finished"]

                    if hasattr(obj, "item_taken"):
                        obj.item_taken = saved_obj["item_taken"]

        print("Game charged")
        return current_map

    except FileNotFoundError:
        print("No saving file")
        return maps[0]


def existing_backbup(player):
    return os.path.exists(get_save_file(player))