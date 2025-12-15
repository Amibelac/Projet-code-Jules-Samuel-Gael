import pygame
import sys
import subprocess

pygame.init()
pygame.mixer.init()

LARGEUR, HAUTEUR = 1024, 1024
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu")

background = pygame.image.load("/Users/gml/Desktop/Projet Trophé NSI#2/Images/Launcher.png").convert()
background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))

pygame.mixer.music.load("/Users/gml/Desktop/Projet Trophé NSI#2/musique/launcher.mp3")
pygame.mixer.music.play(-1)

BLANC = (255, 255, 255)
TRANSLUCSCENT_BLUE = (0, 200, 180, 200)
HOVER_BLUE = (0, 140, 255, 220)
SHADOW = (0, 0, 0)

FONT_TITLE = pygame.font.Font(None, 72)
FONT_BUTTON = pygame.font.Font(None, 36)


class Button:
    def __init__(self, text, center_y, action):
        self.text = text
        self.action = action
        self.width, self.height = 320, 70
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (LARGEUR // 2, center_y)

    def draw(self, win, mouse_pos):
        is_hover = self.rect.collidepoint(mouse_pos)
        color = HOVER_BLUE if is_hover else TRANSLUCSCENT_BLUE

        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, (0, 0, self.width, self.height), border_radius=16)
        win.blit(button_surface, self.rect)

        shadow_surf = FONT_BUTTON.render(self.text, True, SHADOW)
        text_surf = FONT_BUTTON.render(self.text, True, BLANC)

        text_rect = text_surf.get_rect(center=self.rect.center)
        win.blit(shadow_surf, (text_rect.x + 2, text_rect.y + 2))
        win.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]


buttons = [
    Button("Nouvelle Partie", 320, "new"),
    Button("Charger une partie", 400, "load"),
    Button("Options", 480, "option"),
    Button("Quitter", 560, "quit"),
]

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ecran.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    title = FONT_TITLE.render("Mon jeu", True, BLANC)
    shadow = FONT_TITLE.render("Mon jeu", True, SHADOW)
    ecran.blit(shadow, (LARGEUR // 2 - title.get_width() // 2 + 3, 103))
    ecran.blit(title, (LARGEUR // 2 - title.get_width() // 2, 100))

    for btn in buttons:
        btn.draw(ecran, mouse_pos)
        if btn.is_clicked(mouse_pos, mouse_pressed):
            pygame.time.delay(200)

            if btn.action == "new":
                pygame.mixer.music.stop()
                pygame.quit()
                subprocess.run(["python3", "map.py"])
                sys.exit()

            elif btn.action == "load":
                print("Charger partie")

            elif btn.action == "option":
                print("Options")

            elif btn.action == "quit":
                running = False

    pygame.display.flip()

pygame.quit()
print("Fermeture du jeu")
