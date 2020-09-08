# python3
import sys


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    tree = dict()
    cnt = 0
    tree[0] = dict()
    for i in range(0, len(text)):
        x = 0
        for j in text[i:]:
            if j in tree[x]:
                x = tree[x][j]
                continue
            else:
                cnt += 1
                tree[cnt] = dict()
                tree[x][j] = cnt
                x = cnt
    print(tree)
    return result


if __name__ == '__main__':
    # text = sys.stdin.readline().strip()
    text = input().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
