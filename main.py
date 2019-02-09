import pygame
import board

running = True
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.init()
board = board.Board(10, 10, 50)
# board.generate_random(3)

while running:
    screen.fill((0, 0, 0))
    board_surface = board.render()
    screen.blit(board_surface, (50, 50))
    pygame.display.flip()

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        board_rect = board_surface.get_rect().move(50,50)
        if board_rect.collidepoint(event.pos):
            board_pos = event.pos[0] - 50, event.pos[1] - 50
            board.click(board_pos)
    pygame.display.flip()

pygame.quit()
