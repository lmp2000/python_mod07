from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                'error': 'Artifact is destroyed'
            }
        self.durability -= 1
        return {
            'artifact': self.name,
            'effect': self.effect,
            'durability': self.durability
        }

    def get_card_info(self) -> dict:
        dict1 = super().get_card_info()
        dict2 = {
            'durability': self.durability,
            'effect': self.effect
        }
        return dict1 | dict2