# santa-games-bot-python

This is an example of how to write a Santa-Games bot in python.

This particular bot is not very smart, and in fact it just chooses a random empty place to play. All the of the API code is sperated out into a library so that the actual AI can just call normal functions like:

```python
game = api.get_game(game_id)
```
The above gets the game information from the API in the form of a dictionary (parsed from json).

## Getting started

To get started writing your own bot, the best way to start is to take a copy of this repository and copy the "tictactoe_bot_template.py. This file contains all the boiler plate code needed to write a tic-tac-toe bot.

You can run the file by passing the name of the file to python:

```python
python tictactoe_bot_template.py
```

The example bot, and the template both try things in the following order:
- Check if there is a game awaiting their turn.
- Check if someone else has proposed a game they can accept.
- If they don't currently have a game proposal, propose a game.

In the 'tictactoe_bot_template.py' file, there is a section:
```
# get a list of the free spaces
options = [i for i, c in enumerate(game_data) if c == ' ']
if len(options) == 0:
    print("Doesn't look like there's space for me to play..")
    continue

# EDIT HERE
# =========

option = random.choice(options)

# =========
```

This is where you can add you're own logic. The `game_data` variable contains a 9 character string, e.g. `"XO OO XX "`, and represents a grid going left to right, top to bottom. So the string `"123456789"` represents the tic-tac-toe grid:
```
123
456
789
```

To take a move, you return the position you want to play your peice in, which is just the integer value of that position. E.g. to play a peice in the top-right space, the option would be `3`.