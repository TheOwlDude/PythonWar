from PlayerState import PlayerState

class GameInstance:
    """Represents an instance of a game either being played or perhaps already won"""

    players = {}

    moves = {}

    moveCounter = 1

    def __init__(self, gameParameters):
        self.gameParameters = gameParameters

    # add a player to the game
    def AddPlayer(self, playerName):
        if (len(self.players) >= 2):
            raise("The game already has enough players")

        if (playerName in self.players):
            raise("The game already has a player named " + playerName)

        newPlayer = PlayerState(playerName, self.gameParameters)
        self.players[playerName] = newPlayer

        return newPlayer

    # store a player's move. If receiving the move means we have both resolves the outcome
    def AcceptMove(self, playerName, gameMove):
        # validate
        if (len(self.players) < 2):
            raise Exception("The game has not started yet, still waiting for players")

        if (playerName not in self.players):
            raise Exception("Unknown player " + playerName)

        if (playerName in self.moves):
            raise Exception("Player " + playerName + " has already submitted their move")

        soldiersUsed = sum(gameMove.attackingSoldiers) + sum(gameMove.defendingSoldiers)
        if (soldiersUsed > self.players[playerName].soldiers):
            raise Exception("The supplied move uses more soldiers " + soldiersUsed + " than player " + playerName + " has " + self.players[playerName].soldierCount)

        self.moves[playerName] = gameMove

        if (len(self.moves) >= 2):
            self.ResolveMove()

    # update game states based on the supplied moves
    def ResolveMove(self):

        playerNames = list(self.players)
        player1 = self.players[playerNames[0]]
        player2 = self.players[playerNames[1]]

        print(f"Applying Move {self.moveCounter} :: {player1.name}[ {self.moves[player1.name]} ] | {player2.name}[ {self.moves[player2.name]} ]")

        # adjust score based on destroyed forts
        player1FortsDestroyed = 0
        player2FortsDestroyed = 0

        player1Move = self.moves[player1.name]
        player2Move = self.moves[player2.name]

        for i in range(self.gameParameters.fortCount):
            if(player1Move.attackingSoldiers[i] > player2Move.defendingSoldiers[i]):
                player1FortsDestroyed = player1FortsDestroyed + 1

            if(player2Move.attackingSoldiers[i] > player1Move.defendingSoldiers[i]):
                player2FortsDestroyed = player2FortsDestroyed + 1

        # adjust game state
        player1SoldiersUsed = sum(player1Move.attackingSoldiers) + sum(player1Move.defendingSoldiers)
        player2SoldiersUsed = sum(player2Move.attackingSoldiers) + sum(player2Move.defendingSoldiers)

        player1SoldiersUsedBonus = 0
        player2SoldiersUsedBonus = 0

        if (player1SoldiersUsed < player2SoldiersUsed):
            player1SoldiersUsedBonus = (player2SoldiersUsed - player1SoldiersUsed) // self.gameParameters.soldierUsageDeltaFactor

        if (player2SoldiersUsed < player1SoldiersUsed):
            player2SoldiersUsedBonus = (player1SoldiersUsed - player2SoldiersUsed) // self.gameParameters.soldierUsageDeltaFactor

        player1.score = player1.score + player1FortsDestroyed
        player2.score = player2.score + player2FortsDestroyed

        player1.soldiers = (player1.soldiers - player1SoldiersUsed) + self.gameParameters.perTurnNewSoldiers + player1SoldiersUsedBonus
        player1.soldiers = player1.soldiers + self.gameParameters.perSurvivedFortNewSoldiers * (self.gameParameters.fortCount - player2FortsDestroyed)

        player2.soldiers = (player2.soldiers - player2SoldiersUsed) + self.gameParameters.perTurnNewSoldiers + player2SoldiersUsedBonus
        player2.soldiers = player2.soldiers + self.gameParameters.perSurvivedFortNewSoldiers * (self.gameParameters.fortCount - player1FortsDestroyed)

        self.moves = {}

        print(f"Result After Move {self.moveCounter} :: {self}")

        self.moveCounter = self.moveCounter + 1

    def __str__(self):
        result = ""
        playerNames = list(self.players)
        for playerName in playerNames:
            player = self.players[playerName]
            result = result +  f"{playerName}[ Score: {player.score}, Soldiers: {player.soldiers} ] | "
        return result





