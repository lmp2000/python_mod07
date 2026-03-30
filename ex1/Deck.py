from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        index = -1
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                index = i
        if index == -1:
            return False
        self.cards.pop(index)
        return True

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) <= 0:
            raise ValueError('Deck is empty')
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = len(
            [card for card in self.cards if isinstance(card, CreatureCard)]
        )
        spells = len(
            [card for card in self.cards if isinstance(card, SpellCard)]
        )
        artifacts = len(
            [card for card in self.cards if isinstance(card, ArtifactCard)]
        )
        avg = sum(
            [card.cost for card in self.cards]
        ) / total if total > 0 else 0
        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg
        }
