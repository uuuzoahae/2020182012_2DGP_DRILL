from pico2d import *


def handle_events():
    global running
    global x,y
    global dir, dirud

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dirud += 1
            elif event.key == SDLK_DOWN:
                dirud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dirud -= 1
            elif event.key == SDLK_DOWN:
                dirud += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')

running = True
x = 800 // 2
y = 400 // 2 - 110
frame = 0
dir=0
dirud=0


def IDLE():

    global frame

    while(dir==0):
        clear_canvas()
        background.draw(400, 300)
        grass.draw(400, 30)

        if dir>0:
            character.clip_draw(frame*100,100*3,100,100,x,y)
        elif dir<0:
            character.clip_draw(frame*100,100*2,100,100,x,y)

        update_canvas()
        handle_events()
        frame = (frame + 1) % 8

        delay(0.01)




while running:
    clear_canvas()
    background.draw(400, 300)
    grass.draw(400, 30)

    if dir>0:
        character.clip_draw(frame * 100, 100 * 1 , 100, 100, x, y)
    elif dir<0:
        character.clip_draw(frame* 100, 100 *0 , 100, 100, x, y)
    elif dir==0:
        character.clip_draw(frame*100,100*2,100,100,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if x < 0:
        close_canvas()
    elif x > 800:
        close_canvas()
    elif y < 0:
        close_canvas()
    elif y > 600:
        close_canvas()

    y += dirud * 5
    x += dir * 5
    delay(0.01)

