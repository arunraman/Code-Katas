# def say_hello():
#     print 'Hello, World'

# for i in xrange(5):
#     say_hello()


#
# Your previous Plain Text content is preserved below:
#
# Please create a simulation of Modified Connect Four between two computer players which choose the next move randomly. The game should announce when a player wins or ties, and print out the state of the board after every turn.
#
# Connect Four is a two-player game played on a board with 6 rows and 7 columns. Players choose columns in which to place a token, which "drop" all the way down to the bottom to the lowest unoccupied row.
# See this link for a demo: https://www.mathsisfun.com/games/connect4.html
#
# The first player to obtain four contiguous tokens either horizontally or vertically wins. You do NOT have to worry about diagonal wins (hence the "Modified"). For example, the following conditions constitute a win:
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ O _ _ _ _
# _ X X X X _ _
# _ O X X O _ _
# _ O X O O O X
#
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ O O O _ X
# _ _ X X X O X
# _ _ O O O X X
# _ _ X O X O X
#
#
# Tips:
# - Don't worry too much about algorithmic complexity. A naive solution for the win checking is ok.
# - Focus on getting a working version first, before optimizing your code.
# - Feel free to explain your code as you write it, but this is not required--we'd rather see more progress towards completion.
# - We're looking for your speed, communication of ideas, decomposition, and ability to write clean and functional code.
#
#
# As an extension, add in the diagonal win condition.
#
#

# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ O _ _ _ _ _
# _ X _ _ _ _ _


import random


class Solution(object):
    def __init__(self):
        self.board = [['-' for i in xrange(7)] for j in xrange(6)]
        self.player1 = 'X'
        self.player2 = 'O'
        self.win = False


    def placeToken(self, randcolumn, player_token):
        for i in xrange(len(self.board) - 1, -1, -1):
            if self.board[i][randcolumn] == '-':
                self.board[i][randcolumn] = player_token
                return

    def playGame(self):
        w = self.winner()
        self.printBoard()
        if w != "":
            self.win = True
            return w

    def winner(self):
        # Check rows for winner
        for row in range(6):
            for col in range(3):
                if (self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] ==
                            self.board[row][col + 3]) and (self.board[row][col] != '-'):
                    return self.board[row][col]

        # Check columns for winner
        for col in range(6):
            for row in range(3):
                if (self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] ==
                            self.board[row + 3][col]) and (self.board[row][col] != '-'):
                    return self.board[row][col]

        # Check diagonal (top-left to bottom-right) for winner

        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] ==
                            self.board[row + 3][col + 3]) and (self.board[row][col] != '-'):
                    return self.board[row][col]

        # Check diagonal (bottom-left to top-right) for winner

        for row in range(5, 2, -1):
            for col in range(3):
                if (self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] ==
                            self.board[row - 3][col + 3]) and (self.board[row][col] != '-'):
                    return self.board[row][col]

        # No winner: return the empty string
        return ""


    def printBoard(self):
        for i in xrange(len(self.board)):
            for j in xrange(len(self.board[0])):
                print self.board[i][j],
            print "\n"
        print "------------------------"

    def Main(self):
        for i in xrange(0, 49):
            randcolumn = random.randrange(0, 7)
            self.placeToken(randcolumn, self.player1)
            w1 = self.playGame()
            if self.win == True:
                print w1 + " wins!"
                break
            self.placeToken(randcolumn, self.player2)
            w2 = self.playGame()
            if self.win == True:
                print w2 + " wins!"
                break
            print self.win


S = Solution()
S.Main()