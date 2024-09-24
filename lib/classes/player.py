class Player:
    all_players = []

    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self.username = username
        Player.all_players.append(self)

    def results(self):
        # Return all results associated with this player
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        # Return a list of unique games the player has participated in
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        # Return the player with the highest average score in a given game
        players = [player for player in cls.all_players if player.played_game(game)]
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))
