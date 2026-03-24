from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from ex0.Card import Card


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        name = name_or_power if isinstance(name_or_power, str) else 'Dragon'
        power = name_or_power if isinstance(name_or_power, int) else 5
        return CreatureCard(name, power, 'Rare', power, power * 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        name = name_or_power if isinstance(name_or_power, str) else 'Fireball'
        power = name_or_power if isinstance(name_or_power, int) else 3
        return SpellCard(name, power, 'Common', 'damage')

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        name = name_or_power if isinstance(name_or_power, str) else 'Mana Ring'
        power = name_or_power if isinstance(name_or_power, int) else 2
        return ArtifactCard(name, power, 'Uncommon', 3, '+1 mana per turn')

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for i in range(size):
            if i % 3 == 0:
                cards.append(self.create_creature())
            elif i % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {'cards': cards, 'size': len(cards)}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }