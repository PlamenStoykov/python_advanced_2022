from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added = []
        for p in args:
            if p not in self.players:
                self.players.append(p)
                added.append(p)
        return f"Successfully added: {', '.join([p.name for p in added])}"

    def add_supply(self, *args):
        for p in args:
            self.supplies.append(p)

    def find_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return p
        return None

    def __search_supply(self, sus_type):
        for i in range(len(self.supplies) - 1, -1, -1):
            s = self.supplies[i]
            if s.__class__.__name__ == sus_type:
                return i

    def sustain(self, player_name: str, sustenance_type: str):
        possible_sustenance = ['Food', 'Drink']
        current_player: Player = self.find_player(player_name)
        if current_player is None:
            return
        if sustenance_type not in possible_sustenance:
            return

        idx = self.__search_supply(sustenance_type)
        if idx is None:
            return f"There are no {sustenance_type.lower()} supplies left!"
        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."
        current_supply = self.supplies.pop(idx)
        amount = current_player.stamina + current_supply.energy
        current_player.stamina = min(100, amount)
        return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one: Player = self.find_player(first_player_name)
        player_two: Player = self.find_player(second_player_name)
        # check if Stamina is zero
        message = ''
        if player_one.stamina == 0:
            message += f'Player {player_one.name} does not have enough stamina.'
        if player_two.stamina == 0:
            message += f'\nPlayer {player_two.name} does not have enough stamina.'
        if message:
            return message.strip()
        # change order
        if player_one.stamina > player_two.stamina:
            player_one, player_two = player_two, player_one
        first_attack_damage = player_one.stamina / 2

        player_two.stamina = max(0, player_two.stamina - first_attack_damage)
        if player_two.stamina == 0:
            return f"Winner: {player_one.name}"
        second_attack_damage = player_two.stamina / 2
        player_one.stamina = max(0, player_one.stamina - second_attack_damage)
        if player_one.stamina == 0:
            return f"Winner: {player_two.name}"
        winner = player_one if player_one.stamina > player_two.stamina else player_two
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            amount = player.age * 2
            player.stamina = max(0, player.stamina - amount)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        message = ''
        for p in self.players:
            message += f'{str(p)}\n'
        for s in self.supplies:
            message += f'{s.details()}\n'
        return message.strip()

