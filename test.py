import unittest
from scorecard import Scorecard

class TestScoreCard(unittest.TestCase):

    def test_aces(self):
        sc = Scorecard()
        ace_score = sc.score_aces([1,5,4,3,1])
        self.assertEqual(ace_score, 2, "Expected 2")
        
        ace_score = sc.score_aces([1,1,4,1,1])
        self.assertEqual(ace_score, 4, "Expected 4")
        
        ace_score = sc.score_aces([4,4,4,4,4])
        self.assertEqual(ace_score, 0, "Expected 0")



    def test_twos(self):
        sc = Scorecard()
        twos_score = sc.score_twos([1,5,2,3,2])
        self.assertEqual(twos_score, 4, "Expected 4")
        
        twos_score = sc.score_twos([2,1,2,1,2])
        self.assertEqual(twos_score, 6, "Expected 6")
        
        twos_score = sc.score_twos([4,4,4,4,4])
        self.assertEqual(twos_score, 0, "Expected 0")

    def test_threes(self):
        sc = Scorecard()
        ace_score = sc.score_threes([1,5,4,3,1])
        self.assertEqual(ace_score, 3, "Expected 3")
        
        ace_score = sc.score_threes([1,1,4,1,1])
        self.assertEqual(ace_score, 0, "Expected 0")
        
        ace_score = sc.score_threes([3,4,3,4,4])
        self.assertEqual(ace_score, 6, "Expected 6")



    def test_fours(self):
        sc = Scorecard()
        twos_score = sc.score_fours([1,3,2,3,2])
        self.assertEqual(twos_score, 0, "Expected 0")
        
        twos_score = sc.score_fours([2,1,4,4,2])
        self.assertEqual(twos_score, 8, "Expected 8")
        
        twos_score = sc.score_fours([4,4,4,4,4])
        self.assertEqual(twos_score, 20, "Expected 0")

    def test_fives(self):
        sc = Scorecard()
        ace_score = sc.score_fives([1,5,4,3,1])
        self.assertEqual(ace_score, 5, "Expected 5")
        
        ace_score = sc.score_fives([1,1,4,1,1])
        self.assertEqual(ace_score, 0, "Expected 0")
        
        ace_score = sc.score_fives([3,4,5,4,5])
        self.assertEqual(ace_score, 10, "Expected 10")



    def test_sixes(self):
        sc = Scorecard()
        twos_score = sc.score_sixes([1,3,2,3,2])
        self.assertEqual(twos_score, 0, "Expected 0")
        
        twos_score = sc.score_sixes([6,1,4,4,2])
        self.assertEqual(twos_score, 6, "Expected 6")
        
        twos_score = sc.score_sixes([4,6,4,6,6])
        self.assertEqual(twos_score, 18, "Expected 18")

        
    def test_3otk(self):
        sc = Scorecard()
        three_of_a_kind_score = sc.three_of_a_kind([1,5,1,3,1])
        self.assertEqual(three_of_a_kind_score, 11, "Expected 11")
        
        ace_score = sc.three_of_a_kind([1,1,4,1,1])
        self.assertEqual(ace_score, 8, "Expected 8")
        
        ace_score = sc.three_of_a_kind([4,4,4,4,4])
        self.assertEqual(ace_score, 20, "Expected 20")

    def test_4otk(self):
        sc = Scorecard()
        four_of_a_kind_score = sc.four_of_a_kind([1,5,2,3,1])
        self.assertEqual(four_of_a_kind_score, 0, "Expected 0")
        
        four_of_a_kind_score = sc.four_of_a_kind([1,1,4,1,1])
        self.assertEqual(four_of_a_kind_score, 8, "Expected 8")
        
        four_of_a_kind_score = sc.four_of_a_kind([4,4,4,4,4])
        self.assertEqual(four_of_a_kind_score, 20, "Expected 20")


    def test_FullHouse(self):
        sc = Scorecard()
        full_houseScore = sc.full_house([1,5,2,3,1])
        self.assertEqual(full_houseScore, 0, "Expected 0")
        
        full_houseScore = sc.full_house([1,1,4,4,1])
        self.assertEqual(full_houseScore, 25, "Expected 8")
        
        full_houseScore = sc.full_house([4,4,4,4,4])
        self.assertEqual(full_houseScore, 25, "Expected 20")


    def test_SmallStraight(self):
        sc = Scorecard()
        full_houseScore = sc.small_straight([1,5,2,3,1])
        self.assertEqual(full_houseScore, 0, "Expected 0")
        
        full_houseScore = sc.small_straight([1,2,3,4,4])
        self.assertEqual(full_houseScore, 30, "Expected 3")
        
        full_houseScore = sc.small_straight([4,4,4,4,4])
        self.assertEqual(full_houseScore, 0, "Expected 20")

    def test_LargStraight(self):
        sc = Scorecard()
        full_LargStriaght = sc.large_straight([1,5,2,3,1])
        self.assertEqual(full_LargStriaght, 0, "Expected 0")
        
        full_LargStriaght = sc.large_straight([1,2,3,4,5])
        self.assertEqual(full_LargStriaght, 40, "Expected 3")
        
        full_LargStriaght = sc.large_straight([4,4,4,4,4])
        self.assertEqual(full_LargStriaght, 0, "Expected 20")

    def test_yahtzee(self):
        sc = Scorecard()
        full_yahtzee = sc.yahtzee([1,5,2,3,1])
        self.assertEqual(full_yahtzee, 0, "Expected 0")
        
        full_yahtzee = sc.yahtzee([1,2,3,4,4])
        self.assertEqual(full_yahtzee, 0, "Expected 3")
        
        full_yahtzee = sc.yahtzee([4,4,4,4,4])
        self.assertEqual(full_yahtzee, 50, "Expected 20")


    def test_(self):
        sc = Scorecard()
        full_chance = sc.chance([1,5,2,3,1])
        self.assertEqual(full_chance, 12, "Expected 0")
        
        full_chance = sc.chance([1,2,3,4,4])
        self.assertEqual(full_chance, 14, "Expected 3")
        
        full_chance = sc.chance([4,4,4,4,4])
        self.assertEqual(full_chance, 20, "Expected 20")



if __name__ == "__main__":
    unittest.main()