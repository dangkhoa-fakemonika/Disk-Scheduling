import FIFO
import pygame


def generate_path(min_val, max_val, entries):
    path1, path2 = FIFO.get_path(entries)
    new_entries = []

    if entries[0] < entries[1]:
        new_entries.extend(path1)
        new_entries.append(max_val)
        new_entries.extend(path2)
    else:
        new_entries.extend(path2)
        new_entries.append(min_val)
        new_entries.extend(path1)

    return new_entries


def scan(screen, entries, x_dist, y_dist, min_val, max_val):
    movement = 0
    new_entries = generate_path(min_val, max_val, entries)
    for i in range(len(new_entries) - 1):
        pygame.draw.line(screen, (0, 255, 0),
                         (25 + x_dist * new_entries[i], 30 + y_dist * i),
                         (25 + x_dist * new_entries[i + 1], 30 + y_dist * (i + 1)), 3)
        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * new_entries[i], 30 + y_dist * i), 8)
        movement += abs(new_entries[i] - new_entries[i + 1])

    pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * new_entries[-1], 30 + y_dist * (len(new_entries) - 1)), 8)

    fonts = pygame.font.Font('freesansbold.ttf', 25)
    name = fonts.render('SCAN ' + str(movement), True, (255, 255, 255))
    name_rect = name.get_rect()
    name_rect.center = (500, 650)
    screen.blit(name, name_rect)


def c_scan(screen, entries, x_dist, y_dist, min_val, max_val):
    movement = 0
    path1, path2 = FIFO.get_path(entries)
    if entries[0] < entries[1]:
        path2.reverse()
        path1.append(max_val)
        for i in range(len(path1) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path1[i], 30 + y_dist * i),
                             (25 + x_dist * path1[i + 1], 30 + y_dist * (i + 1)), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path1[i], 30 + y_dist * i), 8)
            movement += abs(path1[i] - path1[i + 1])

        pygame.draw.circle(screen, (0, 0, 255), (25 + x_dist * path1[-1], 30 + y_dist * (len(path1) - 1)), 8)

        path2.insert(min_val, 0)
        movement += max_val - min_val
        pygame.draw.line(screen, (0, 0, 255),
                         (25 + x_dist * path1[-1], 30 + y_dist * (len(path1) - 1)),
                         (25 + x_dist * path2[0], 30 + y_dist * (len(path1))), 3)

        for i in range(len(path2) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path2[i], 30 + y_dist * (i + len(path1))),
                             (25 + x_dist * path2[i + 1], 30 + y_dist * (i + 1 + len(path1))), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path2[i], 30 + y_dist * (i + len(path1))), 8)
            movement += abs(path2[i] - path2[i + 1])

        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path2[-1], 30 + y_dist * (len(path2) + len(path1) - 1)), 8)
    else:
        path1.reverse()
        path2.append(min_val)
        for i in range(len(path2) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path2[i], 30 + y_dist * i),
                             (25 + x_dist * path2[i + 1], 30 + y_dist * (i + 1)), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path2[i], 30 + y_dist * i), 8)
            movement += abs(path2[i] - path2[i + 1])

        pygame.draw.circle(screen, (0, 0, 255), (25 + x_dist * path2[-1], 30 + y_dist * (len(path2) - 1)), 8)
        movement += max_val - min_val
        path1.insert(max_val, 0)
        pygame.draw.line(screen, (0, 0, 255),
                         (25 + x_dist * path1[-1], 30 + y_dist * (len(path1) - 1)),
                         (25 + x_dist * path2[0], 30 + y_dist * (len(path1))), 3)
        for i in range(len(path1) - 1):
            pygame.draw.line(screen, (0, 255, 0),
                             (25 + x_dist * path1[i], 30 + y_dist * (i + len(path2))),
                             (25 + x_dist * path1[i + 1], 30 + y_dist * (i + 1 + len(path2))), 3)
            pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path1[i], 30 + y_dist * (i + len(path2))), 8)
            movement += abs(path1[i] - path1[i + 1])
        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * path1[-1], 30 + y_dist * (len(path2) + len(path1) - 1)),
                           8)

    fonts = pygame.font.Font('freesansbold.ttf', 25)
    name = fonts.render('C-SCAN ' + str(movement), True, (255, 255, 255))
    name_rect = name.get_rect()
    name_rect.center = (500, 650)
    screen.blit(name, name_rect)
