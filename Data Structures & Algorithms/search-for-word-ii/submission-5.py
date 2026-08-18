class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #form a trie out of words
        root = TrieNode()
        curr = root
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWord = True
            curr.word = word

        #search through entire board and try to form words with trie
        seen = set()
        rows = len(board)
        cols = len(board[0])
        res = set()

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen or board[r][c] not in node.children:
                return

            seen.add((r, c))
            node = node.children[board[r][c]]

            if node.isWord:
                res.add(node.word)

            dfs(r + 1, c, node) 
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            seen.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(res)


