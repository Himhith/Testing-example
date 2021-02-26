import unittest
import Guess



class TestGuess(unittest.TestCase):  # testing if file guess true  when numbers are  equal
    def test_guess_num(self):
        test_param_ans = 10
        test_param_num = 10
        result = Guess.guess_num(test_param_num, test_param_ans)
        self.assertEqual(result, True)

    # testing if file guess gives false when numbers are not equal
    def test_guess_num2(self):
        test_param_ans = 1
        test_param_num = 10
        result = Guess.guess_num(test_param_num, test_param_ans)
        self.assertEqual(result, False)

    def test_guess_num3(self):  # testing if file guess can take strings
        test_param_ans = 1
        test_param_num = '10'
        result = Guess.guess_num(test_param_num, test_param_ans)
        self.assertEqual(result, False)  # will output error


unittest.main()
