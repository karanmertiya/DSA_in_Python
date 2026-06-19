# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Sort items in descending order of value/weight ratio. Greedily pick items with the highest ratio first. If an item cannot fit completely, take the fraction that fits.

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w

def fractionalKnapsack(W, arr, n):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if W >= item.weight:
            finalValue += item.value
            W -= item.weight
        else:
            finalValue += item.value * (W / item.weight)
            break
    return finalValue

