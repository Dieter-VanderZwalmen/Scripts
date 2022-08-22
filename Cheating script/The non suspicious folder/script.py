import re
from pynput.keyboard import Key, Controller,Listener
import time



keyboard = Controller()


with open ("Antwoorden.md","r",encoding="utf-8") as file:
    tekst = file.read().split("~~")
    global teller
    teller = 1
    def telleren(getal):
        global teller
        if(teller >= len(tekst)-1 or teller+getal < 0):
            teller = 0
            return
        teller += getal
    
    def on_press(key):
        global teller
        if key == Key.f2:##terug gaan
            keyboard.type(tekst[teller])
            
        if key == Key.f3:
            telleren(-1)
            print(teller)
        if key == Key.f4:
            telleren(1)
            print(teller)
        if key == Key.f11:
            listener.stop()
        
with Listener(on_press=on_press) as listener:
            listener.join()           









