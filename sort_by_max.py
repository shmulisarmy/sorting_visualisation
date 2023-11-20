import pygame, random

def handle_display():
    window.fill('black')

    for i, num in enumerate(numbers):
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(PILLAR_WIDTH*i, 0, PILLAR_WIDTH, PILLAR_HEIGHT*num))

    pygame.display.update()

pygame.init()
WIDTH, HEIGHT = 800, 800
MAX_NUM_AMOUNT = 100
FPS = MAX_NUM_AMOUNT//20
numbers = [random.randint(1, 60) for i in range(random.randint(5, MAX_NUM_AMOUNT))]
PILLAR_WIDTH, PILLAR_HEIGHT = WIDTH/len(numbers), HEIGHT/max(numbers)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

for i in range(len(numbers)-1, -1, -1):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    max_num = max(numbers[:i:])
    numbers[numbers.index(max_num)], numbers[i] = numbers[i], max_num

    handle_display()

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    handle_display()