import pygame

pygame.init()

x = 40
y = 40
snek = []
health = 3
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
move ="R"
FPS = 10
counter = 0



while not done:
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move = "U"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move = "D"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move = "R"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move = "L"
    if move == "U":
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
        y = y - 35
        snek.append(pygame.Rect(x, y, 30, 30))
        clock.tick(FPS)
        pygame.display.flip()

    if move == "D":

        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
        y = y + 35
        snek.append(pygame.Rect(x, y, 30, 30))
        clock.tick(FPS)
        pygame.display.flip()

    if move == "R":

        if (len(snek) <= health):
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
            x = x + 35
            snek.append(pygame.Rect(x, y, 30, 30))
            clock.tick(FPS)
            pygame.display.flip()

        else:
            clock.tick(FPS)
            pygame.draw.rect(screen, (0, 0, 0), snek[0])
            snek.pop(0)
            pygame.display.flip()

    if move == "L":
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
        x = x - 35
        snek.append(pygame.Rect(x, y, 30, 30))
        clock.tick(FPS)
        pygame.display.flip()





pygame.quit()