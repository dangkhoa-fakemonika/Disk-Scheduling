import pygame
import FIFO


def get_shortest_time(entries):
    shortlist = []
    cur_entries = list(entries)
    cur_max = 0
    cur = cur_entries[cur_max]
    cur_entries.pop(cur_max)
    shortlist.append(cur)

    while len(cur_entries) > 0:
        cur_time = 10000000  # Don't even try, I'm hard-coding this
        cur_max = -1
        for i in range(len(cur_entries)):
            if abs(cur - cur_entries[i]) < cur_time:
                cur_time = abs(cur - cur_entries[i])
                cur_max = i

        if cur_max >= 0:
            cur = cur_entries[cur_max]
            cur_entries.pop(cur_max)
            shortlist.append(cur)

    return shortlist


def sstf(screen, entries, x_dist, y_dist):
    movement = 0
    new_entries = get_shortest_time(entries)
    for i in range(len(new_entries) - 1):
        pygame.draw.line(screen, (0, 255, 0),
                         (25 + x_dist * new_entries[i], 30 + y_dist * i),
                         (25 + x_dist * new_entries[i + 1], 30 + y_dist * (i + 1)), 3)
        pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * new_entries[i], 30 + y_dist * i), 8)
        movement += abs(new_entries[i] - new_entries[i + 1])

    pygame.draw.circle(screen, (0, 255, 0), (25 + x_dist * new_entries[-1], 30 + y_dist * (len(new_entries) - 1)), 8)

    fonts = pygame.font.Font('freesansbold.ttf', 25)
    name = fonts.render('SSTF ' + str(movement), True, (255, 255, 255))
    name_rect = name.get_rect()
    name_rect.center = (500, 650)
    screen.blit(name, name_rect)
