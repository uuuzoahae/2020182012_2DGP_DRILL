from pico2d import *
import game_framework
import play_state

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('add_delete_boy')
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    global logo_time
    global running
    if logo_time > 0.5:
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01
    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()

