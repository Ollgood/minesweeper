""" Main function for generating minefield for minesweeper """
import random
from flask import render_template, Flask


application = Flask(__name__)


def create_map(width, height, mines):
    """ generates array of 0 of given width and height,
    then adds mines to random coordinates (randomint) to cells,
    which are not str ('*')then adds +=1 to fields near mines,
    using 12 hour clock in comments to help understanding where numbers will be added """

    minefield = []
    if mines >= (width * height):
        mines = (width * height) - 1
    for cell in range(height):
        minefield.append([0] * width)

    mine_count = 0
    while mine_count < mines:
        w_mine = random.randint(0, width - 1)
        h_mine = random.randint(0, height - 1)
        if not isinstance(minefield[w_mine][h_mine], str):
            minefield[w_mine][h_mine] = '*'
            mine_count += 1

    for row in range(len(minefield)):
        for cell in range(len(minefield[row])):
            if minefield[row][cell] == '*':

                # 12:00
                if row != 0 and isinstance(minefield[row - 1][cell], int):
                    minefield[row - 1][cell] += 1

                # 13:00
                if row != 0 and cell != height - 1 and\
                        isinstance(minefield[row - 1][cell + 1], int):
                    minefield[row - 1][cell + 1] += 1

                # 15:00
                if cell != height - 1 and isinstance(minefield[row][cell + 1], int):
                    minefield[row][cell + 1] += 1

                # 17:00
                if row != width - 1 and cell != height - 1 \
                        and isinstance(minefield[row + 1][cell + 1], int):
                    minefield[row + 1][cell + 1] += 1

                # 18:00
                if row != width - 1 and isinstance(minefield[row + 1][cell], int):
                    minefield[row + 1][cell] += 1

                # 19:00
                if row != width - 1 and cell != 0 and isinstance(minefield[row + 1][cell - 1], int):
                    minefield[row + 1][cell - 1] += 1

                # 21:00
                if cell != 0 and isinstance(minefield[row][cell - 1], int):
                    minefield[row][cell - 1] += 1

                # 23:00
                if row != 0 and cell != 0 and isinstance(minefield[row - 1][cell - 1], int):
                    minefield[row - 1][cell - 1] += 1

    for row in minefield:
        print(row)
    return minefield


@application.route('/', methods = ['GET'])
def page():
    """starts with made map of 8 width, 8 height, 10 mines"""

    minefield = create_map(8, 8, 10)
    return render_template('game.html', map = minefield )
