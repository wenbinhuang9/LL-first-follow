from first import first, NONTERMINAL, EPSILON, decodeProductionList
from collections import defaultdict

def getFollow(input):
    start, productionList = decodeProductionList(input)

    firstMap = first(productionList)
    return follow(productionList, firstMap, start)

def follow(productionList, firstMap, start):

    followProductionMap = followProduction(productionList)

    followMap = defaultdict(list)

    followMap[start].append("$")

    for nonterminal, followList in followProductionMap.items():

        ans = __follow(nonterminal, firstMap, followMap, followProductionMap)
        followMap[nonterminal] = ans

    return  followMap

def __follow(nonterminal, firstMap, followMap, followProductionMap):
    followList = followProductionMap[nonterminal]

    if nonterminal  in followMap:
        return followMap[nonterminal]

    ans = []
    for right, left in followList:
        if right == "":
            subans = __follow(left, firstMap, followMap, followProductionMap )
            ans.extend(subans)
        else:
            subans =getFirstFromRight(right, firstMap)
            ans.extend(subans)

            if containEpsilon(right, firstMap):
                subans = __follow(left, firstMap, followMap, followProductionMap)
                ans.extend(subans)

    return list(set(ans))

def getFirstFromRight(right, firstMap):
    ans = []
    subans  = firstMap[right[0]]
    ans.extend(subans)
    if EPSILON in subans:
        ans.remove(EPSILON)
    i =1
    while i < len(right) and  EPSILON in subans:
        subans = firstMap[right[i]]
        i += 1
        ans.extend(subans)
        if EPSILON in subans:
            ans.remove(EPSILON)

    return list(set(ans))

def containEpsilon(right, fisrtMap):
    for symbol in right:
        if EPSILON not in fisrtMap[symbol]:
            return False

    return True

## A->w1Bw2, recording B, (w2, A) through map
def followProduction(proudctionList):
    floowProductionMap = defaultdict(list)

    for production in proudctionList:
        nonterminal = production.nonterminal

        for right in production.rightList:
            for i, symbol in enumerate(right):
                if symbol in NONTERMINAL:
                    floowProductionMap[symbol].append((right[i + 1:], nonterminal))

    return floowProductionMap
