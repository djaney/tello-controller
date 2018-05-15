from tello import Tello
import socket
import keyboard

local_ip = socket.gethostbyname(socket.getfqdn())
controller = Tello(local_ip, 32768)

speed = 1

while True:  # making a loop
    try:
        if keyboard.is_pressed('w'):
            controller.move_forward(speed)
            break
        elif keyboard.is_pressed('a'):
            controller.move_left(speed)
            break
        elif keyboard.is_pressed('s'):
            controller.move_backward(speed)
            break
        elif keyboard.is_pressed('d'):
            controller.move_right(speed)
            break
        elif keyboard.is_pressed('space'):
            controller.move_up(speed)
            break
        elif keyboard.is_pressed('ctrl'):
            controller.move_down(speed)
            break
        else:
            pass
    except:
        break
