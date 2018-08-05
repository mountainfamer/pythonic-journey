# coding:utf-8

class Game_entry(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def __str__(self):
        return '{0}, {1}'.format(self._name, self._score)


class Scoreboard(object):

    def __init__(self, capacity=10):
        self._board = [None]*capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board): # no score drops from list
                self._n += 1 # so overall number increases
        j = self._n - 1
        while j > 0 and self._board[j-1].get_score( ) < score:
            self._board[j] = self._board[j-1] # shift entry from j-1 to j
            j -= 1
        self._board[j] = entry


if __name__ == '__main__':
    entry1 = Game_entry('Jack',89)
    entry2 = Game_entry('sofi',100)
    scoreBoard = Scoreboard()
    scoreBoard.add(entry1)
    scoreBoard.add(entry2)
    print scoreBoard

