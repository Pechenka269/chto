import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    c = 100
    running = True
    k = 0
    tex = pygame.font.Font(None, 111)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEOEXPOSE:
                k += 1

        screen.fill((0, 0, 0))
        text = tex.render(str(k), True, 'red')
        text_rect = text.get_rect(center=(c, c))
        screen.blit(text, text_rect)
        pygame.display.flip()

pygame.quit()
