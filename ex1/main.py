from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print('=== DataDeck Deck Builder ===\n')

    deck = Deck()
    game_state = {'available_mana': 6}

    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    bolt = SpellCard('Lightning Bolt', 3, 'Common', 'damage')
    crystal = ArtifactCard('Mana Crystal', 2, 'Rare', 3, '+1 mana per turn')

    deck.add_card(bolt)
    deck.add_card(crystal)
    deck.add_card(dragon)

    print('Building deck with different card types...')
    print(f'Deck stats: {deck.get_deck_stats()}\n')

    print('Drawing and playing cards:\n')

    card = deck.draw_card()
    print(f'Drew: {card.name} (Spell)')
    print(f'Play result: {card.play(game_state)}\n')

    card = deck.draw_card()
    print(f'Drew: {card.name} (Artifact)')
    print(f'Play result: {card.play(game_state)}\n')

    card = deck.draw_card()
    print(f'Drew: {card.name} (Creature)')
    print(f'Play result: {card.play(game_state)}\n')

    print('Polymorphism in action: Same interface, different card behaviors!')


if __name__ == '__main__':
    main()
