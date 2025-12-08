"""import pygame
import pytmx
import pyscroll

from screen import Screen


class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.switch_map("map0")

    def switch_map(self, map: str):
        self.tmx_data = pytmx.load_pygame(f"../../assets/map/{map}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

    def update(self):
        self.group.draw(self.screen.get_display())
        """

import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

tmx_data = load_pygame("/Users/gml/Desktop/Projet code jeu python/images/Map/assets/map_projet.tmx")

surfaceW = 800
surfaceH = 500
speed = 2

surface = pygame.display.set_mode((surfaceW, surfaceH))

blue = (113, 177, 227)
white = (255, 255, 255)
PersoW = 50
PersoH = 66

img = pygame.image.load("Personnage-vendeur.png")

def dessiner_map(surface, tmx_data):
    # Dessine toutes les couches de tuiles visibles
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
    x = 150
    y = 200

    game_over = False
    clock = pygame.time.Clock()
    speed = 2

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_s]:
            y += speed


        dessiner_map(surface, tmx_data)


        perso(x, y, img)

        pygame.display.update()
        clock.tick(60)

principale()

pygame.quit()
quit()
