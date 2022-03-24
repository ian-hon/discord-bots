import discord
from discord.ext import commands
import random


def colour(_random=False):
    if _random:
        return random.randint(0x100000, 0xFFFFFF)
    else:
        return 55807


def get_ping_colour(_i):
    _min = 0
    _max = 500
    _percent = (_i - _min) / _max - _min
    _r = 510 * _percent
    _g = 510 * (1 - _percent)
    if _r > 255:
        _r = 255
    if _g > 255:
        _g = 255
    return _r, _g


def dynamic_color(i):
    """Enter a float from 0-1 and will return red and green values accordingly,
    with 0 being fully green and 1 being fully red"""
    r = 255 * i
    g = 255 * (1 - i)

    if r > 255:
        r = 255
    elif r < 0:
        r = 0

    if g > 255:
        g = 255
    elif g < 0:
        g = 0

    return int(r), int(g)


def uptime_string(enoch_time):
    if enoch_time > 3600:
        hour = enoch_time // 3600
        minute = (enoch_time / 60) - (int(hour) * 60)
        return f"{int(hour)}h {int(minute)}m"
    else:
        minute = enoch_time / 60
        second = enoch_time - (int(minute) * 60)
        return f"{int(minute)}m {int(second)}s"


def beautify_dict(d, indent=0):
    final = ''
    for key, value in d.items():
        final += '\t' * indent + str(key)
        if isinstance(value, dict):
            beautify_dict(value, indent+1)
        else:
            final += '\t' * (indent+1) + str(value)
    return final
