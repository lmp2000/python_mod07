from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
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
        self.mana: int = 0

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            'attack': self.attack_power,
            'health': self.health,
            'defense': self.defense
        }

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite monster summoned to battlefield'
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= max(0, incoming_damage - self.defense)
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.defense,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'defense': self.defense,
            'health': self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana_pool': self.mana,
            'known_spells': ['Fireball', 'Rasengan', 'Kagebushin'],
        }
