import datetime
import pygame


def fps_counter(FPS, date_time_old):  # Функция подсчёта ФПС
    FPS_was = -1
    date_time_now = datetime.datetime.now().timetuple().tm_sec
    if FPS == -1:
        pass
    else:
        # print(date_time_now, date_time_old)
        if date_time_now != date_time_old:
            FPS_was = FPS
            FPS = 0
    FPS = FPS + 1
    return FPS, date_time_now, FPS_was


def size_screen():  # Функция полученяия размеров экрана системы
    infos = pygame.display.Info()
    return 1920 / infos.current_w, 1080 / infos.current_h


def stop_or_run(time_old):  # Функция определения можно ли остановиться
    time_now = pygame.time.get_ticks()
    if time_now - time_old > 10:
        return 0, time_now
    return 1, time_now


def dict_del():
    pass


def dict_add():
    pass
