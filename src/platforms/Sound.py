import pygame

from src.utils import path

pygame.mixer.init()
pygame.mixer.set_num_channels(4)
channels = [
    pygame.mixer.Channel(0),  # jump
    pygame.mixer.Channel(1),  # hit
    pygame.mixer.Channel(2),  # cannons
    pygame.mixer.Channel(3),  # coins
]

jump_sound = pygame.mixer.Sound(path("static/sounds/ha.wav"))
hit_sound = pygame.mixer.Sound(path("static/sounds/ah.wav"))
fire_sound = pygame.mixer.Sound(path("static/sounds/pium.wav"))
coin_sound = pygame.mixer.Sound(path("static/sounds/prim.wav"))


def play_jump():
    channels[0].play(jump_sound)
    return


def play_hit():
    channels[1].play(hit_sound)
    return


def play_fire():
    channels[2].play(fire_sound)
    return


def play_coin():
    channels[3].play(coin_sound)
    return
