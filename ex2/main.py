from ex2.EliteCard import EliteCard


def main() -> None:
    print('\n=== DataDeck Ability System ===\n')

    warrior = EliteCard('Arcane Warrior', 6, 'Legendary', 5, 10, 3)
    game_state = {'available_mana': 8}

    print('EliteCard capabilities:')
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    print(f'Playing {warrior.name} (Elite Card):\n')

    print('Combat phase:')
    print(f'Attack result: {warrior.attack("Enemy")}')
    print(f'Defense result: {warrior.defend(2)}')
    print()

    print('Magic phase:')
    print(f'Spell cast: {warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])}')
    print(f'Mana channel: {warrior.channel_mana(3)}')
    print()

    print('Multiple interface implementation successful!')


if __name__ == '__main__':
    main()
