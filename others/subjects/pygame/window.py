import pygame as pg

# inicia o pygame
pg.init()

# seta as dimensões da janela e retorna a instância da janela
main = pg.display.set_mode([840, 480])

# seta o título da janela
pg.display.set_caption("Meu primeiro script com Pygame")

# função para desenhar na tela
def draw():
    main.fill([255, 255, 255])
    
# gameloop
# variavel que deixa o script rodando
gameloop = True

while gameloop:
    # preenche a tela com uma cor (em rgb)
    draw()
    
    # atualiza a tela
    pg.display.update()