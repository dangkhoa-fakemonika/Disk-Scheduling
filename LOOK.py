import FIFO
import pygame


def generate_path(entries):
    path1, path2 = FIFO.get_path(entries)
    new_entries = []
    if entries[0] < entries[1]:
        new_entries.extend(path1)
        new_entries.extend(path2)
    else:
        new_entries.extend(path2)
        new_entries.extend(path1)

    return new_entries


def look(screen, entries, x_dist, y_dist):
    movement = 0
    new_entries = generate_path(entries)
    for i in range(len(new_entries) - 1):
        pygame.draw.line(screen, (0, 255, 0),
                         (25 + x_dist * new_entries[i], 30 + y_dist * i),
                         (25 + x_dist * new_entries[i + 1], 30 + y_dist * (i + 1)), 3)
        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * new_entries[i], 30 + y_dist * i), 8)
        movement += abs(new_entries[i] - new_entries[i + 1])

    pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * new_entries[-1], 30 + y_dist * (len(new_entries) - 1)), 8)

    fonts = pygame.font.Font('freesansbold.ttf', 25)
    name = fonts.render('LOOK ' + str(movement), True, (255, 255, 255))
    name_rect = name.get_rect()
    name_rect.center = (500, 650)
    screen.blit(name, name_rect)


def c_look(screen, entries, x_dist, y_dist):
    movement = 0
    path1, path2 = FIFO.get_path(entries)
    if entries[0] < entries[1]:
        path2.reverse()
        for i in range(len(path1) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path1[i], 30 + y_dist * i),
                             (25 + x_dist * path1[i + 1], 30 + y_dist * (i + 1)), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path1[i], 30 + y_dist * i), 8)
            movement += abs(path1[i] - path1[i + 1])

        pygame.draw.circle(screen, (0, 0, 255), (25 + x_dist * path1[-1], 30 + y_dist * (len(path1) - 1)), 8)
        movement += abs(path1[-1] - path2[0])
        pygame.draw.line(screen, (0, 0, 255),
                         (25 + x_dist * path1[-1], 30 + y_dist * (len(path1) - 1)),
                         (25 + x_dist * path2[0], 30 + y_dist * (len(path1))), 3)
        for i in range(len(path2) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path2[i], 30 + y_dist * (i + len(path1))),
                             (25 + x_dist * path2[i + 1], 30 + y_dist * (i + 1 + len(path1))), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path2[i], 30 + y_dist * (i + len(path1))), 8)
            movement += abs(path2[i] - path2[i + 1])
        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path2[-1], 30 + y_dist * (len(path2) + len(path1) - 1)),
                           8)
    else:
        path1.reverse()
        for i in range(len(path2) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path2[i], 30 + y_dist * i),
                             (25 + x_dist * path2[i + 1], 30 + y_dist * (i + 1)), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path2[i], 30 + y_dist * i), 8)
            movement += abs(path2[i] - path2[i + 1])

        pygame.draw.circle(screen, (0, 0, 255), (25 + x_dist * path2[-1], 30 + y_dist * (len(path2) - 1)), 8)
        pygame.draw.line(screen, (0, 0, 255),
                         (25 + x_dist * path2[-1], 30 + y_dist * (len(path1) - 1)),
                         (25 + x_dist * path1[0], 30 + y_dist * (len(path1))), 3)
        movement += abs(path2[-1] - path1[0])
        for i in range(len(path1) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path1[i], 30 + y_dist * (i + len(path2))),
                             (25 + x_dist * path1[i + 1], 30 + y_dist * (i + 1 + len(path2))), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path1[i], 30 + y_dist * (i + len(path2))), 8)
            movement += abs(path1[i] - path1[i + 1])

        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path1[-1], 30 + y_dist * (len(path2) + len(path1) - 1)),
                           8)

    fonts = pygame.font.Font('freesansbold.ttf', 25)
    name = fonts.render('C-LOOK ' + str(movement), True, (255, 255, 255))
    name_rect = name.get_rect()
    name_rect.center = (500, 650)
    screen.blit(name, name_rect)
