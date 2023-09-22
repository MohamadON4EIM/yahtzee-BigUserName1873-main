import unittest


from scorecard import *

class TestAces(unittest.TestCase):
    def test_aces(self):
        self.sc = Scorecard()
        ace_score = self.sc.score_aces([6, 4, 1, 1, 1])
        self.assertEqual(ace_score, 3, "Error")



if __name__ == "__main__":
    unittest.main()