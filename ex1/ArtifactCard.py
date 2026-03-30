from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.in_play = False
        self.destroyed = False

    def play(self, game_state: dict) -> dict:
        del game_state
        if self.destroyed:
            return {'error': 'Artifact is destroyed'}
        if self.in_play:
            return {
                'card_played': self.name,
                'mana_used': 0,
                'effect': 'Artifact already active',
                'in_play': True,
                'destroyed': False,
            }
        self.in_play = True
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}',
            'in_play': True,
            'destroyed': False,
        }

    def activate_ability(self) -> dict:
        if self.destroyed:
            return {'error': 'Artifact is destroyed'}
        if not self.in_play:
            return {'error': 'Artifact is not in play'}

        self.durability -= 1
        if self.durability <= 0:
            self.destroyed = True
            self.in_play = False
            return {
                'artifact': self.name,
                'effect': self.effect,
                'durability': 0,
                'in_play': False,
                'destroyed': True,
            }
        return {
            'artifact': self.name,
            'effect': self.effect,
            'durability': self.durability,
            'in_play': True,
            'destroyed': False,
        }

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            'durability': self.durability,
            'effect': self.effect,
            'in_play': self.in_play,
            'destroyed': self.destroyed,
        }
