from pynput.keyboard import Key, Controller #Controlling the keyboard

from pynput import keyboard                 #monitoring the keyboard

               

Keyboard = Controller()                     #Controlling the keyboard

 

def on_press(key):
                print(key)
        if key == Key.f5:

                

                Keyboard.type('t/s = a')

                if key == Key.f8:
                        listener.close()

def on_release(key):

    pass

 

with keyboard.Listener(

        on_press=on_press,

        on_release=on_release) as listener:

    listener.join()
