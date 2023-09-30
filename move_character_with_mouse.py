from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_character(start_x, start_y, target_x, target_y):

    x, y = start_x, start_y
    frame = 0

    for i in range(0, 100 + 1, 2):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(target_x, target_y)
        t = i / 100
        x = (1 - t) * start_x + t * target_x
        y = (1 - t) * start_y + t * target_y
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.02)  # 적절한 딜레이를 주어 움직임이 자연스럽게 보이도록 함
    return x, y


def random_mouse():
    return random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)


running = True
hide_cursor()
start_x, start_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    target_x, target_y = random_mouse()
    start_x, start_y = move_character(start_x, start_y, target_x, target_y)
    handle_events()
close_canvas()

