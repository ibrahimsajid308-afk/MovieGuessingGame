# Person 2's File
class GameLogic:
    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.lives = 6
        self.hidden = "*" * len(movie_title)

    def guess(self, letter):
        print(f"Logic checking letter: {letter}")
        # Logic to check letter goes here
        return self.hidden, self.lives
