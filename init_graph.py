import pygame


def check_values(min_val, max_val, entries):
    if len(entries) == 0:
        print("Invalid entries amount!")
        return True

    m = min(entries)
    n = max(entries)

    errors = len([x for x in entries if x < 0]) > 0 or max_val < n or min_val > m
    if errors:
        print("Invalid inputs!")
    return errors


def get_screen(width, height, min_val, max_val, entries, screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height), width=10)

    x_dist = (width - 50) // (max_val - min_val + 1)
    y_dist = (height - 50) // (len(entries) + 4)

    fonts = pygame.font.Font('freesansbold.ttf', 25)

    for entry in entries:
        num = fonts.render(str(entry), True, (255, 0, 0))
        num_rect = num.get_rect()
        num_rect.center = (25 + entry * x_dist, 15)
        screen.blit(num, num_rect)
        pygame.draw.line(screen,(255, 0, 0), (25 + entry * x_dist, 0), (25 + entry * x_dist, width))

    for entry in [min_val, max_val]:
        num = fonts.render(str(entry), True, (255, 0, 0))
        num_rect = num.get_rect()
        num_rect.center = (25 + entry * x_dist, 15)
        screen.blit(num, num_rect)
        pygame.draw.line(screen, (255, 0, 0), (25 + entry * x_dist, 0), (25 + entry * x_dist, width))

    return x_dist, y_dist
