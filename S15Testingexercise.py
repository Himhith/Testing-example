import unittest
import Guess
print('token')
class TestGuess(unittest.TestCase):
    def test_guess_num(self):
        test_param_ans = 10
        test_param_num = 10
        result = Guess.guess_num(test_param_num,test_param_ans)
        self.assertEqual(result, True)

    def test_guess_num2(self):
        test_param_ans = 1
        test_param_num = 10
        result = Guess.guess_num(test_param_num, test_param_ans)
        self.assertEqual(result, False)
    def test_guess_num3(self):
        test_param_ans = 1
        test_param_num = '10'
        result = Guess.guess_num(test_param_num, test_param_ans)
        self.assertEqual(result, False)

unittest.main()

