import random

from GameMove import GameMove


class RandomPlayer:
    """Submits random moves. Allows a human player to play 'against' something"""

    def __init__(self, playerState, gameParameters, gameInstance):
        self.playerState = playerState
        self.gameParameters = gameParameters
        self.gameInstance = gameInstance

    def GetRandomMove(self):
        attackingSoldiers = []
        defendingSoldiers = []

        soldiersUsed = 0
        for index in range(self.gameParameters.fortCount):
            numberAttacking = random.randint(0, self.playerState.soldiers - soldiersUsed)
            attackingSoldiers.append(numberAttacking)
            soldiersUsed = soldiersUsed + numberAttacking
            numberDefending = random.randint(0, self.playerState.soldiers - soldiersUsed)
            defendingSoldiers.append(numberDefending)
            soldiersUsed = soldiersUsed + numberDefending

        attackingTuple = tuple(sorted(attackingSoldiers, reverse=True))
        defendingTuple = tuple(sorted(defendingSoldiers, reverse=True))

        move = GameMove(attackingTuple, defendingTuple, self.gameParameters)
        self.gameInstance.AcceptMove(self.playerState.name, move)

