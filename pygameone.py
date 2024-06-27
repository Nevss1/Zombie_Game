import pygame
import random

pygame.init()

FPS = 20
clock = pygame.time.Clock()

janela = pygame.display.set_mode((1024, 626)) # screen_display
pygame.display.set_caption("Shooter Mouse")
fundo = pygame.image.load("background.png")

imagem_cursor = pygame.image.load("aim_cursor.png")
imagem_cursor = pygame.transform.smoothscale(imagem_cursor, (256, 256)) # define o tamanho do cursor
pygame.mouse.set_visible(False)

pygame.mixer.music.load("Loonboon.mp3") # background music
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(2)
som_tiro = pygame.mixer.Sound("shoot.mp3")

zombie1 = pygame.image.load("zombie1.png")
z1_x, z1_y = zombie1.get_size() # ajuste do tamanho do zumbi
zombie1 = pygame.transform.smoothscale(zombie1, (z1_x*0.3, z1_y*0.3)) #zumbi1
zombie1 = pygame.transform.flip(zombie1, True, False) # gira em torno do eixo X
posicao_zombie1 = [1000, 300] #define por onde o zombie1 vai andar horizontalmente


class Zombie:
    def __init__(self, x, y, velocidade):
        self.imagem = zombie1
        self.rect = self.imagem.get_rect(topright=(x, y))
        self.velocidade = velocidade

    def update(self): # andar
        self.rect.x -= self.velocidade

    def draw(self, surface):
        surface.blit(self.imagem, self.rect)


def adicionarzumbi(pos, velocidade):
    return Zombie(905, pos, velocidade)


inicial_pos = [15, 100, 200]  # posições Y iniciais dos zumbis
zumbis_normais = []

for i in range(3):
    zumbis_normais.append(adicionarzumbi(inicial_pos[i], 1))

game = True
while game:
    clock.tick(30)
    janela.blit(fundo, (0, 0))  # background
    x, y = pygame.mouse.get_pos()
    pos_cursor = [x-130, y-130]  # centraliza
    janela.blit(imagem_cursor, pos_cursor)  # atualiza o novo cursor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            som_tiro.play()
            print(x, y)
            pos_click = event.pos
            for zumbi in zumbis_normais:
                print(zumbi.rect.x)
                area_zumbi = zumbi.imagem.get_rect(topleft=[zumbi.rect.x, zumbi.rect.y])  # verifica se o mouse clicou na área de algum zumbi dentro do loop
                if area_zumbi.collidepoint(pos_click):
                    zumbis_normais.remove(zumbi)

            # if imgzombie1_rect.collidepoint(pos_click): # se o mouse click clicar no espaço onde a imagem está
                # zombie1_view = False

    for zumbi in zumbis_normais:
        zumbi.draw(janela)  # movimenta o zumbi
        zumbi.update()  #

    pygame.display.flip()  # update tela

pygame.quit()
