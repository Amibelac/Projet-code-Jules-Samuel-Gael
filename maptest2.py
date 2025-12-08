import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

# Taille de la fenêtre
surfaceW = 800
surfaceH = 500

# Plein écran (si tu veux garder fenêtré, enlève pygame.FULLSCREEN)
surface = pygame.display.set_mode((surfaceW, surfaceH), pygame.FULLSCREEN)

# Chargement de la map Tiled
tmx_data = load_pygame("/Users/gml/Desktop/Projet code jeu python/images/Map/assets/map_projet.tmx")

# Infos sur la map (en cases → puis en pixels)
tile_w = tmx_data.tilewidth
tile_h = tmx_data.tileheight
map_w_px = tmx_data.width * tile_w
map_h_px = tmx_data.height * tile_h

blue = (113, 177, 227)
white = (255, 255, 255)
PersoW = 50
PersoH = 66

img = pygame.image.load("Personnage-vendeur.png")

def dessiner_map(surface, tmx_data, camera_x, camera_y):
    """Dessine les tuiles en tenant compte de la caméra (décalage)."""
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tmx_data.get_tile_image_by_gid(gid)
                if tile_image:
                    # position de la tuile dans la map (en pixels)
                    world_x = x * tmx_data.tilewidth
                    world_y = y * tmx_data.tileheight

                    # position sur l'écran = position monde - caméra
                    screen_x = world_x - camera_x
                    screen_y = world_y - camera_y

                    surface.blit(tile_image, (screen_x, screen_y))

def perso_ecran(surface, image):
    """Dessine le perso au centre de l'écran (la caméra suit le perso)."""
    screen_x = surfaceW // 2 - PersoW // 2
    screen_y = surfaceH // 2 - PersoH // 2
    surface.blit(image, (screen_x, screen_y))

def principale():
    # 🔹 Position du perso AU CENTRE DE LA MAP (en coordonnées monde)
    player_x = map_w_px // 2
    player_y = map_h_px // 2

    speed = 2
    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()

        # Déplacement du perso dans LA MAP (coordonnées monde)
        # ici WASD, tu peux remettre ZQSD si tu veux
        if keys[pygame.K_a]:     # gauche
            player_x -= speed
        if keys[pygame.K_d]:     # droite
            player_x += speed
        if keys[pygame.K_w]:     # haut
            player_y -= speed
        if keys[pygame.K_s]:     # bas
            player_y += speed

        # 🔹 Caméra centrée sur le perso
        camera_x = player_x - surfaceW // 2
        camera_y = player_y - surfaceH // 2

        # (optionnel) remplir le fond si map plus petite
        surface.fill(blue)

        # 🔹 On dessine la map en fonction de la caméra
        dessiner_map(surface, tmx_data, camera_x, camera_y)

        # 🔹 On dessine le perso AU CENTRE de l'écran
        perso_ecran(surface, img)

        pygame.display.update()
        clock.tick(60)

principale()

pygame.quit()
quit()
