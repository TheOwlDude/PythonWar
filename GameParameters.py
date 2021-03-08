class GameParameters:
    """The set of tunable parameters used by a GameInstance"""

    def __init__(self, fortCount, victoryScore, perTurnNewSoldiers, perSurvivedFortNewSoldiers, soldierUsageDeltaFactor):
        self.fortCount = fortCount
        self.victoryScore = victoryScore
        self.perTurnNewSoldiers = perTurnNewSoldiers
        self.perSurvivedFortNewSoldiers = perSurvivedFortNewSoldiers
        self.soldierUsageDeltaFactor = soldierUsageDeltaFactor

