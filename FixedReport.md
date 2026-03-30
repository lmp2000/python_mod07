# Fixed Report

## Validation Status
- `flake8 .` -> **PASS** (0 errors)
- `python3 -m ex0.main` -> **PASS**
- `python3 -m ex1.main` -> **PASS**
- `python3 -m ex2.main` -> **PASS**
- `python3 -m ex3.main` -> **PASS**
- `python3 -m ex4.main` -> **PASS**

## ex0
### `ex0/Card.py`
- Added one required blank line between imports and class definition (`E302`).
- Added final newline at end of file (`W292`).

### `ex0/CreatureCard.py`
- Tightened constructor validation to enforce integer checks:
  - `attack <= 0 or not isinstance(attack, int) or isinstance(attack, bool)`
  - `health <= 0 or not isinstance(health, int) or isinstance(health, bool)`
- This aligns better with the requirement of **positive integers**.

### `ex0/main.py`
- Wrapped long print statements to satisfy flake8 line length (`E501`).

### `ex0/__init__.py`
- Added final newline (`W292`).

## ex1
### `ex1/SpellCard.py`
- Refactored formatting to pass flake8 (`E302`, `W291`, `W292`).
- Normalized `effect_type` to lowercase.
- Enforced valid categories at initialization (`damage/heal/buff/debuff`);
  invalid values now raise `ValueError`.
- Added `_describe_effect()` and changed `play()` to produce effect text by category:
  - `damage` -> `Deal X damage to target`
  - `heal` -> `Restore X health to ally`
  - `buff` -> `Grant +X attack to ally`
  - `debuff` -> `Reduce enemy attack by X`
  - fallback -> `Apply <effect_type> effect`
- Kept one-time spell consumption behavior (`self.used`).

### `ex1/ArtifactCard.py`
- Implemented explicit permanence lifecycle:
  - Added `self.in_play` and `self.destroyed` state flags.
  - `play()` now:
    - rejects destroyed artifacts,
    - avoids replay cost if already active,
    - returns `Permanent: <effect>` and active state.
  - `activate_ability()` now:
    - rejects destroyed/not-in-play artifacts,
    - decrements durability,
    - marks artifact destroyed when durability reaches 0.
- Extended `get_card_info()` with `in_play` and `destroyed`.
- Fixed flake8 style/newline issues.

### `ex1/Deck.py`
- Kept required signature `draw_card(self) -> Card`.
- Added explicit empty-deck handling: raises `ValueError('Deck is empty')`
  instead of returning `None`.

### `ex1/__init__.py`
- Added final newline (`W292`).

## ex2
### `ex2/main.py`
- Removed unused variable `game_state` (`F841`).
- Split long spell-cast print into two steps (`E501`).

### `ex2/EliteCard.py`
- Fixed blank-line whitespace issue (`W293`) and class spacing (`E302`).
- Added final newline (`W292`).
- Minor string quote/style normalization (no behavior change).

### `ex2/__init__.py`
- Added final newline (`W292`).

## ex3
### `ex3/AggressiveStrategy.py`
- Reworked aggressive turn logic to match requested behavior:
  - Prioritizes **enemy creatures first**, then **enemy player**, else others.
  - If no targets exist, defaults to `['Enemy Player']`.
  - Plays **low-cost creatures first**, then other cards.
- Damage calculation now prefers combat stats when present:
  - uses `attack` integer when available,
  - else `attack_power`,
  - else falls back to `card.cost`.
- Added private helper `_is_creature()`.
- Fixed style/newline/line-length issues.

### `ex3/FantasyCardFactory.py`
- Added extensible registration system:
  - `register_creature_type(...)`
  - `register_spell_type(...)`
  - `register_artifact_type(...)`
- Added internal registries:
  - `self.creature_types`, `self.spell_types`, `self.artifact_types`
- Added `_register_defaults()` to preload:
  - `dragon`, `goblin`, `fireball`, `mana_ring`
- Updated `create_creature/create_spell/create_artifact`:
  - supports lookup by registered string key,
  - keeps existing support for custom strings and integer power paths,
  - uses defaults from registry when `None`.
- Updated `get_supported_types()` to return registered type keys dynamically.
- Fixed line-length/newline issues.

### `ex3/GameEngine.py`
- Added blank line between imports and class (`E302`).

### `ex3/main.py`
- Wrapped long print line (`E501`).

### `ex3/GameStrategy.py`
- Added final newline (`W292`).

### `ex3/__init__.py`
- Added final newline (`W292`).

## ex4
### `ex4/TournamentCard.py`
- Fixed indentation/alignment issues in constructor signature (`E131`).
- Added blank line before class (`E302`) and ensured final newline.
- Added type hint to `attack(self, target: str)`.
- Minor formatting cleanup (quote style, trailing commas, dict composition simplification).
- No functional regression in tournament logic.

### `ex4/main.py`
- Removed invalid f-strings without placeholders (`F541`).
- Wrapped long leaderboard print line (`E501`).

### `ex4/Rankable.py`
- Added final newline (`W292`).

### `ex4/__init__.py`
- Added final newline (`W292`).

## Root Package
### `__init__.py`
- Added final newline (`W292`).

## Notes
- Removed tracked `__pycache__/*.pyc` artifacts from the repository.
- Added `.gitignore` with:
  - `__pycache__/`
  - `*.pyc`
