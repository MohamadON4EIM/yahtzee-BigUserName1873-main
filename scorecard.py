class Scorecard:
    def __init__(self):
        self.score = 0
        self.aces_used = False
        self.two_used = False
        self.threes_used = False
        self.fours_used = False
        self.fives_used = False
        self.sixes_used = False
        self.three_of_kind_used = False
        self.four_of_kind_used = False
        self.full_house_used = False        
        self.sm_straight_used = False
        self.lg_straight_used = False
        self.yahtzee_used = False
        self.chance_used = False

        self.bonus_yahtzee = False
    
    def remove_dups_and_sort(list:list):
        set(list)
        return sorted(set)

    def score_aces(self, dice:list):
        '''Scores the aces. Adds all the ones and adds it to the scorecard.'''
        round_score = 0
        for die in dice:
            if die == 1:
                round_score += 1

        self.aces_used = True
        return round_score
    
    def score_twos(self, dice:list):
        '''Scores the twos. Adds all the twos and adds it to the scorecard.'''
        round_score = 0
        for die in dice:
            if die == 2:
                round_score += 2

        self.two_used = True
        return round_score
    
    def score_threes(self, dice:list):
        '''Scores the threes. Adds all the threes and adds it to the scorecard.'''
        round_score = 0
        for die in dice:
            if die == 3:
                round_score += 3

        self.threes_used = True
        return round_score
    
    def score_fours(self, dice:list):
        '''Scores the fours. Adds all the fours and adds it to the scorecard.'''
        round_score = 0
        for die in dice:
            if die == 4:
                round_score += 4

        self.fours_used = True
        return round_score
    
    def score_fives(self, dice:list):
        '''Scores the fives. Adds all the fives and adds it to the scorecard.'''
        round_score = 0
        for die in dice:
            if die == 5:
                round_score += 5

        self.fives_used = True
        return round_score
    
    def score_sixes(self, dice:list):
        '''Scores the sixes. Adds all the sixes and adds it to the scorecard.'''
        round_score = 0
        for die in dice:
            if die == 6:
                round_score += 6

        self.sixes_used = True
        return round_score


    def large_straight(self,dice:list):
        round_score = 0
        
        if sorted(dice) == [1, 2, 3, 4, 5] or sorted(dice) == [2, 3, 4, 5, 6,]:
            self.lg_straight_used = True
            round_score += 40

        return round_score

    def yahtzee(self, dice:list):
        '''Scores the yahtzee. 
        It removes the duplicates from the list using set 
        and tests if the lenght is longer than one.'''
        round_score = 0

        dice_set = set(dice)

        if len(dice_set) == 1:
            if self.bonus_yahtzee == True:
                round_score += 100
            else:
                round_score += 50
                self.bonus_yahtzee = True

        return round_score



    def chance(self, dice:list):
        '''Scores the chance. Uses sum to add all the values.'''
        round_score = 0
        self.chance_used = True
        chance_score = sum(dice)
        round_score += chance_score

        return round_score


    def full_house(self, dice:list):
        '''Scores the full house. It removes the duplicates from the list using set and tests if the lenght is longer than two.'''
        round_score = 0

        sorted_dice = sorted(dice)

        if (
            sorted_dice[0] == sorted_dice[1] and sorted_dice[2] == sorted_dice[4] or
            sorted_dice[0] == sorted_dice[2] and sorted_dice[3] == sorted_dice[4]
        ):
            self.full_house_used = True
            round_score += 25

        return round_score

    def small_straight(self, dice:list):
        '''Score small straight.'''
        round_score = 0
        dice_check = 0


        dice_sorted = self.remove_dups_and_sort(dice)

        for i in range(4):
            if dice_sorted[i] + 1 == dice_sorted[i+1]:
                dice_check += 1
        if dice_check >= 3:
            round_score += 30
            self.sm_straight_used = True

        return round_score

    def four_of_a_kind(self, dice:list):

        round_score = 0 

        dice_sorted = self.remove_dups_and_sort(dice)
        
        if dice_sorted >=2 :
            dice_score = sum(dice)
            round_score += dice_score


    def theer_of_a_kind(self, dice:list):

        round_score = 0 

        dice_sorted = self.remove_dups_and_sort(dice)
        
        if dice_sorted >=3 :
            dice_score = sum(dice)
            round_score += dice_score

