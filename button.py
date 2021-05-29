import pygame.font

class Button():
    __button_space = 0
    def __init__(self, ai_game, msg):   #screen był też atrybut
        """Inicialisation button's atributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Define dimensions and atributes of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Creating button and centerering button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center                                          #Aby wycentrować przypisujemy środkowi przycisku środek nasszego ekranu
        self.rect.y += self.__button_space

        Button.__button_space += self.rect.height + 30

        #Message prompt by the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Placing prompts in generated image and centring text on button"""
        #Dzięki wywołanie font.render() zmiena tekst z msg na obraz
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)    #Bolowska wartość stwierdza (antyaliasing, wygładzenie krawędzi czcionki)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Displaying empty button, then the message on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)                               #Blit wyświetla obraz tekstu na ekranie
