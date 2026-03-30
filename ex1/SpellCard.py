from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type.lower()
        allowed_effects = {'damage', 'heal', 'buff', 'debuff'}
        if self.effect_type not in allowed_effects:
            raise ValueError(
                'effect_type must be one of: damage, heal, buff, debuff'
            )
        self.used = False

    def play(self, game_state: dict) -> dict:
        del game_state
        if self.used:
            return {'error': 'spell already used'}
        self.used = True
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self._describe_effect(),
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True,
        }

    def get_card_info(self) -> dict:
        return super().get_card_info() | {'effect_type': self.effect_type}

    def _describe_effect(self) -> str:
        if self.effect_type == 'damage':
            return f'Deal {self.cost} damage to target'
        if self.effect_type == 'heal':
            return f'Restore {self.cost} health to ally'
        if self.effect_type == 'buff':
            return f'Grant +{self.cost} attack to ally'
        if self.effect_type == 'debuff':
            return f'Reduce enemy attack by {self.cost}'
        return f'Apply {self.effect_type} effect'
