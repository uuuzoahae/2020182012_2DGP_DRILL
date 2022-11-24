from pico2d import *
import random

import game_world
import server
from background import FixedBackground as Background

class Ball:
    count = None
    image = None
    def __init__(self, x=200, y=200, count=0):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

        # self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2
        # print("canvas w: ",get_canvas_width() // 2)
        self.x, self.y = random.randint(0,get_canvas_width()), random.randint(0,get_canvas_height())
        Ball.count = 0
        # print("canvas h: ",get_canvas_height() // 2)
        # self.x, self.y, Ball.count = random.randint(300,600), random.randint(300,500), 0
        pass

    def update(self):
        pass


    def draw(ball):
        # self.image.clip_draw(0,0,300,300,self.x,self.y,25,25)
        sx, sy = ball.x - server.background.window_left, ball.y - server.background.window_bottom
        ball.image.clip_draw(0,0,300,300,sx,sy,25,25)

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            self.count += 1
        pass

    def get_bb(self):
        return self.x-1,self.y-1,self.x+1,self.y+1
        pass

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def count_ball(self):
        return self.count