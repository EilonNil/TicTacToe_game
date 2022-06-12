from objects.circle import Circle


def summon_c(screen, x, y, POSITIONS, placements):  # summons a circle according to the place the user clicked
    if x < 128 and y < 128:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['11'])
        placements[0][0] = 3
    elif x < 233 and y < 128:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['12'])
        placements[0][1] = 3
    elif y < 128:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['13'])
        placements[0][2] = 3
    elif x < 128 and y < 233:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['21'])
        placements[1][0] = 3
    elif x < 233 and y < 233:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['22'])
        placements[1][1] = 3
    elif y < 233:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['23'])
        placements[1][2] = 3
    elif x < 128 and y < 360:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['31'])
        placements[2][0] = 3
    elif x < 233 and y < 360:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['32'])
        placements[2][1] = 3
    elif y < 360:
        circle = Circle()
        screen.blit(circle.image, POSITIONS['33'])
        placements[2][2] = 3