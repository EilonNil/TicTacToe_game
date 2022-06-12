from objects.cross import X


def summon_x(screen, x, y, POSITIONS, placements):  # summons a cross according to the place the user clicked
    if x < 128 and y < 128:
        cross = X()
        screen.blit(cross.image, POSITIONS['11'])
        placements[0][0] = 2
    elif x < 233 and y < 128:
        cross = X()
        screen.blit(cross.image, POSITIONS['12'])
        placements[0][1] = 2
    elif y < 128:
        cross = X()
        screen.blit(cross.image, POSITIONS['13'])
        placements[0][2] = 2
    elif x < 128 and y < 233:
        cross = X()
        screen.blit(cross.image, POSITIONS['21'])
        placements[1][0] = 2
    elif x < 233 and y < 233:
        cross = X()
        screen.blit(cross.image, POSITIONS['22'])
        placements[1][1] = 2
    elif y < 233:
        cross = X()
        screen.blit(cross.image, POSITIONS['23'])
        placements[1][2] = 2
    elif x < 128 and y < 360:
        cross = X()
        screen.blit(cross.image, POSITIONS['31'])
        placements[2][0] = 2
    elif x < 233 and y < 360:
        cross = X()
        screen.blit(cross.image, POSITIONS['32'])
        placements[2][1] = 2
    elif y < 360:
        cross = X()
        screen.blit(cross.image, POSITIONS['33'])
        placements[2][2] = 2

