

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


def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue, totalWeight = 0.0, 0.0

    for item in itemsCopy:
        weight = item.getWeight()
        value = item.getValue()

        if (totalWeight + weight) <= maxWeight:
            result.append(item)
            totalWeight += weight
            totalValue += value

    return (result, totalValue, totalWeight)


def buildItems():
    names = ["clock", "painting", "radio", "vase", "book", "computer"]
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]

    items = []
    for i in range(len(names)):
        item = Item(names[i], values[i], weights[i])
        items.append(item)

    return items


def testGreedy(items, maxWeight, keyFunction):
    takenItems, totalValue, totalWeight = greedy(items, maxWeight, keyFunction)

    print("Total value taken is:", totalValue)
    print("Total weight taken is:", totalWeight)
    for item in takenItems:
        print("  ", item)


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1.0/item.getWeight()


def density(item):
    return item.getValue()/item.getWeight()


def testGreedys(maxWeight=20):
    items = buildItems()

    print("\nGreedy by value, max weight:", maxWeight)
    testGreedy(items, maxWeight, value)

    print("\nGreedy by weight, max weight:", maxWeight)
    testGreedy(items, maxWeight, weightInverse)

    print("\nGreedy by density, max weight:", maxWeight)
    testGreedy(items, maxWeight, density)

testGreedys()