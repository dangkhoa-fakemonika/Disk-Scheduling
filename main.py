import pygame
import init_graph, FIFO, SSTF, SCAN, LOOK


SCR_WIDTH = 1000
SCR_HEIGHT = 720
options = 0
on_clicked = False

pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
screen.fill((0, 0, 0))

# Insert you entries here, entry[0] is the read-hand and entry[1] != entry[0]
entries = (11, 13, 2, 38, 17, 36, 7, 21)

# Insert your range here (must be valid range)
min_val = 0  # Min should always be 0 though
max_val = 40

errors = init_graph.check_values(min_val, max_val, entries)
if errors:
    exit()
x_dist, y_dist = init_graph.get_screen(SCR_WIDTH, SCR_HEIGHT, min_val, max_val, entries, screen)

# FIFO.fifo(screen, entries, x_dist, y_dist)
# SSTF.sstf(screen, entries, x_dist, y_dist)
# SCAN.scan(screen, entries, x_dist, y_dist, min_val, max_val)
# LOOK.look(screen, entries, x_dist, y_dist)
# SCAN.c_scan(screen, entries, x_dist, y_dist, min_val, max_val)
# LOOK.c_look(screen, entries, x_dist, y_dist)

pygame.display.flip()

running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            break
        if events.type == pygame.KEYDOWN and not on_clicked:
            if events.key == pygame.K_LEFT:
                options -= 1
                if options < 0:
                    options = 5
                on_clicked = True
            if events.key == pygame.K_RIGHT:
                options += 1
                if options > 5:
                    options = 0
                on_clicked = True
        if events.type == pygame.KEYUP and on_clicked:
            on_clicked = False

        init_graph.get_screen(SCR_WIDTH, SCR_HEIGHT, min_val, max_val, entries, screen)
        if options == 0:
            FIFO.fifo(screen, entries, x_dist, y_dist)
        elif options == 1:
            SSTF.sstf(screen, entries, x_dist, y_dist)
        elif options == 2:
            SCAN.scan(screen, entries, x_dist, y_dist, min_val, max_val)
        elif options == 3:
            SCAN.c_scan(screen, entries, x_dist, y_dist, min_val, max_val)
        elif options == 4:
            LOOK.look(screen, entries, x_dist, y_dist)
        elif options == 5:
            LOOK.c_look(screen, entries, x_dist, y_dist)

        pygame.display.flip()
pygame.quit()


