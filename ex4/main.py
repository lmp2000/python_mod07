from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===\n')

    platform = TournamentPlatform()

    dragon = TournamentCard('Fire Dragon', 5, 'Legendary', 7, 10, 3)
    wizard = TournamentCard('Ice Wizard', 4, 'Rare', 5, 8, 2)

    print('Registering Tournament Cards...\n')
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f'{dragon.name} (ID: {dragon_id}):')
    print(f'- Interfaces: [Card, Combatable, Rankable]')
    print(f'- Rating: {dragon.ranking}')
    print(f'- Record: {dragon.wins}-{dragon.losses}')
    print()

    print(f'{wizard.name} (ID: {wizard_id}):')
    print(f'- Interfaces: [Card, Combatable, Rankable]')
    print(f'- Rating: {wizard.ranking}')
    print(f'- Record: {wizard.wins}-{wizard.losses}')
    print()

    print('Creating tournament match...')
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f'Match result: {match_result}')
    print()

    print('Tournament Leaderboard:')
    for i, card in enumerate(platform.get_leaderboard(), 1):
        print(f'{i}. {card.name} - Rating: {card.ranking} ({card.wins}-{card.losses})')
    print()

    print('Platform Report:')
    print(platform.generate_tournament_report())
    print()

    print('=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')


if __name__ == '__main__':
    main()
