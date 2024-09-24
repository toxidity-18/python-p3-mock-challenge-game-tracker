class Result:
    """Class to represent a game result."""
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        
        # Register the result with the player
        player.add_result(self)
        # Register the result with the game
        game.add_result(self)


class Game:
    """Class to represent a game."""
    
    def __init__(self, title):
        self.title = title
        self._results = []

    def add_result(self, result):
        """Add a result to the game."""
        self._results.append(result)

    def results(self):
        """Return all results for the game."""
        return self._results

    def players(self):
        """Return unique players who have played the game."""
        unique_players = {result.player for result in self.results()}
        return list(unique_players)

    def average_score(self, player):
        """Calculate the average score of a player."""
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores) if scores else 0


class Player:
    """Class to represent a player."""
    
    def __init__(self, username):
        if not (2 <= len(username) <= 16) or not isinstance(username, str):
            raise ValueError("Username must be a string between 2 and 16 characters long.")
        
        self.username = username
        self._results = []

    def add_result(self, result):
        """Add a result to the player's results."""
        self._results.append(result)

    def results(self):
        """Return all results for the player."""
        return self._results

    def games_played(self):
        """Return unique games played by the player."""
        unique_games = {result.game for result in self.results()}
        return list(unique_games)

    def played_game(self, game):
        """Check if the player has played a specific game."""
        return game in self.games_played()

    def num_times_played(self, game):
        """Return the number of times the player has played a specific game."""
        return sum(1 for result in self.results() if result.game == game)

    @staticmethod
    def highest_scored(game):
        """Find the player with the highest average score for a given game."""
        players = game.players()
        highest_player = None
        highest_average = float('-inf')

        for player in players:
            avg_score = game.average_score(player)
            if avg_score > highest_average:
                highest_average = avg_score
                highest_player = player

        return highest_player
