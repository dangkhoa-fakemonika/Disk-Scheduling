import pygame


def get_path(entries):
    path1 = list([x for x in entries if x >= entries[0]])
    path2 = list([x for x in entries if x < entries[0]])
    path1.sort()
    path2.sort(reverse=True)
    return path1, path2


def fifo(screen, entries, x_dist, y_dist):
    movement = 0

    for i in range(len(entries) - 1):
        pygame.draw.line(screen, (0, 255, 0),
                         (25 + x_dist * entries[i], 30 + y_dist * i),
                         (25 + x_dist * entries[i + 1], 30 + y_dist * (i + 1)), 3)
        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * entries[i], 30 + y_dist * i), 8)
        movement += abs(entries[i] - entries[i + 1])

    pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * entries[-1], 30 + y_dist * (len(entries) - 1)), 8)

    fonts = pygame.font.Font('freesansbold.ttf', 25)
    name = fonts.render('FIFO ' + str(movement), True, (255, 255, 255))
    name_rect = name.get_rect()
    name_rect.center = (500, 650)
    screen.blit(name, name_rect)



