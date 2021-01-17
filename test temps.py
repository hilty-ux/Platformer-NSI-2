import pygame

screen = pygame.display.set_mode((100, 100))
running = True
clock = pygame.time.Clock()
begin_time = pygame.time.get_ticks()
actual_time = 0
color = [(255, 0, 0), (0, 255, 0)]
color_index = 0

pygame.init()
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    actual_time = pygame.time.get_ticks()
    if actual_time - begin_time > 1000:
        if color_index == 1:
            color_index -= 1
        else:
            color_index += 1
        begin_time = pygame.time.get_ticks()

    screen.fill(color[color_index])
    pygame.display.flip()

pygame.quit()