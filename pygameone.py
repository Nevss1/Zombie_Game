import pygame
pygame.init()

janela = pygame.display.set_mode((1024, 626)) # screen_display
pygame.display.set_caption("Shooter Mouse")
fundo = pygame.image.load("background.png")

imagem_cursor = pygame.image.load("aim_cursor.png")
imagem_cursor = pygame.transform.smoothscale(imagem_cursor, (256, 256)) # define o tamanho do cursor
pygame.mouse.set_visible(False)

pygame.mixer.music.load("Loonboon.mp3") # background music
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(2)


zombie1 = pygame.image.load("zombie1.png")
z1_x, z1_y = zombie1.get_size()
zombie1 = pygame.transform.smoothscale(zombie1, (z1_x*0.3, z1_y*0.3)) #zumbi
zombie1 = pygame.transform.flip(zombie1, True, False) # gira em torno do eixo X
posicao_zombie1 = [1000, 300] #define por onde o zombie1 vai andar horizontalmente

game = True
while game:
    janela.blit(fundo, (0, 0))  # background
    x, y = pygame.mouse.get_pos()  # pega a posição
    pos_cursor = [x-130, y-130]  # centralize o cursor
    janela.blit(imagem_cursor, pos_cursor)  # atualiza a pos do novo cursor

    for event in pygame.event.get():
        imgzombie1_rect = zombie1.get_rect(topleft=posicao_zombie1)  # pega o retângulo, a superficie onde a imagem está
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(x, y)
            pos_click = event.pos
            if imgzombie1_rect.collidepoint(pos_click): # se o mouse click clicar no espaço onde a imagem está
                zombie1.
    if not posicao_zombie1[0] < 206:
        posicao_zombie1[0] -= 0.1 # velocidade
    else:
        print("zumbi chegou")

    janela.blit(zombie1, posicao_zombie1)
    pygame.display.update()

pygame.quit()
