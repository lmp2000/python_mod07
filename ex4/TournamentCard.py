from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        defense: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0:
            raise ValueError('Attack must be bigger than 0')
        if health <= 0:
            raise ValueError('Health must be bigger than 0')
        if defense < 0:
            raise ValueError('Defense must be bigger or equal to 0')

        self.attack_power = attack
        self.health = health
        self.defense = defense
        self.ranking = 1200
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get('available_mana', 0)
        if not isinstance(available_mana, int):
            return {'error': 'available_mana must be an integer'}
        if not self.is_playable(available_mana):
            return {'error': 'Not enough mana to play this card'}

        game_state['current_mana'] = available_mana - self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card enters battle',
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee',
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= max(0, incoming_damage - self.defense)
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.defense,
            'still_alive': self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'defense': self.defense,
            'health': self.health,
        }

    def calculate_rating(self) -> int:
        return self.ranking

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.ranking += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.ranking -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            'rating': self.ranking,
            'wins': self.wins,
            'losses': self.losses,
            'record': f'{self.wins}-{self.losses}',
        }

    def get_tournament_stats(self) -> dict:
        return self.get_card_info() | self.get_combat_stats() | {
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.ranking,
        }
