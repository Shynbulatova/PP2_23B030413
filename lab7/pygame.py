# Lab 7
# Learn tutorial: https://nerdparadise.com/programming/pygame: * Getting Started * Working with Images * Music and Sound Effects * Geometric Drawing * Fonts and Text * More on Input

# Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use: pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144

# mickeyclock
# Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.

# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
import pygame
import sys
import time
import math

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load("mickey.png")
mickey_rect = mickey_image.get_rect(center=(screen_width // 2, screen_height // 2))

clock = pygame.time.Clock()

def draw_clock():
    current_time = time.localtime()
    seconds_angle = (current_time.tm_sec / 60) * 360
    minutes_angle = (current_time.tm_min / 60) * 360
    mickey_seconds_hand = pygame.transform.rotate(mickey_image, -seconds_angle)
    mickey_minutes_hand = pygame.transform.rotate(mickey_image, -minutes_angle)
    screen.blit(mickey_minutes_hand, mickey_rect)
    screen.blit(mickey_seconds_hand, mickey_rect)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_clock()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
