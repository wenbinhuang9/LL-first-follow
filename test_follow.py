import unittest

from  follow import  getFollow
class MyTestCase(unittest.TestCase):
    def test_follow(self):
        input = "./expression"
        followMap = getFollow(input)

        ans =  {'A': ['h', '$', 'g'], 'S': ['$'], 'B': ['a', 'h', '$', 'g'], 'C': ['h', 'b', '$', 'g']}

        for key, value in followMap.items():
            self.assertEqual(all([ans[key][i] == value[i] for i in range(len(value))]), True)
if __name__ == '__main__':
    unittest.main()
