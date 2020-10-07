class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.WORD_KEY = '$'
        Trie = {}
        for word in words:
            node = Trie
            for letter in word:
                if letter not in node:
                    node[letter] = dict()
                node = node[letter]
            node[self.WORD_KEY] = word

        matchedWords = []
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                self.backTracking(row, col, Trie, board, matchedWords)
        return matchedWords

    def backTracking(self, row, col, parent, board, matchedWords):
        letter = board[row][col]
        if letter not in parent:
            return
        currNode = parent[letter]
        if self.WORD_KEY in currNode:
            matchedWords.append(currNode[self.WORD_KEY])
            currNode.pop(self.WORD_KEY)

        board[row][col] = "#"
        dirs = (1, 0, -1, 0, 1)
        for i in range(4):
            nr, nc = row + dirs[i], col + dirs[i + 1]
            if nr > -1 and nr < len(board) and nc > -1 and nc < len(board[0]):
                self.backTracking(nr, nc, currNode, board, matchedWords)
        board[row][col] = letter
        return