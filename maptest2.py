import pyscroll
import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

surfaceL = 2000
surfaceH = 1920
"""
tailleEcran=(1080, 720)
"""
speed = 2.5


surface = pygame.display.set_mode((surfaceL, surfaceH))

tmx_data = load_pygame("/Users/gml/Desktop/Projet Trophé NSI#2/Images/Map/map_projet_python.tmx")

blue = (113, 177, 227)
white = (255, 255, 255)
PersoW = 50
PersoH = 66

img = pygame.image.load("Personnage-vendeur.png")
img_rect = img.get_rect()


#Chatgpt ou vidéo jsplus
def Map(surface, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tmx_data.get_tile_image_by_gid(gid)
                if tile_image:
                    surface.blit(
                        tile_image,
                        (x * tmx_data.tilewidth, y * tmx_data.tileheight)
                    )


def perso(x, y, image):
    surface.blit(image, (x, y))

def principale():

    x = (surfaceL - img_rect.width) // 2
    y = (surfaceH - img_rect.height) // 2

    game_over = False
    clock = pygame.time.Clock()
    speed = 2
#Pour quitter le jeu #1
    while not game_over:#1
        for event in pygame.event.get():#1
            if event.type == pygame.QUIT:#1
                game_over = True#1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_q]:
            x -= speed
        if keys[pygame.K_d] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_w] or keys[pygame.K_a]:
            y -= speed
        if keys[pygame.K_s]:
            y += speed


        Map(surface, tmx_data)
        perso(x, y, img)
        self.group.center(self.player.rect)

        pygame.display.update()
        clock.tick(60)

principale()
pygame.quit()
quit()
