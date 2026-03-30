from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        enemy_creatures = []
        enemy_players = []
        others = []
        for target in available_targets:
            target_text = str(target).lower()
            if 'player' in target_text:
                enemy_players.append(target)
            elif 'enemy' in target_text:
                enemy_creatures.append(target)
            else:
                others.append(target)
        prioritized = enemy_creatures + enemy_players + others
        if not prioritized:
            return ['Enemy Player']
        return prioritized

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        creatures = [card for card in sorted_hand if self._is_creature(card)]
        non_creatures = [
            card for card in sorted_hand
            if not self._is_creature(card)
        ]
        ordered_hand = creatures + non_creatures

        targets = self.prioritize_targets(battlefield)
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in ordered_hand:
            cards_played.append(card.name)
            mana_used += card.cost
            attack_value = getattr(card, 'attack', None)
            if isinstance(attack_value, int):
                damage_dealt += attack_value
                continue
            attack_power = getattr(card, 'attack_power', None)
            if isinstance(attack_power, int):
                damage_dealt += attack_power
                continue
            damage_dealt += card.cost

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets,
            'damage_dealt': damage_dealt,
        }

    def _is_creature(self, card: object) -> bool:
        card_type = card.__class__.__name__.lower()
        has_combat_stats = (
            hasattr(card, 'attack')
            or hasattr(card, 'attack_power')
        )
        return has_combat_stats or 'creature' in card_type
