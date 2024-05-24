import pygame, sys
from button import Button


pygame.init()

Tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

Fundo = pygame.image.load("assets/Fundo.jpg")
Fundo2 = pygame.image.load("assets/Fundo2.jpeg")


def get_font(size):
    return pygame.font.Font("assets/Augusta.ttf", size)
def get_font2(size):
    return pygame.font.Font("assets/Morris.ttf", size)
def get_font3(size):
    return pygame.font.Font("assets/Titania-Regular.ttf", size)

def play():

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        Tela.fill("black")

        play_text = get_font(43).render("Essa é a tela do JOGO.", True, "white")
        play_rect = play_text.get_rect(center=(640, 260))
        Tela.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(640, 660),
                            text_input="Ok", font=get_font2(75), base_color="white", hovering_color="Green")
        

        play_back.changeColor(play_mouse_pos)
        play_back.update(Tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    select()
                    main_menu()

        pygame.display.update()



def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()
        Tela.fill("white")

        options_text = get_font(45).render("Essa é a Tela de Opções", True, "Black")
        options_rect = options_text.get_rect(center=(640, 260))
        Tela.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(640, 660),
                                text_input="Back", font=get_font2(75), base_color="Black", hovering_color="Green")

        options_back.changeColor(options_mouse_pos)
        options_back.update(Tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    
                    main_menu()

        pygame.display.update()

def select():
    select_images = ["assets/hibrid2.png", "assets/meninododoi.png", "assets/assassino.png"]
    select_buttons = []

    for i, image in enumerate(select_images):
        select_buttons.append(Button(image=pygame.image.load(image), pos=(320 + i * 320, 360),
                                     text_input="", font=get_font(75), base_color="white", hovering_color="Green"))
    

    while True:
        select_mouse_pos = pygame.mouse.get_pos()
        Tela.blit(Fundo, (0, 0))
        

        select_text = get_font(25).render("Escolha seu personagem.", True, "Gray")
        select_rect = select_text.get_rect(center=(640, 54))
        Tela.blit(select_text, select_rect)

        select_back = Button(image=None, pos=(640, 675),
                             text_input="Voltar", font=get_font2(25), base_color="white", hovering_color="Green")

        select_back.changeColor(select_mouse_pos)
        select_back.update(Tela)

        for button in select_buttons:
            button.changeColor(select_mouse_pos)
            button.update(Tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_back.checkForInput(select_mouse_pos):
                    main_menu()
                for i, button in enumerate(select_buttons):
                    if button.checkForInput(select_mouse_pos):
                        selected_character = select_images[i]
                        play()
                        main_menu()

        pygame.display.update()

def main_menu():
    while True:
        Tela.blit(Fundo, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(180).render("Etherya", True, "#ffffff")
        MENU_RECT = menu_text.get_rect(center=(640, 80))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(72, 484),
                             text_input="JOGAR", font=get_font3(34), base_color="#d7fcd4", hovering_color="White")
        select_button = Button(image=pygame.image.load("assets/Selecionar Rect.png"), pos=(120, 520),
                               text_input="PERSONAGENS", font=get_font3(29), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(71, 555),
                                text_input="OPÇÕES", font=get_font3(29), base_color="#d7fcd4", hovering_color="White")
        
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(52, 638),
                             text_input="SAIR", font=get_font3(29), base_color="#d7fcd4", hovering_color="White")

        Tela.blit(menu_text, MENU_RECT)

        for button in [play_button, options_button, select_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(Tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if select_button.checkForInput(menu_mouse_pos):
                    select()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()