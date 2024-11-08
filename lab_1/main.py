class Yahtzee:
    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        """Calculate the total score for the chance category."""
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total
    @staticmethod
    def yahtzee(dice):
        """Check if the player has a Yahtzee (five of a kind)."""
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        """Count the number of ones rolled."""
        count = 0
        if d1 == 1:
            count += 1
        if d2 == 1:
            count += 1
        if d3 == 1:
            count += 1
        if d4 == 1:
            count += 1
        if d5 == 1:
            count += 1
        return count
    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        """Count the score for twos rolled."""
        count = 0
        if d1 == 2:
            count += 2
        if d2 == 2:
            count += 2
        if d3 == 2:
            count += 2
        if d4 == 2:
            count += 2
        if d5 == 2:
            count += 2
        return count
    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        """Count the score for threes rolled."""
        count = 0
        if d1 == 3:
            count += 3
        if d2 == 3:
            count += 3
        if d3 == 3:
            count += 3
        if d4 == 3:
            count += 3
        if d5 == 3:
            count += 3
        return count
    def __init__(self, d1, d2, d3, d4, d5):
        """Initialize the Yahtzee game with five dice."""
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5
    def fours(self):
        """Count the score for fours rolled."""
        count = 0
        for at in range(5):
            if self.dice[at] == 4:
                count += 4
        return count
    def fives(self):
        """Count the score for fives rolled."""
        count = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 5:
                count += 5
        return count
    def sixes(self):
        """Count the score for sixes rolled."""
        count = 0
        for at in range(len(self.dice)):
            if self.dice[at] == 6:
                count += 6
        return count
    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        """Calculate the score for a pair."""
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        for at in range(6):
            if counts[6 - at - 1] == 2:
                return (6 - at) * 2
        return 0
    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        """Calculate the score for two pairs."""
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if counts[6 - i - 1] == 2:
                n += 1
                score += (6 - i)
        if n == 2:
            return score * 2
        else:
            return 0
    @staticmethod
    def four_of_a_kind(d1, d2, d3, d4, d5):
        """Check if there are four of a kind and return the score."""
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] == 4:
                return (i + 1) * 4
        return 0
    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        """Check if there are three of a kind and return the score."""
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if t[i] == 3:
                return (i + 1) * 3
        return 0
    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        """Check for a small straight and return the score."""
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0
    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        """Check for a large straight and return the score."""
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1 and
                tallies[5] == 1):
            return 20
        return 0
    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        """Check for a full house and return the score."""
        tallies = [0] * 6
        _2 = False
        _2_at = 0
        _3 = False
        _3_at = 0
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] == 2: 
                _2 = True
                _2_at = i + 1
        for i in range(6):
            if tallies[i] == 3: 
                _3 = True
                _3_at = i + 1
        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0
