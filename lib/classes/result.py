class Result:
    all_results = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise ValueError("player must be of type Player")
        if not isinstance(game, Game):
            raise ValueError("game must be of type Game")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000.")
        
        self._player = player
        self._game = game
        self._score = score
        Result.all_results.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
