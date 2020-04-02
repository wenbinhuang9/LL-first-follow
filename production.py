def decodeProductionList(file):

    ans = []

    start = None
    with open(file) as fd:
        lines = fd.readlines()

        for line in lines:
            if line.startswith("start"):
                start = line.split()[1]
            elif line != "":
                production = decodeProduction(line)
                ans.append(production)

    if start == None:
        return ans
    else:
        return  (start, ans)

def decodeProduction(line):
    production_rule = line.split("->")
    left, right_rule = production_rule[0], production_rule[1]

    production = Production().left(left)

    rights = right_rule.split("|")

    production.right([right.strip() for right in rights])

    return production

class Production():
    def __init__(self):
        self.nonterminal = None

        self.rightList = []

    def left(self, nonterminal):
        self.nonterminal = nonterminal
        return self

    def right(self, rightDerivations):
        if isinstance(rightDerivations, list):
            self.rightList.extend(rightDerivations)
        else:
            self.rightList.append(rightDerivations)

        return self


