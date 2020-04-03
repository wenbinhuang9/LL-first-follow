from first import first, NONTERMINAL, EPSILON, decodeProductionList, getFirstFromRight
from collections import defaultdict

def getFollow(input):
    start, productionList = decodeProductionList(input)

    firstMap = first(productionList)
    return follow(productionList, firstMap, start)

def follow(productionList, firstMap, start):

    followProductionMap = followProduction(productionList)

    followMap = defaultdict(list)



    for nonterminal, followList in followProductionMap.items():
        if nonterminal == "A":
            print ("here")
        ans = __follow(nonterminal, firstMap, followMap, followProductionMap, start)
        followMap[nonterminal] = ans

    return  followMap

def __follow(nonterminal, firstMap, followMap, followProductionMap, start):
    followList = followProductionMap[nonterminal]

    if nonterminal  in followMap:
        return followMap[nonterminal]

    ans = []

    if nonterminal == start:
        ans.append("$")
    for right, left in followList:
        if right == "" :
            if  nonterminal != left:
                subans = __follow(left, firstMap, followMap, followProductionMap, start )
                ans.extend(subans)
        else:
            subans =getFirstFromRight(right, firstMap)
            ans.extend(subans)

            if containEpsilon(right, firstMap) and nonterminal != left:
                subans = __follow(left, firstMap, followMap, followProductionMap, start)
                ans.extend(subans)

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
