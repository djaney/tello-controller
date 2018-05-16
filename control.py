import tellopy
import socket
import keyboard
import time

local_ip = socket.gethostbyname(socket.getfqdn())
drone = tellopy.Tello()

speed = 20

drone.connect()

drone.wait_for_connection(60.0)

while True:  # making a loop
    try:
        if keyboard.is_pressed('w'):
            drone.move_forward(speed)
            break
        elif keyboard.is_pressed('a'):
            drone.move_left(speed)
            break
        elif keyboard.is_pressed('s'):
            drone.move_backward(speed)
            break
        elif keyboard.is_pressed('d'):
            drone.move_right(speed)
            break
        elif keyboard.is_pressed('space'):
            drone.move_up(speed)
            break
        elif keyboard.is_pressed('ctrl'):
            drone.move_down(speed)
            break
        else:
            pass
    except:
        break
    time.sleep(0.1)
