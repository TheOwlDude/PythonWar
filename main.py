# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from GameInstance import GameInstance
from GameMove import GameMove
from GameParameters import GameParameters
from RandomPlayer import RandomPlayer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    gameParameters = GameParameters(3,8,3,3,2)
    gameInstance = GameInstance(gameParameters)
    me = gameInstance.AddPlayer("Me")
    rp = gameInstance.AddPlayer("Random")
    rpMover = RandomPlayer(rp, gameParameters, gameInstance)

    gameInstance.AcceptMove("Me", GameMove((4,2,0), (3,2,0), gameParameters))
    #gameInstance.AcceptMove("Random", GameMove((10,0,0), (2,0,0), gameParameters))
    gameInstance.AcceptMove("Random", GameMove((8,1,1), (2,0,0), gameParameters))
    #rpMover.GetRandomMove()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
