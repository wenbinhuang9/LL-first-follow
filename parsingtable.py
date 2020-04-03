
from collections import  defaultdict
from first import  first
from follow import follow, EPSILON
from production import  decodeProductionList

def createParseTable(input):
    start, productionList = decodeProductionList(input)

    firstMap = first(productionList)

    followMap = follow(productionList, firstMap, start)

    table = __create(productionList, firstMap, followMap)

    ##filter the same production in each value
    for key, value in table.items():
        table[key] = list(set(value))

    return table


def __create(productionList, first, follow):
    ans = defaultdict(list)
    for production in productionList:
        nonterminal = production.nonterminal
        for right in production.rightList:
            if right == EPSILON:
                print("here")
            firstInRight = getFirstFromRight(right, first)
            for s in firstInRight:
                ## ensure s is termina
                if s != EPSILON:
                    ans[(nonterminal, s)].append(nonterminal + "->" + right)

            if EPSILON in firstInRight:
                nonterminalFollow = follow[nonterminal]
                for s in nonterminalFollow:
                    ans[(nonterminal, s)].append(nonterminal + "->" + right)

                if "$" in nonterminalFollow:
                    ans[(nonterminal, "$")].append(nonterminal + "->" + right)


    ## filter the same production
    return ans

def getFirstFromRight(right, firstMap):
    ans = []
    subans  = firstMap[right[0]]
    ans.extend(subans)

    i =1
    while i < len(right) and  EPSILON in subans:
        subans = firstMap[right[i]]
        i += 1
        ans.extend(subans)


    return list(set(ans))