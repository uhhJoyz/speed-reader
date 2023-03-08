
from PIL import ImageGrab
from pynput import mouse
from pytesseract import pytesseract
import pygame
import time
import re
from pynput import keyboard

ptot = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def mouse_setup():
    coordinates = []

    def on_click(x, y, button, pressed):
        if pressed:
            coordinates.append(x)
            coordinates.append(y)
            return False

    for i in range(0,2):
        with mouse.Listener(on_click = on_click) as L:
            L.join()

    return coordinates

def read_image(coordinates):
    print("Now entering read_image()")
    img = ImageGrab.grab(bbox=(coordinates[0], coordinates[1], coordinates[2], coordinates[3]))
    pytesseract.tesseract_cmd = ptot
    return pytesseract.image_to_string(img)

def preState():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def pause(item, screen, scrFont):

    while True:
        #invert image color because pause button is black
        img = pygame.image.load(".\\61039.png").convert_alpha()
        img = pygame.transform.scale(img, (64,64))
        inv = pygame.Surface(img.get_size())
        inv.fill((255,255,255))
        inv.blit(img, (0,0), None, pygame.BLEND_RGBA_SUB)
        img = inv
        img.set_colorkey((0,0,0))

        screen.fill((175,50,50))
        text = scrFont.render(item, 1, (200, 200, 200))
        textPosition = text.get_rect(center=(1920 / 2 - 1, 1080 / 2 - 1))
        shadow = scrFont.render(item, 1, (0,0,0))
        shadowPosition = shadow.get_rect(center=(1920 / 2 + 1, 1080 / 2 + 1))
        screen.blit(shadow, shadowPosition)
        screen.blit(text, (textPosition))
        screen.blit(img, (24,24))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        time.sleep(0.15)

def eventHandle(item, screen, scrFont):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause(item, screen, scrFont)

def splash(li):
    pygame.font.init()
    screen = pygame.display.set_mode((1920,1080))
    screen.fill((50,50,50))
    scrFont = pygame.font.Font(None, 90)
    pygame.display.update()

    preState()

    time.sleep(0.2)
    for item in li:

        # handle events
        eventHandle(item, screen, scrFont)

        text = scrFont.render(item,1,(255,255,255))
        trect = text.get_rect(center=(1920/2,1080/2))
        screen.blit(text, (trect))
        pygame.display.update()
        time.sleep(0.2)
        screen.fill((50,50,50))
    time.sleep(1)
    pygame.quit()

def textHandle(text):
    tx = re.sub("[\(\[].*?[\)\]]", "", text)
    tx = re.sub("(\.’)", "", tx)
    tx = re.sub("\—", "— ", tx)
    tx = re.sub("( )+", " ", tx)
    tx = re.sub("( \.)", ".", tx)
    tx = re.sub(" \—", "—", tx)

    print(tx)
    outs = tx.split("\n")
    fin = []
    for t in outs:
        for i in t.split():
            fin.append(i)
    return fin

# def stopCommand():
#
#     def on_activate_q():
#         print("Terminating program")
#         sys.exit()
#
#     def for_canonical(function):
#         return lambda k: function(stopListener.canonical(k))
#     hotkey = keyboard.HotKey(
#         keyboard.HotKey.parse('<ctrl>+<alt>+<shift>+q'), on_activate_q)
#     with keyboard.Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)
#     ) as stopListener:
#         stopListener.start()

def beginCommand():

    def on_activate_a():
        print("Beginning mouse_setup()")
        keyListener.stop()

    def for_canonical(function):
        return lambda k: function(keyListener.canonical(k))
    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<alt>+<shift>+a'), on_activate_a)
    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as keyListener:
        keyListener.join()

def main():
    # stopCommand()
    while(True):
        beginCommand()
        screensnip = mouse_setup()
        print(screensnip)
        text = read_image(screensnip)
        splash(textHandle(text))

main()