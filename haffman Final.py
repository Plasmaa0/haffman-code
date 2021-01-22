class Node:
    '''
    node of a tree
    '''

    def __init__(self, digit=None, freq=None, left=None, right=None):
        self.digit = digit
        self.frequency = freq
        self.left = left
        self.right = right

    def __repr__(self):
        # , l: {self.left.digit}, r: {self.right.digit}
        return f'Node[\'{self.digit}\', {self.frequency}, l:{self.left}, r:{self.right}]'


def find(digit, node: Node, route):  # search in binary tree
    if len(node.digit) == 1:
        return route
    if digit in node.left.digit:
        route.append(0)
        return find(digit, node.left, route)
    elif digit in node.right.digit:
        route.append(1)
        return find(digit, node.right, route)


if __name__ == "__main__":
    s = input()
    rawdigits = list(set(s))
    number = len(rawdigits)
    tree = list()
    digits = list()
    for digit in rawdigits:
        digits.append(Node(digit, s.count(digit)))
    digits.sort(key=lambda tup: tup.frequency)
    tree.append(digits)
    while len(tree[-1]) > 1:
        now = tree[-1]
        now.sort(key=lambda tup: tup.frequency)
        first = now[0]
        second = now[1]
        newelement = Node(first.digit + second.digit,
                          first.frequency + second.frequency, first, second)
        newlist = now[2::]
        newlist.append(newelement)
        tree.append(newlist)
    tree = tree.pop().pop()
    rawdigits.sort()
    for digit in rawdigits:
        print(f'\'{digit}\' code: {find(digit, tree, list())}')
