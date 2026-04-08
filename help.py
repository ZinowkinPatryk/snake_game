import pygame

pygame.init()
screen = pygame.display.set_mode((720, 720))

# Inicjalizacja muzyki
pygame.mixer.init()
pygame.mixer.music.load("sound/background_music.mp3")  # Zmień na swoją muzykę
pygame.mixer.music.play(-1)  # Odtwarzaj w tle

# Zmienne globalne
mute_counter = 0

def pause():
    global mute_counter
    paused = True

    # Wczytanie ikon
    silenced = pygame.image.load("silenced.png")
    silenced = pygame.transform.scale(silenced, (40, 40))
    mute = pygame.image.load("MUTE.png")
    mute = pygame.transform.scale(mute, (45, 45))

    # Definicja przycisków
    button_sound = pygame.Rect(10, 665, 50, 50)
    font = pygame.font.SysFont('Arial', 30)
    text1 = font.render("New game", True, (0, 0, 0))
    text2 = font.render("Quit", True, (0, 0, 0))
    button_width, button_height = 150, 50
    button1_rect = pygame.Rect(720 // 2 - button_width - 10, 250, button_width, button_height)
    button2_rect = pygame.Rect(720 // 2 + 10, 250, button_width, button_height)

    while paused:
        screen.fill((255, 255, 255))  # Czyszczenie ekranu

        pygame.draw.rect(screen, (200, 200, 200), button_sound, border_radius=5)

        if mute_counter == 0:
            screen.blit(silenced, (13, 668))
        else:
            screen.blit(mute, (13, 668))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(event.pos):  # "New Game"
                    paused = False
                    screen.fill((0, 0, 0))  # Wyczyść ekran
                    pygame.display.flip()  # Odśwież ekran
                    return
                elif button2_rect.collidepoint(event.pos):  # "Quit"
                    pygame.quit()
                    quit()
                elif button_sound.collidepoint(event.pos):  # Mute/unmute
                    if mute_counter == 0:
                        pygame.mixer.music.pause()
                        mute_counter = 1
                    else:
                        pygame.mixer.music.unpause()
                        mute_counter = 0

        # Rysowanie przycisków
        pygame.draw.rect(screen, (200, 200, 200), button1_rect, border_radius=10)
        pygame.draw.rect(screen, (200, 200, 200), button2_rect, border_radius=10)
        screen.blit(text1, (button1_rect.x + 2, button1_rect.y + 10))
        screen.blit(text2, (button2_rect.x + 40, button2_rect.y + 10))

        pygame.display.flip()

pause()  # Wywołanie menu pauzy na start