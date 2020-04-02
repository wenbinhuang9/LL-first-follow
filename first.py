from collections import defaultdict
EPSILON = "e"

from production import  decodeProductionList
NONTERMINAL = set([chr(ord('A') + i) for i in range(0, 26)])

def getFirst(input):
    productionList = decodeProductionList(input)

    firstMap = first(productionList)

    firstMap = {k:list(set(v)) for k, v in firstMap.items()}

    return firstMap


def first(productionList):
    productionMap = getProductionMap(productionList)

    firstMap = defaultdict(list)

    for production in productionList:
        ans = __first(production, firstMap, productionMap)
        firstMap[production.nonterminal] = ans
    return firstMap


def getProductionMap(productionList):
    return {production.nonterminal: production for production in productionList }

def __first( production, firstMap, productionMap):
    nonterminal = production.nonterminal

    if nonterminal in firstMap.keys():
        return firstMap[nonterminal]
    ans = []


    for right in production.rightList:
        subans = firstEachRight(nonterminal, right, firstMap, productionMap)
        ans.extend(subans)

    return ans
def firstEachRight(nonterminal, right, firstMap, productionMap):

    if right == "":
        return []

    ## epsilon will be calculated here too
    if isFristTerminalInRight(right):
        return [right[0]]
    else:
        ans = []
        ## get first from nonterminal
        subnonterminal = right[0]
        subproduction = productionMap[subnonterminal]
        subFirst = __first(subproduction, firstMap, productionMap)

        ans.extend(subFirst)

        assert  subFirst != None

        if EPSILON in subFirst:
            subans = firstEachRight(nonterminal, right[1:], firstMap, productionMap)

            ans.extend(subans)
    return ans

def isFristTerminalInRight(right):
    return len(right) > 0 and right[0] not in NONTERMINAL



