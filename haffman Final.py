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
        return f'Node[\'{self.digit}\', {self.frequency}, l:{self.left}, r:{self.right}]'


def find(digit: str, node: Node, route: list) -> list:  # search in binary tree
    if len(node.digit) == 1:
        return route
    if digit in node.left.digit:
        route.append(0)
        return find(digit, node.left, route)
    elif digit in node.right.digit:
        route.append(1)
        return find(digit, node.right, route)


def arr2str(arr: list) -> str:
    s = ''
    for n in arr:
        s += str(n)
    return s


def code():
    print("Huffman coding\nInput text you want to code:", end=' ')
    s = input()
    rawdigits = list(set(s))
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
    code = dict()
    for digit in rawdigits:
        a = arr2str(find(digit, tree, list()))
        code[digit] = a
        print(f'\'{digit}\' code: {a}')
    print('Print coded text? (1-Y / 0-N): ', end='')
    if input() in ['1', 'Y', 'y']:
        n = str()
        for digit in s:
            n += code[digit]
        print(f'Output text: {n}')


def encode():
    print("Huffman code decoder.\nCreate a dictionary of differrent symbols.\nType: *anysymbol* + *space* + *code of this symbol*")
    print("Exmaple 'a 1101'.")
    print("Press enter once to begin typing next symbol's code.")
    print("Press enter twice to begin typing coded message.")
    code = dict()
    i = 0
    while True:
        try:
            i += 1
            print(f"{i} symbol:", end=' ')
            digit, c = input().split()
            code[c] = digit
        except ValueError:
            print("Type coded message:", end=' ')
            break
    s = input()
    s = list(s)
    buff = []
    decoded = []
    while True:
        if len(s) == 0:
            print(f'Encoded message: "{arr2str(decoded)}"')
            break
        buff.append(s.pop(0))
        g = arr2str(buff)
        if g in code:
            decoded.append(code[g])
            buff.clear()


if __name__ == "__main__":
    print("What you want to do?\n1. Code\n2. Encode\nAnswer: ", end='')
    if(int(input()) == 1):
        code()
    else:
        encode()
