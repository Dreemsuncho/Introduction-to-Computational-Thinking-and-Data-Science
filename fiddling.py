class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.weight) + ">"


def buildItems():
    names = ["clock", "painting", "radio", "vase", "book", "computer"]
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]

    items = []
    for i in range(len(names)):
        item = Item(names[i], values[i], weights[i])
        items.append(item)

    return items


def chooseBest(itemsPowerset, maxWeight, getVal, getWeight):
    bestSet = None
    bestVal = 0.0

    for items in itemsPowerset:
        itemsVal = 0.0
        itemsWeight = 0.0

        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)

            if (itemsWeight <= maxWeight) and (itemsVal > bestVal):
                bestVal = itemsVal
                bestSet = items

    return (bestSet, bestVal)


def getPowerset(L):
    res = []
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = getPowerset(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:  # for all smaller solutions, add one with last element
        new.append(small+extra)
    return smaller+new  # combine those with last element and those without


def testBest(maxWeight=20):
    items = buildItems()
    itemsPowerset = getPowerset(items)

    takenItems, itemsVal = chooseBest(itemsPowerset, maxWeight,
                                      Item.getValue, Item.getWeight)

    print("Total value of items taken is:", itemsVal)
    for item in takenItems:
        print(item)


testBest()
