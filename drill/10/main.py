import pico2d
import play_state
import logo_state
import item_state
import game_framework
start_state = logo_state # 모듈을 변수로 저장

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.close_canvas()