import pygame as pg

pg.init()

main = pg.display.set_mode([840, 480])

pg.display.set_caption("Meu primeiro script com Pygame")

def draw():
    main.fill([255, 255, 255])
    
gameloop = True

while gameloop:
    # setando as binds
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameloop = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                print("Você apertou a tecla W")
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                print("Você soltou o W")
            
    # preenche a tela com uma cor (em rgb)
    draw()
    
    # atualiza a tela
    pg.display.update()