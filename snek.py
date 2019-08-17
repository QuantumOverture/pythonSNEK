import pygame,random

pygame.init()

x = 40
y = 40
snek = []
health = 4

# To Do list --> Menu, dots, score, gameover

screen = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()
done = False
move ="R"
FPS = 12
counter = 0
head = pygame.Rect(x,y,30,30)
gem = pygame.Rect((random.randint(0, 30)) * 30, random.randint(0, 20) * 30, 30, 30)
pygame.draw.rect(screen,(255,0,0),gem)
score = 0
pygame.display.set_caption('Score: ' + str(score))

pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
snek.append(pygame.Rect(x, y, 30, 30))
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            health+=1
    if move == "U":
        if (len(snek) < health):
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
            head = pygame.Rect(x, y, 30, 30)
            y = y - 35
            snek.append(pygame.Rect(x, y, 30, 30))
            clock.tick(FPS)
            pygame.display.flip()
        else:
            clock.tick(FPS)
            pygame.draw.rect(screen, (0, 0, 0), snek[0])
            snek.pop(0)
            pygame.display.flip()
    if move == "D":
        if (len(snek) < health):
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
            head = pygame.Rect(x, y, 30, 30)
            y = y + 35
            snek.append(pygame.Rect(x, y, 30, 30))
            clock.tick(FPS)
            pygame.display.flip()
        else:
            clock.tick(FPS)
            pygame.draw.rect(screen, (0, 0, 0), snek[0])
            snek.pop(0)
            pygame.display.flip()
    if move == "R":

        if (len(snek) < health):
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
            head = pygame.Rect(x, y, 30, 30)
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
        if (len(snek) < health):
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 30, 30))
            head = pygame.Rect(x, y, 30, 30)
            x = x - 35
            snek.append(pygame.Rect(x, y, 30, 30))
            clock.tick(FPS)
            pygame.display.flip()
        else:
            clock.tick(FPS)
            pygame.draw.rect(screen, (0, 0, 0), snek[0])
            snek.pop(0)
            pygame.display.flip()

    if head.colliderect(gem):
        pygame.draw.rect(screen, (0, 0, 0), gem)
        gem = pygame.Rect((random.randint(1, 29)) * 30, random.randint(1, 19) * 30, 30, 30)
        pygame.draw.rect(screen, (255, 0, 0), gem)
        score += 1
        health += 1
        pygame.display.set_caption('Score: '+ str(score))


pygame.quit()