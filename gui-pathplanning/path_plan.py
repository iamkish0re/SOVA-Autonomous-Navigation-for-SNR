#!/usr/bin/python

import pygame
import pygame_widgets as pw
import json
import math

"""
how many pixel = actual distance in cm
70px = 360cm --> 360/70 = MAP_SIZE_COEFF
"""

MAP_SIZE_COEFF = 5.14

class Background(pygame.sprite.Sprite):
    def __init__(self, image, location, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def get_dist_btw_pos(pos0, pos1):
    """
    Get distance between 2 mouse position.
    """
    x = abs(pos0[0] - pos1[0])
    y = abs(pos0[1] - pos1[1])
    dist_px = math.hypot(x, y)
    dist_cm = dist_px * MAP_SIZE_COEFF
    return int(dist_cm), int(dist_px)


def get_angle_btw_line(pos0, pos1, posref):
    """
    Get angle between two lines respective to 'posref'
    NOTE: using dot product calculation.
    """
    ax = posref[0] - pos0[0]
    ay = posref[1] - pos0[1]
    bx = posref[0] - pos1[0]
    by = posref[1] - pos1[1]
    # Get dot product of pos0 and pos1.
    _dot = (ax * bx) + (ay * by)
    # Get magnitude of pos0 and pos1.
    _magA = math.sqrt(ax**2 + ay**2)
    _magB = math.sqrt(bx**2 + by**2)
    _rad = math.acos(_dot / (_magA * _magB))
    # Angle in degrees.
    angle = (_rad * 180) / math.pi
    return int(angle)


"""
Main capturing mouse program.
"""
# Load background image.
def map_points():

    pygame.init()
    screen = pygame.display.set_mode([720, 720])
    # button = pygame.Rect(100, 100, 50, 50)
    button = pw.Button(
            screen, 100, 100, 75, 150, text='Hello',
            fontSize=50, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: print('Click')
        )
    screen.fill((255, 255, 255))
    running = True
    bground = Background('licet.png', [0, 0], 1.6)
    screen.blit(bground.image, bground.rect)

    path_wp = []
    index = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                path_wp.append(pos)
                if index > 0:
                    pygame.draw.line(screen, (255, 0, 0), path_wp[index-1], pos, 2)
                index += 1

                # if button.collidepoint(pos):
                #     # prints current location of mouse
                #     print('button was pressed at {0}'.format(pos))

        # pygame.draw.rect(screen, [255, 0, 0], button)
        pygame.display.update()

    """
    Compute the waypoints (distance and angle).
    """
    # Append first pos ref. (dummy)

    path_wp.insert(0, (path_wp[0][0], path_wp[0][1] - 10))

    path_dist_cm = []
    path_dist_px = []
    path_angle = []
    for index in range(len(path_wp)):
        # Skip the first and second index.
        if index > 1:
            dist_cm, dist_px = get_dist_btw_pos(path_wp[index-1], path_wp[index])
            path_dist_cm.append(dist_cm)
            path_dist_px.append(dist_px)

        # Skip the first and last index.
        if index > 0 and index < (len(path_wp) - 1):
            angle = get_angle_btw_line(path_wp[index-1], path_wp[index+1], path_wp[index])
            path_angle.append(angle)

    # Print out the information.
    print('path_wp: {}'.format(path_wp))
    print('dist_cm: {}'.format(path_dist_cm))
    print('dist_px: {}'.format(path_dist_px))
    print('dist_angle: {}'.format(path_angle))

    """
    Save waypoints into JSON file.
    """
    waypoints = []
    for index in range(len(path_dist_cm)):
        waypoints.append({
            "dist_cm": path_dist_cm[index],
            "dist_px": path_dist_px[index],
            "angle_deg": path_angle[index]
        })

    # Save to JSON file.
    f = open('waypoint.json', 'w+')
    path_wp.pop(0)
    json.dump({
        "wp": waypoints,
        "pos": path_wp
    }, f, indent=4)
    f.close()
