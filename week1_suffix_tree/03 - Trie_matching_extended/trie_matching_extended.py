# # python3
# import sys

# NA = -1

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4
# 		self.patternEnd = False

# def solve (text, n, patterns):
# 	result = []

# 	// write your code here

# 	return result

# text = sys.stdin.readline ().strip ()
# n = int (sys.stdin.readline ().strip ())
# patterns = []
# for i in range (n):
# 	patterns += [sys.stdin.readline ().strip ()]

# ans = solve (text, n, patterns)

# sys.stdout.write (' '.join (map (str, ans)) + '\n')

# python3
import sys


def build_trie(patterns):
    tree = dict()
    cnt = 0
    tree[0] = dict()
    for pattern in patterns:
        x = 0
        for i in pattern:
            if i in tree[x]:
                x = tree[x][i]
                continue
            else:
                cnt += 1
                tree[cnt] = {}
                tree[x][i] = cnt
                x = cnt
    return tree


def solve(text, n, patterns):
    tree = build_trie(patterns)
    result = set()
    for i in range(len(text)):
        x = 0
        j = i
        while j < len(text) and tree[x] != {}:
            try:
                x = tree[x][text[j]]
                j += 1
            except:
                break
        if '$' in tree[x]:
            result.add(i)
    return (list(result))


text = input().strip()
n = int(input().strip())
patterns = []
for i in range(n):
    patterns.append(input().strip() + '$')
tree = build_trie(patterns)
ans = solve(text, n, patterns)
print(' '.join(map(str, ans)))
