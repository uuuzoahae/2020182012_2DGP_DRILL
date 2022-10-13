from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x , KPU_HEIGHT -1 -event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(TUK_WIDTH,TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('hand_arrow.png')