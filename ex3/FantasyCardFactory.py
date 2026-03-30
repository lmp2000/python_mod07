from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_types: dict[str, dict] = {}
        self.spell_types: dict[str, dict] = {}
        self.artifact_types: dict[str, dict] = {}
        self._register_defaults()

    def register_creature_type(
        self,
        type_name: str,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        self.creature_types[type_name.lower()] = {
            'name': name,
            'cost': cost,
            'rarity': rarity,
            'attack': attack,
            'health': health,
        }

    def register_spell_type(
        self,
        type_name: str,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        self.spell_types[type_name.lower()] = {
            'name': name,
            'cost': cost,
            'rarity': rarity,
            'effect_type': effect_type,
        }

    def register_artifact_type(
        self,
        type_name: str,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        self.artifact_types[type_name.lower()] = {
            'name': name,
            'cost': cost,
            'rarity': rarity,
            'durability': durability,
            'effect': effect,
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            registered = self.creature_types.get(name_or_power.lower())
            if registered is not None:
                return CreatureCard(
                    registered['name'],
                    registered['cost'],
                    registered['rarity'],
                    registered['attack'],
                    registered['health'],
                )
            return CreatureCard(name_or_power, 5, 'Rare', 5, 10)

        if isinstance(name_or_power, int):
            return CreatureCard(
                'Dragon',
                name_or_power,
                'Rare',
                name_or_power,
                name_or_power * 2,
            )

        dragon = self.creature_types['dragon']
        return CreatureCard(
            dragon['name'],
            dragon['cost'],
            dragon['rarity'],
            dragon['attack'],
            dragon['health'],
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            registered = self.spell_types.get(name_or_power.lower())
            if registered is not None:
                return SpellCard(
                    registered['name'],
                    registered['cost'],
                    registered['rarity'],
                    registered['effect_type'],
                )
            return SpellCard(name_or_power, 3, 'Common', 'damage')

        if isinstance(name_or_power, int):
            return SpellCard('Fireball', name_or_power, 'Common', 'damage')

        fireball = self.spell_types['fireball']
        return SpellCard(
            fireball['name'],
            fireball['cost'],
            fireball['rarity'],
            fireball['effect_type'],
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            registered = self.artifact_types.get(name_or_power.lower())
            if registered is not None:
                return ArtifactCard(
                    registered['name'],
                    registered['cost'],
                    registered['rarity'],
                    registered['durability'],
                    registered['effect'],
                )
            return ArtifactCard(
                name_or_power,
                2,
                'Uncommon',
                3,
                '+1 mana per turn',
            )

        if isinstance(name_or_power, int):
            return ArtifactCard(
                'Mana Ring',
                name_or_power,
                'Uncommon',
                3,
                '+1 mana per turn',
            )

        mana_ring = self.artifact_types['mana_ring']
        return ArtifactCard(
            mana_ring['name'],
            mana_ring['cost'],
            mana_ring['rarity'],
            mana_ring['durability'],
            mana_ring['effect'],
        )

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for index in range(size):
            if index % 3 == 0:
                cards.append(self.create_creature())
            elif index % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {'cards': cards, 'size': len(cards)}

    def get_supported_types(self) -> dict:
        return {
            'creatures': sorted(self.creature_types.keys()),
            'spells': sorted(self.spell_types.keys()),
            'artifacts': sorted(self.artifact_types.keys()),
        }

    def _register_defaults(self) -> None:
        self.register_creature_type('dragon', 'Fire Dragon', 5, 'Rare', 5, 10)
        self.register_creature_type(
            'goblin',
            'Goblin Warrior',
            2,
            'Common',
            2,
            2,
        )
        self.register_spell_type('fireball', 'Fireball', 3, 'Common', 'damage')
        self.register_artifact_type(
            'mana_ring',
            'Mana Ring',
            2,
            'Uncommon',
            3,
            '+1 mana per turn',
        )
