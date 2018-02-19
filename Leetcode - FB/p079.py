class p079(object):

    def exists(self, board, word):
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.existsRecu(board, word, 0, i, j, visited):
                    return True
        return False

    def existsRecu(self, board, word, curr, i , j, visited):
        if curr == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[curr]:
            return False

        visited[i][j] = True

        result = self.existsRecu(board, word, curr + 1, i + 1, j, visited) or \
                self.existsRecu(board, word, curr + 1, i - 1, j, visited) or \
                self.existsRecu(board, word, curr + 1, i, j + 1, visited) or \
                self.existsRecu(board, word, curr + 1, i, j - 1, visited)

        visited[i][j] = False

        return result

S = p079()
board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
print S.exists(board, "ABCCED")
print S.exists(board, "SEE")
print S.exists(board, "ABCB")