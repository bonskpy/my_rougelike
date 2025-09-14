# This file contains logic responsible for procedural map generation.

from typing import Tuple
from game_map import GameMap
import tile_types


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)


def generate_dungeon(dungeon_width, dungeon_height) -> GameMap:
    dungeon = GameMap(width=dungeon_width, height=dungeon_height)

    room1 = RectangularRoom(
        x=20,
        y=15,
        width=10,
        height=15,
    )

    room2 = RectangularRoom(
        x=35,
        y=15,
        width=10,
        height=15,
    )

    dungeon.tiles[room1.inner] = tile_types.floor
    dungeon.tiles[room2.inner] = tile_types.floor

    return dungeon
