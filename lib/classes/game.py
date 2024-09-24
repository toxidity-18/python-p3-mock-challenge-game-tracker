class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = title

    @property
    def title(self):
        return self._title

    def results(self):
        # Return all results associated with this game
        return [result for result in Result.all_results if result.game == self]

    def players(self):
        # Return a list of unique players who have played this game
        return list({result.player for result in self.results()})
