class PlayerState:
    """Stores the current game state (score and soldier count for a player within a game instance"""

    score = 0

    def __init__(self, name, gameParameters):
        self.name = name
        self.soldiers = gameParameters.fortCount * gameParameters.perSurvivedFortNewSoldiers + gameParameters.perTurnNewSoldiers

