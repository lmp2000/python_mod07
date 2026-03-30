from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if (
            attack <= 0
            or not isinstance(attack, int)
            or isinstance(attack, bool)
        ):
            raise ValueError('Attack must be bigger than 0')
        self.attack = attack
        if (
            health <= 0
            or not isinstance(health, int)
            or isinstance(health, bool)
        ):
            raise ValueError('Health must be bigger than 0')
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        dict1 = super().get_card_info()
        dict2 = {
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        }
        return dict1 | dict2
