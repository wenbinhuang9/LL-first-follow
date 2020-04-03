import unittest

from  follow import  getFollow
from  first import getFirst
from parsingtable import  createParseTable

class MyTestCase(unittest.TestCase):
    def test_first(self):
        input = "./production"

        firstMap = getFirst(input)

        print (firstMap)

        ans = {'A': ['h', 'e', 'd', 'g'], 'S': ['a', 'b', 'e', 'd', 'g', 'h'], 'B': ['e', 'g'], 'C': ['h', 'e']}

        for k, v in ans.items():
            self.assertEqual( all([firstMap.get(k)[i]==v[i] for i in range(len(v))]), True)

    def test_first_from_expression(self):
        input = "./expression"

        firstMap = getFirst(input)

        print (firstMap)

    def test_follow_from_expression(self):
        input = "./expression"
        followMap = getFollow(input)

        print(followMap)

        ans = {'A': [')', '$'], 'B': [')', '+', '$'], 'E': [')', '$'], 'T': [')', '+', '$'], 'F': [')', '+', '*', '$']}

        for k, v in ans.items():
            self.assertEqual(all([followMap.get(k)[i] == v[i] for i in range(len(v))]), True)


    def test_follow(self):
        input = "./production"
        followMap = getFollow(input)

        ans =  {'A': ['h', '$', 'g'], 'S': ['$'], 'B': ['a', 'h', '$', 'g'], 'C': ['h', 'b', '$', 'g']}

        for key, value in followMap.items():
            self.assertEqual(all([ans[key][i] == value[i] for i in range(len(value))]), True)



    def test_parse_table(self):
        input = "./expression"

        table = createParseTable(input)

        correctAns = {('F', '('): ['F->(E)'], ('E', '('):
            ['E->TA'], ('E', 'i'): ['E->TA'], ('B', '+'):
            ['B->e'], ('B', '*'): ['B->*FB'], ('T', 'i'): ['T->FB'],
                      ('B', ')'): ['B->e'], ('T', '('): ['T->FB'],
                      ('A', '$'): ['A->e'], ('A', '+'): ['A->+TA'],
                      ('A', ')'): ['A->e'], ('F', 'i'): ['F->i'],
                      ('B', '$'): ['B->e']}

        for key, value in table.items():
            self.assertEqual(all([correctAns[key][i] == value[i] for i in range(len(value))]), True)


if __name__ == '__main__':
    unittest.main()

