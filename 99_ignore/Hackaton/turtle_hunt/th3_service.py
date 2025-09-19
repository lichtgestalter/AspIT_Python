"""Opgave "Turtle Hunt": Service funktioner

Du må ikke redigere denne fil!

Læs øvelsesbeskrivelsen i th1_exercise.py."""

import math


def distance(pos1, pos2):  # calculate the distance between 2 points with the Pythagorean equation
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def direction(start_position, end_position):
    # returns the direction from start_position to end_position in degrees
    # 0° is east (plus x-axis), which is also the direction of each turtle at the beginning of each hunt.
    # 90° is south (minus y-axis), 180° is west (minus x-axis), 270° is north (plus y-axis)
    #
    #           270°
    #            N
    #            |
    #   180° W --o-- E 0°
    #            |
    #            S
    #           90°
    #
    delta_x = end_position[0] - start_position[0]
    delta_y = end_position[1] - start_position[1]
    angle = math.atan2(delta_y, delta_x) * 180 / math.pi
    if delta_y < 0:
        return -angle
    else:
        return 360 - angle
