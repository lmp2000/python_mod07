from ex0.Card import Card

class SpellCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.used = False

    def play(self, game_state: dict) -> dict:
        if self.used:
            return {'error': 'spell already used'}
        self.used = True
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 
            f'Deal {self.cost} {self.effect_type} to target'
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True
        }

    def get_card_info(self) -> dict:
        dict1 = super().get_card_info()
        dict2 = {
            'effect_type': self.effect_type
        }
        return dict1 | dict2