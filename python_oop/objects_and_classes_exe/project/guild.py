from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = f'{self.name}'
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if any([player_name == player.name for player in self.players]):
            current_player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(current_player)
            current_player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for player in self.players:
            result += f'{player.player_info()}\n'
        return result

