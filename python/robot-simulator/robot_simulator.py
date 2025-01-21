# Globals for the directions
# Change the values as you see fit
EAST = object()
NORTH = object()
WEST = object()
SOUTH = object()


class Robot:
    right_hand_orientation = {
        EAST: SOUTH,
        NORTH: EAST,
        WEST: NORTH,
        SOUTH: WEST,
    }

    left_hand_orientation = {
        EAST: NORTH,
        NORTH: WEST,
        WEST: SOUTH,
        SOUTH: EAST,
    }

    offsets_per_direction = {
        EAST: (1, 0),
        NORTH: (0, 1),
        WEST: (-1, 0),
        SOUTH: (0, -1),
    }

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            match instruction:
                case "R":
                    self.direction = self.right_hand_orientation[self.direction]
                case "L":
                    self.direction = self.left_hand_orientation[self.direction]
                case "A":
                    self.coordinates = tuple(
                        coord + offset
                        for coord, offset in zip(
                            self.coordinates, self.offsets_per_direction[self.direction]
                        )
                    )
