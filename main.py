from PIL import Image
import imagehash
import time
import keyboard
import os
import pyautogui
def main () -> None:
    while True:
            key = "l"
            if keyboard.is_pressed("j"):
                im = pyautogui.screenshot(("reticle.png"), region=(957,536,7,7))#Change both of these to match your reticle
                time.sleep(0.2)
                im2 = pyautogui.screenshot(("offset.png"), region=(957,536,7,7)) #change me too!
                reticle = imagehash.average_hash(Image.open("reticle.png"))
                offsetHash = imagehash.average_hash(Image.open("offset.png"))
                print(reticle, offsetHash)
                if reticle != offsetHash :
                    os.remove("offset.png")
                    os.remove("reticle.png")
                    print("images don't match, shooting!")
                    keyboard.press(key)
                    time.sleep(0.2)
                    keyboard.press(key)
main()