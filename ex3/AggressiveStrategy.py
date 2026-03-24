from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        targets = self.prioritize_targets(battlefield)
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted_hand:
            cards_played.append(card.name)
            mana_used += card.cost
            damage_dealt += card.cost

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets,
            'damage_dealt': damage_dealt
        }