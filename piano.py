import pygame  # Библиотека игры
import pygame.midi  # Библиотека звуков
# import time
from structures import BGs_cl  # Структура БГ
from structures import Notes_cl  # Структура клавиш
from structures import Images_dic  # Словарь задних изображений
from structures import notes_dic  # Словарь всех клавишклавиш
from structures import w_notes_dic  # Словарь отступа ширины клавиш
from structures import h_notes_dic  # Словарь низа клавиш
import controls  # Файл py
import functions  # Файл py


def run():  # Функция запуска
    pygame.init()  # Инициализация игры
    pygame.midi.init()  # Инициализация звуков
    turntable = pygame.midi.Output(0)  # Выбор источника звука
    turntable.set_instrument(2)  # Выбор инструмента #2
    #screen = pygame.display.set_mode((720, 720)) # Создание графической области #HD #1280 #720
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Создание графической области на весь экран
    pygame.display.set_caption("Пианино")  # Приписывание названия
    bg_color = (200, 230, 255)  # Выбор цвета заднего фона
    tone, volume = 46, 127  # Тональность и звук #46 #127

    for f_BGs in Images_dic:  # Загрузка задних изображений
        Images_dic[f_BGs] = BGs_cl(screen, str(f_BGs))  # Загрузка поверхностей изображений БГ с помощью словаря
    for f_notes in notes_dic:  # Загрузка всех клавиш
        notes_dic[f_notes] = Notes_cl(screen, str(f_notes), w_notes_dic, h_notes_dic)  # Загрузка поверхностей изображений нот с помощью словаря

    FPS = date_time_old = -1  # Переменные для вызова функции подсчёта ФПС
    SOR, SOR_time = 0, 0  # Переменная для вызова функции определения можно ли приостановиться

    while True:  # Бесконечный цикл работы игры
        controls.events_run(notes_dic, turntable, tone, volume)  # Вызов обработки событий
        screen.fill(bg_color)  # Заливка экрана

        for f_BGs in Images_dic:
            Images_dic[f_BGs].output()  # Отрисовка задних изображений
        for f_notes in notes_dic:
            notes_dic[f_notes].output()  # Отрисовка клавиш

        FPS, date_time_old, FPS_was = functions.fps_counter(FPS, date_time_old)  # Вызов функции подсчёта ФПС
        if FPS_was != -1:  # Вывод значения отрисованных кадров за прощедшую секунду
            # print(FPS_was)
            pass

        SOR, SOR_time = functions.stop_or_run(SOR_time)  # Функция определения можно ли остановиться
        if SOR == 1:
            pygame.time.delay(10)  # Проверка каждые 10 мс

        pygame.display.flip()  # Прорисовка кадра


if __name__ == "__main__":  # Запуск только при старте
    run()  # Вызов функции запуска


#pyinstaller piano.py functions.py controls.py structures.py -n Пианино -F --noconsole --icon=Пианино.ico
#pyinstaller piano.py functions.py controls.py structures.py -n Пианино -F --noconsole --icon=Пианино.ico images\int_lines.png images\int_musclub_day.png images\keys.png images\notes\'.png images\notes\;.png images\notes\{.png images\notes\}.png images\notes\A.png images\notes\back_sl.png images\notes\D.png images\notes\E.png images\notes\F.png images\notes\G.png images\notes\H.png images\notes\J.png images\notes\K.png images\notes\L.png images\notes\O.png images\notes\P.png images\notes\S.png images\notes\shift.png images\notes\T.png images\notes\tab.png images\notes\U.png images\notes\W.png images\notes\Y.png
