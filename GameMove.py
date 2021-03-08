class GameMove:
    """Represents a move in a game"""

    def __init__(self, attackingSoldiers, defendingSoldiers, gameParameters):
        # validations
        if (len(attackingSoldiers) != gameParameters.fortCount):
            raise Exception("The tuple length of attacking soldiers must match the game's fort count")

        if (len(defendingSoldiers) != gameParameters.fortCount):
            raise Exception("The tuple length of defending soldiers must match the game's fort count")

        # ensure attackingSoldiers is monotonically decreasing
        for i in range(len(attackingSoldiers) - 1):
            if (attackingSoldiers[i + 1] > attackingSoldiers[i]):
                raise Exception("The attacking soldiers tuple must be sorted in decreasing order")

        # ensure defendingSoldiers is monotonically decreasing
        for i in range(len(defendingSoldiers) - 1):
            if (defendingSoldiers[i + 1] > defendingSoldiers[i]):
                raise Exception("The defending soldiers tuple must be sorted in decreasing order")

        self.attackingSoldiers = attackingSoldiers
        self.defendingSoldiers = defendingSoldiers

    def __str__(self):
        attacking = "Attacking: ("
        defending = "Defending: ("

        for index in range(len(self.attackingSoldiers)):
            if index > 0:
                 attacking = attacking + ", "
                 defending = defending + ", "
            attacking = attacking + f"{self.attackingSoldiers[index]}"
            defending = defending + f"{self.defendingSoldiers[index]}"
        attacking = attacking + ")"
        defending = defending + ")"
        return f"{attacking} {defending}"