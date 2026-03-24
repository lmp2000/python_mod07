from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        word = card.name.split()
        id_word = word[-1].lower()
        count = len(self.cards) + 1
        card_id = f'{id_word}_{count:03d}'
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            return {"error": "One or both card IDs are not registered"}
        if card1_id == card2_id:
            return {"error": "A card cannot battle itself"}

        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        card1_score = card1.attack_power + card1.defense + card1.health
        card2_score = card2.attack_power + card2.defense + card2.health

        if card1_score >= card2_score:
            winner_id = card1_id
            loser_id = card2_id
        else:
            winner_id = card2_id
            loser_id = card1_id

        winner = self.cards.get(winner_id)
        loser = self.cards.get(loser_id)
        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.ranking,
            'loser_rating': loser.ranking
        }

    def get_leaderboard(self) -> list:
        leaderboard = sorted(
            self.cards.values(), key=lambda card: card.ranking
        )
        leaderboard.reverse()
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total = len(self.cards)
        if total == 0:
            avg = 0
        else:
            total_rating = sum(card.ranking for card in self.cards.values())
            avg = int(round(total_rating / total))

        status = "active" if total > 0 else "inactive"
        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": status,
        }
