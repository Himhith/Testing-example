import unittest
import S15Testing

class TestS15Testing(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = S15Testing.do_stuff(test_param)
        self.assertEqual(result, 15)

unittest.main()