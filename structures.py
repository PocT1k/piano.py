import pygame  # Библиотека игры
import functions

Images_dic = \
    {
        "int_musclub_day": 0,
        "int_lines": 0,
        "keys": 0
    }  # Словарь задних изображений

notes_dic = \
    {
        "tab": "la_diez_-1",
        "shift": "si_-1",
        "A": "do_0",
        "W": "do_diez_0",
        "S": "re_0",
        "E": "re_diez_0",
        "D": "mi_0",
        "F": "fa_0",
        "T": "fa_diez_0",
        "G": "sol_0",
        "Y": "sol_diez_0",
        "H": "la_0",
        "U": "la_diez_0",
        "J": "si_0",
        "K": "do_1",
        "O": "do_diez_1",
        "L": "re_1",
        "P": "re_diez_1",
        ";": "mi_1",
        "\'": "fa_1",
        "{": "fa_diez_1",
        "back_sl": "sol_1",
        "}": "sol_diez_1"
    }  # Словарь всех клавишклавиш

un_notes_dic = {}  # Обратный словарь клавиш
for f_notes in notes_dic:
    un_notes_dic[notes_dic[f_notes]] = f_notes

w_notes_dic = \
    {
        "tab": 0,
        "shift": 2,
        "A": 150,
        "W": 241,
        "S": 297,
        "E": 415,
        "D": 445,
        "F": 593,
        "T": 675,
        "G": 740,
        "Y": 845,
        "H": 888,
        "U": 1016,
        "J": 1036,
        "K": 1184,
        "O": 1275,
        "L": 1331,
        "P": 1449,
        ";": 1479,
        "\'": 1627,
        "{": 1708,
        "back_sl": 1774,
        "}": 1880
    }  # Словарь отступа ширины клавиш

zna1_h_dic = 971
zna2_h_dic = 1080
h_notes_dic = \
    {
        "tab": zna1_h_dic,
        "shift": zna2_h_dic,
        "A": zna2_h_dic,
        "W": zna1_h_dic,
        "S": zna2_h_dic,
        "E": zna1_h_dic,
        "D": zna2_h_dic,
        "F": zna2_h_dic,
        "T": zna1_h_dic,
        "G": zna2_h_dic,
        "Y": zna1_h_dic,
        "H": zna2_h_dic,
        "U": zna1_h_dic,
        "J": zna2_h_dic,
        "K": zna2_h_dic,
        "O": zna1_h_dic,
        "L": zna2_h_dic,
        "P": zna1_h_dic,
        ";": zna2_h_dic,
        "\'": zna2_h_dic,
        "{": zna1_h_dic,
        "back_sl": zna2_h_dic,
        "}": zna1_h_dic
    }  # Словарь низа клавиш


class BGs_cl():  # Класс БГ

    def __init__(self, screen, pic):  # Инициализация
        self.screen = screen  # Получение экрана
        self.image = pygame.image.load("images/" + pic + ".png").convert_alpha()  # Загрузка изображения
        self.width_r, self.height_r = functions.size_screen()  # Запись размера экрана
        if pic == "int_musclub_day":
            if self.width_r > self.height_r:  # Масштабирование без искажения
                self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.height_r,
                                                                 self.image.get_height() // self.height_r))  # Масштабирование под заданное окно
            elif self.width_r < self.height_r:
                self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.width_r,
                                                                 self.image.get_height() // self.width_r))  # Масштабирование под заданное окно
            else:
                self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.width_r,
                                                                 self.image.get_height() // self.height_r))  # Масштабирование под заданное окно
        else:  # Масштабирование просто
            self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.width_r,
                                                             self.image.get_height() // self.height_r))  # Масштабирование под заданное окно
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # Полученеи объекта экрана
        self.rect.centerx = self.screen_rect.centerx  # Координаты по центру X
        self.rect.bottom = self.screen_rect.bottom  # Координаты по дну Y

    def output(self):  # Отрисовка
        self.screen.blit(self.image, self.rect)


class Notes_cl():  # Класс всех клавиш

    def __init__(self, screen, pic, w_notes_dic, h_notes_dic):  # Инициализация
        self.screen = screen  # Получение экрана
        self.image = pygame.image.load("images/notes/" + pic + ".png").convert_alpha()  # Загрузка изображения
        self.width_r, self.height_r = functions.size_screen()  # Запись размера экрана
        self.image = pygame.transform.scale(self.image, (round(self.image.get_width() // self.width_r), round(
            self.image.get_height() // self.height_r)))  # Масштабирование под заданное окно
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # Полученеи объекта экрана
        self.rect.left = w_notes_dic[pic] // self.width_r  # Координаты X
        self.rect.bottom = h_notes_dic[pic] // self.height_r  # Координаты Y
        self.draw = False

    def output(self):  # Отрисовка
        if self.draw == True:
            self.screen.blit(self.image, self.rect)


# top: int
# left: int
# bottom: int
# right: int
