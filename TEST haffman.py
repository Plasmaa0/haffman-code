class Node:
    def __init__(self, digit=None, freq=None, left=None, right=None, parent=None):
        self.digit = digit
        self.frequency = freq
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree:
    def __init__(self):
        self.root = None

    def newNode(self, digit, frequency):
        return Node(digit, frequency, None, None, None)


s = input()
rawdigits = list(set(s))
tree = list()
digits = list()
for digit in rawdigits:
    digits.append([digit, s.count(digit)])
digits.sort(key=lambda tup: tup[1])
tree.append(digits)
while len(tree[-1]) > 1:
    now = tree[-1]
    now.sort(key=lambda tup: tup[1])
    first = now[0]
    second = now[1]
    newelement = [first[0] + second[0], first[1] + second[1]]
    newlist = now[2::]
    newlist.append(newelement)
    tree.append(newlist)

for layer in tree:
    print(layer)
