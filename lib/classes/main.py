class Player:
    all_players = []

    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self.username = username
        Player.all_players.append(self)

    def results(self):
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        players = [player for player in cls.all_players if player.played_game(game)]
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))


class Game:
    def __init__(self, title):
        self.title = title
        self._results = []

    def add_result(self, result):
        self._results.append(result)

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if not player_results:
            return 0
        return sum(player_results) / len(player_results)

    def results(self):
        return self._results


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
        game.add_result(self)  # Add result to the game's results
        player.add_result(self)  # Add result to the player's results

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
