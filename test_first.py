import unittest


from  first import getFirst
class MyTestCase(unittest.TestCase):
    def test_first(self):
        input = "./expression"

        firstMap = getFirst(input)

        print (firstMap)

        ans = {'A': ['h', 'e', 'd', 'g'], 'S': ['a', 'b', 'e', 'd', 'g', 'h'], 'B': ['e', 'g'], 'C': ['h', 'e']}

        for k, v in ans.items():
            self.assertEqual( all([firstMap.get(k)[i]==v[i] for i in range(len(v))]), True)

if __name__ == '__main__':
    unittest.main()
