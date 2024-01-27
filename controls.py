import pygame  # Библиотека игры
import sys  # Библеотека работы с системой


def events_run(KeyssNotes_dic, turntable, tone, volume):  # Обработка событий
    for event in pygame.event.get():  # Перебор всех событий
        if event.type == pygame.QUIT:  # Если событие выход
            sys.exit()  # Выход
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()  # Выход
            if event.key == pygame.K_TAB:
                turntable.note_on(tone, volume)
                KeyssNotes_dic["tab"].draw = True
            if (event.key == pygame.K_LSHIFT) or (event.key == pygame.K_CAPSLOCK):
                turntable.note_on(tone + 1, volume)
                KeyssNotes_dic["shift"].draw = True
            if event.key == pygame.K_a:
                turntable.note_on(tone + 2, volume)
                KeyssNotes_dic["A"].draw = True
            if event.key == pygame.K_w:
                turntable.note_on(tone + 3, volume)
                KeyssNotes_dic["W"].draw = True
            if event.key == pygame.K_s:
                turntable.note_on(tone + 4, volume)
                KeyssNotes_dic["S"].draw = True
            if event.key == pygame.K_e:
                turntable.note_on(tone + 5, volume)
                KeyssNotes_dic["E"].draw = True
            if event.key == pygame.K_d:
                turntable.note_on(tone + 6, volume)
                KeyssNotes_dic["D"].draw = True
            if event.key == pygame.K_f:
                turntable.note_on(tone + 7, volume)
                KeyssNotes_dic["F"].draw = True
            if event.key == pygame.K_t:
                turntable.note_on(tone + 8, volume)
                KeyssNotes_dic["T"].draw = True
            if event.key == pygame.K_g:
                turntable.note_on(tone + 9, volume)
                KeyssNotes_dic["G"].draw = True
            if event.key == pygame.K_y:
                turntable.note_on(tone + 10, volume)
                KeyssNotes_dic["Y"].draw = True
            if event.key == pygame.K_h:
                turntable.note_on(tone + 11, volume)
                KeyssNotes_dic["H"].draw = True
            if event.key == pygame.K_u:
                turntable.note_on(tone + 12, volume)
                KeyssNotes_dic["U"].draw = True
            if event.key == pygame.K_j:
                turntable.note_on(tone + 13, volume)
                KeyssNotes_dic["J"].draw = True
            if event.key == pygame.K_k:
                turntable.note_on(tone + 14, volume)
                KeyssNotes_dic["K"].draw = True
            if event.key == pygame.K_o:
                turntable.note_on(tone + 15, volume)
                KeyssNotes_dic["O"].draw = True
            if event.key == pygame.K_l:
                turntable.note_on(tone + 16, volume)
                KeyssNotes_dic["L"].draw = True
            if event.key == pygame.K_p:
                turntable.note_on(tone + 17, volume)
                KeyssNotes_dic["P"].draw = True
            if (event.key == pygame.K_SEMICOLON) or (event.key == ord('ж')):
                turntable.note_on(tone + 18, volume)
                KeyssNotes_dic[";"].draw = True
            if (event.key == pygame.K_QUOTE) or (event.key == ord('э')):
                turntable.note_on(tone + 19, volume)
                KeyssNotes_dic["\'"].draw = True
            if (event.key == pygame.K_LEFTBRACKET) or (event.key == ord('х')):
                turntable.note_on(tone + 20, volume)
                KeyssNotes_dic["{"].draw = True
            if event.key == pygame.K_BACKSLASH:
                turntable.note_on(tone + 21, volume)
                KeyssNotes_dic["back_sl"].draw = True
            if (event.key == pygame.K_RIGHTBRACKET) or (event.key == ord('ъ')):
                turntable.note_on(tone + 22, volume)
                KeyssNotes_dic["}"].draw = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                turntable.note_off(tone, volume)
                KeyssNotes_dic["tab"].draw = False
            if (event.key == pygame.K_LSHIFT) or (event.key == pygame.K_CAPSLOCK):
                turntable.note_off(tone + 1, volume)
                KeyssNotes_dic["shift"].draw = False
            if event.key == pygame.K_a:
                turntable.note_off(tone + 2, volume)
                KeyssNotes_dic["A"].draw = False
            if event.key == pygame.K_w:
                turntable.note_off(tone + 3, volume)
                KeyssNotes_dic["W"].draw = False
            if event.key == pygame.K_s:
                turntable.note_off(tone + 4, volume)
                KeyssNotes_dic["S"].draw = False
            if event.key == pygame.K_e:
                turntable.note_off(tone + 5, volume)
                KeyssNotes_dic["E"].draw = False
            if event.key == pygame.K_d:
                turntable.note_off(tone + 6, volume)
                KeyssNotes_dic["D"].draw = False
            if event.key == pygame.K_f:
                turntable.note_off(tone + 7, volume)
                KeyssNotes_dic["F"].draw = False
            if event.key == pygame.K_t:
                turntable.note_off(tone + 8, volume)
                KeyssNotes_dic["T"].draw = False
            if event.key == pygame.K_g:
                turntable.note_off(tone + 9, volume)
                KeyssNotes_dic["G"].draw = False
            if event.key == pygame.K_y:
                turntable.note_off(tone + 10, volume)
                KeyssNotes_dic["Y"].draw = False
            if event.key == pygame.K_h:
                turntable.note_off(tone + 11, volume)
                KeyssNotes_dic["H"].draw = False
            if event.key == pygame.K_u:
                turntable.note_off(tone + 12, volume)
                KeyssNotes_dic["U"].draw = False
            if event.key == pygame.K_j:
                turntable.note_off(tone + 13, volume)
                KeyssNotes_dic["J"].draw = False
            if event.key == pygame.K_k:
                turntable.note_off(tone + 14, volume)
                KeyssNotes_dic["K"].draw = False
            if event.key == pygame.K_o:
                turntable.note_off(tone + 15, volume)
                KeyssNotes_dic["O"].draw = False
            if event.key == pygame.K_l:
                turntable.note_off(tone + 16, volume)
                KeyssNotes_dic["L"].draw = False
            if event.key == pygame.K_p:
                turntable.note_off(tone + 17, volume)
                KeyssNotes_dic["P"].draw = False
            if (event.key == pygame.K_SEMICOLON) or (event.key == ord('ж')):
                turntable.note_off(tone + 18, volume)
                KeyssNotes_dic[";"].draw = False
            if (event.key == pygame.K_QUOTE) or (event.key == ord('э')):
                turntable.note_off(tone + 19, volume)
                KeyssNotes_dic["\'"].draw = False
            if (event.key == pygame.K_LEFTBRACKET) or (event.key == ord('х')):
                turntable.note_off(tone + 20, volume)
                KeyssNotes_dic["{"].draw = False
            if event.key == pygame.K_BACKSLASH:
                turntable.note_off(tone + 21, volume)
                KeyssNotes_dic["back_sl"].draw = False
            if (event.key == pygame.K_RIGHTBRACKET) or (event.key == ord('ъ')):
                turntable.note_off(tone + 22, volume)
                KeyssNotes_dic["}"].draw = False


