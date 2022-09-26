from pico2d import *

open_canvas()

star = load_image('star_run.png')
grass = load_image('grass.png')
x = 0
frame = 0

while(x<800):
    clear_canvas()
    grass.draw(400,270)
    star.clip_draw(frame*61, 0,50,80, x, 300 )
    update_canvas()

    frame = (frame + 1) % 7
    delay(0.05)
    x += 5
    get_events()

