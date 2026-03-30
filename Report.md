# DataDeck Compliance Report

Scope checked: `subject.pdf` (all chapters), repository structure, all submitted Python files, `python3 -m exN.main` runtime, and `flake8`.

## 1) Must-fix blockers for full compliance

1. **Flake8 compliance is currently failing** (Common Instructions IV.1 says project must adhere to flake8).
   - Current failures include: `E302`, `E501`, `E131`, `F541`, `F841`, `W291`, `W292`, `W293`.
   - Run `flake8 .` and fix until zero errors.

2. **Submission cleanliness issue: compiled files are tracked in git** (`__pycache__/` and `*.pyc`).
   - The subject asks specific source files per exercise; tracked bytecode files are unnecessary and risky for evaluation.
   - Remove tracked `__pycache__`/`.pyc` files from git and ignore them.

3. **Potential signature/typing mismatch in `Deck.draw_card`**.
   - File: `ex1/Deck.py`
   - Current signature is `def draw_card(self) -> Card`, but it returns `None` when deck is empty.
   - To fully comply, either:
     - keep `-> Card` and raise a controlled exception on empty deck, or
     - change to `-> Card | None` (or `Optional[Card]`) and handle this in callers.

## 2) Exercise-specific gaps to fix

### ex0
1. **Positive integer validation is incomplete** for `attack`/`health` in `CreatureCard`.
   - File: `ex0/CreatureCard.py`
   - Requirement says positive integers; current checks only compare `<= 0`.
   - Add `isinstance(value, int)` validation (and reject bools if you want strict integer-only).

### ex1
1. **`SpellCard` effect behavior text is not aligned with spec categories**.
   - File: `ex1/SpellCard.py`
   - `effect_type` should represent `damage/heal/buff/debuff`; currently the play effect is always phrased as deal damage.
   - Adjust output/logic by `effect_type`.

2. **`ArtifactCard` should explicitly represent permanence-until-destroyed behavior.**
   - File: `ex1/ArtifactCard.py`
   - Add explicit in-play state and destroyed transition when durability reaches 0, so behavior matches spec wording.

### ex2
1. **No functional blocker found** in required interfaces/inheritance.
2. **But flake8 must be fixed** (`F841` unused `game_state`, line length).

### ex3
1. **`AggressiveStrategy` behavior is only partially aligned with required strategy behavior.**
   - File: `ex3/AggressiveStrategy.py`
   - Subject asks: prioritize attacking, play low-cost creatures first, target enemy creatures and player directly.
   - Current logic sorts all cards by cost and uses `battlefield` as-is for targets.
   - Update turn logic to prioritize low-cost creatures first and include direct player targeting when relevant.

2. **`FantasyCardFactory` misses "extensible card type registration" requirement.**
   - File: `ex3/FantasyCardFactory.py`
   - Add a registration mechanism (e.g., internal type registry and registration method) to support extension cleanly.

### ex4
1. **Core required architecture is implemented, but flake8 is failing in this exercise** (`E131`, `F541`, `E501`, `W292`).
   - Files: `ex4/TournamentCard.py`, `ex4/main.py`, `ex4/Rankable.py`, `ex4/__init__.py`

## 3) Global cleanup needed

1. Ensure all files end with newline (`W292`) and remove trailing whitespace (`W291`/`W293`).
2. Wrap long lines to <= 79 chars (`E501`).
3. Fix spacing/blank-line style (`E302`, `E131`).
4. Re-run:
   - `python3 -m ex0.main`
   - `python3 -m ex1.main`
   - `python3 -m ex2.main`
   - `python3 -m ex3.main`
   - `python3 -m ex4.main`
   - `flake8 .`

---

## Quick conclusion

Your architecture and exercise progression are mostly correct. The main reason it is **not yet fully compliant** is **flake8 non-compliance**, plus a few spec-behavior gaps (notably `draw_card` typing/behavior and ex3 strategy/factory expectations).