def events_black(KeyssNotes_dic, turntable, tone, volume):  # Обработка событий для чёрных клавиш
    for event in pygame.event.get():  # Перебор всех событий
        # print(event.key)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                turntable.note_on(tone, volume)
                KeyssNotes_dic["tab"].draw = True
            if event.key == pygame.K_w:
                turntable.note_on(tone + 3, volume)
                KeyssNotes_dic["W"].draw = True
            if event.key == pygame.K_e:
                turntable.note_on(tone + 5, volume)
                KeyssNotes_dic["E"].draw = True
            if event.key == pygame.K_t:
                turntable.note_on(tone + 8, volume)
                KeyssNotes_dic["T"].draw = True
            if event.key == pygame.K_y:
                turntable.note_on(tone + 10, volume)
                KeyssNotes_dic["Y"].draw = True
            if event.key == pygame.K_u:
                turntable.note_on(tone + 12, volume)
                KeyssNotes_dic["U"].draw = True
            if event.key == pygame.K_o:
                turntable.note_on(tone + 15, volume)
                KeyssNotes_dic["O"].draw = True
            if event.key == pygame.K_p:
                turntable.note_on(tone + 17, volume)
                KeyssNotes_dic["P"].draw = True
            if (event.key == pygame.K_LEFTBRACKET) or (event.key == ord('х')):
                turntable.note_on(tone + 20, volume)
                KeyssNotes_dic["{"].draw = True
            if (event.key == pygame.K_RIGHTBRACKET) or (event.key == ord('ъ')):
                turntable.note_on(tone + 22, volume)
                KeyssNotes_dic["}"].draw = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                turntable.note_off(tone, volume)
                KeyssNotes_dic["tab"].draw = False
            if event.key == pygame.K_w:
                turntable.note_off(tone + 3, volume)
                KeyssNotes_dic["W"].draw = False
            if event.key == pygame.K_e:
                turntable.note_off(tone + 5, volume)
                KeyssNotes_dic["E"].draw = False
            if event.key == pygame.K_t:
                turntable.note_off(tone + 8, volume)
                KeyssNotes_dic["T"].draw = False
            if event.key == pygame.K_y:
                turntable.note_off(tone + 10, volume)
                KeyssNotes_dic["Y"].draw = False
            if event.key == pygame.K_u:
                turntable.note_off(tone + 12, volume)
                KeyssNotes_dic["U"].draw = False
            if event.key == pygame.K_o:
                turntable.note_off(tone + 15, volume)
                KeyssNotes_dic["O"].draw = False
            if event.key == pygame.K_p:
                turntable.note_off(tone + 17, volume)
                KeyssNotes_dic["P"].draw = False
            if (event.key == pygame.K_LEFTBRACKET) or (event.key == ord('х')):
                turntable.note_off(tone + 20, volume)
                KeyssNotes_dic["{"].draw = False
            if (event.key == pygame.K_RIGHTBRACKET) or (event.key == ord('ъ')):
                turntable.note_off(tone + 22, volume)
                KeyssNotes_dic["}"].draw = False
