from ex0.CreatureCard import CreatureCard


def main() -> None:
    print('\n=== DataDeck Card Foundation ===\n')
    print('Testing Abstract Base Class Design:\n')

    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    game_state = {'available_mana': 6}

    print('CreatureCard Info:')
    print(dragon.get_card_info())
    print()

    print(
        f'Playing Fire Dragon with {game_state["available_mana"]} mana '
        'available:'
    )
    print(f'Playable: {dragon.is_playable(game_state["available_mana"])}')
    print(f'Play result: {dragon.play(game_state)}')
    print()

    print('Fire Dragon attacks Goblin Warrior:')
    print(f'Attack result: {dragon.attack_target("Goblin Warrior")}')
    print()

    game_state['available_mana'] = 3
    print(
        'Testing insufficient mana '
        f'({game_state["available_mana"]} available):'
    )
    print(f'Playable: {dragon.is_playable(game_state["available_mana"])}')
    print()

    print('Abstract pattern successfully demonstrated!')


if __name__ == '__main__':
    main()
