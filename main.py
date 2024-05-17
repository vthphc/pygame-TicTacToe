import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TicTacToe")

line_width = 12
markers = []
clicked = False
pos = []
player = 1
game_over = False
winner = 0


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, 200 * x), (600, 200 * x), line_width)
        pygame.draw.line(screen, grid, (200 * x, 0), (200 * x, 600), line_width)


def check_winner():
    global game_over, winner
    for i in range(3):
        if markers[i][0] == markers[i][1] == markers[i][2] != 0:
            winner = markers[i][0]
            game_over = True
        if markers[0][i] == markers[1][i] == markers[2][i] != 0:
            winner = markers[0][i]
            game_over = True
    if markers[0][0] == markers[1][1] == markers[2][2] != 0:
        winner = markers[0][0]
        game_over = True
    if markers[0][2] == markers[1][1] == markers[2][0] != 0:
        winner = markers[0][2]
        game_over = True

    if all([all(row) for row in markers]) and winner == 0:
        game_over = True
        winner = "Tie"


def draw_winner(winner):
    if winner != "Tie":
        win_text = "Player " + str(winner) + " wins!"
    else:
        win_text = "It's a tie!"

    font = pygame.font.Font(None, 48)
    text = font.render(win_text, True, (253, 254, 254))
    text_rect = text.get_rect(center=(300, 300))
    pygame.draw.rect(screen, (46, 134, 193), (175, 225, 250, 150), 0, 10)
    screen.blit(text, text_rect)


for x in range(3):
    row = [0] * 3
    markers.append(row)

run = True
while run:
    draw_grid()

    for y in range(3):
        for x in range(3):
            if markers[y][x] == 1:
                pygame.draw.line(screen, (231, 76, 60), (x * 200 + 50, y * 200 + 50), (x * 200 + 150, y * 200 + 150), line_width)
                pygame.draw.line(screen, (231, 76, 60), (x * 200 + 150, y * 200 + 50), (x * 200 + 50, y * 200 + 150), line_width)
            elif markers[y][x] == -1:
                pygame.draw.circle(screen, (46, 204, 113), (x * 200 + 100, y * 200 + 100), 50, line_width)

    check_winner()
    if game_over:
        draw_winner(winner)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0] // 200
            cell_y = pos[1] // 200
            if markers[cell_y][cell_x] == 0:
                markers[cell_y][cell_x] = player
                player *= -1

    pygame.display.update()

pygame.quit()
