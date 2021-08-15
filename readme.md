# Snake

## Installation

Clone the repository and start your virtual environment. Open downloaded directory. Install all dependencies.
<pre>pip3 install -r requirements.txt</pre>

Run: <pre>python main.py</pre>
(If you use macOS you should replace `python` to `python3`)

## Gameplay Description

There are 3 modes: hard, medium, easy.

While playing <b>easy mode</b>, your apple takes 4 cells, it disappears in 18 seconds by default, you can go beyond edges.

While playing <b>medium mode</b>, your apple takes 4 cells, it disappears in 9 seconds by default, you can't go beyond edges, and you die if you collide them.

While playing <b>hard mode</b>, your apple takes 1 cell, it disappears in 6 seconds, and you can't go beyond edges.

Apple lifetime decreases every 10 points by 2 seconds. Every 5 points your speed increases by 3 FPS.
(Snake speed is measured in FPS here. In `code/settings/config.py` you can change default FPS value)

## Other

You can customize game for you. All the game settings are in this file. You can change:
- Object colors
- Snake speed
- Apple lifetime
- Tail length

*NOTE*: There is field `PLAYER_SPEED`, but I don't recommend changing it. You better to change `FPS`. 