import random
from flask import render_template, Flask

application = Flask(__name__)


def create_map(width, height, mines):
    map = []
    if mines >= (width * height):
        mines = (width * height) - 1
    for cell in range(height):
        map.append([0] * width)
    mine_count = 0
    while mine_count < mines:
        w_mine = random.randint(0, width - 1)
        h_mine = random.randint(0, height - 1)
        if not isinstance(map[w_mine][h_mine], str):
            map[w_mine][h_mine] = '*'
            mine_count += 1
    for row in range(len(map)):
        for cell in range(len(map[row])):
            if map[row][cell] == '*':
                # 12:00
                if row != 0 and isinstance(map[row - 1][cell], int):
                    map[row - 1][cell] += 1
                # 13:00
                if row != 0 and cell != height - 1 and isinstance(map[row - 1][cell + 1], int):
                    map[row - 1][cell + 1] += 1
                # 15:00
                if cell != height - 1 and isinstance(map[row][cell + 1], int):
                    map[row][cell + 1] += 1
                # 17:00
                if row != width - 1 and cell != height - 1 and isinstance(map[row + 1][cell + 1], int):
                    map[row + 1][cell + 1] += 1
                # 18:00
                if row != width - 1 and isinstance(map[row + 1][cell], int):
                    map[row + 1][cell] += 1
                # 19:00
                if row != width - 1 and cell != 0 and isinstance(map[row + 1][cell - 1], int):
                    map[row + 1][cell - 1] += 1
                # 21:00
                if cell != 0 and isinstance(map[row][cell - 1], int):
                    map[row][cell - 1] += 1
                # 23:00
                if row != 0 and cell != 0 and isinstance(map[row - 1][cell - 1], int):
                    map[row - 1][cell - 1] += 1
    for row in map:
        print(row)
    return map



@application.route('/', methods = ['GET'])
def page():
    map = create_map(8, 8, 10)
    return render_template('game.html', map = map )