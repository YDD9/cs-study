import random
class Deck_Of_Cards():
    def shuffleCards(self):
        deck = range(52)
        random.shuffle(deck)
        # https://en.wikipedia.org/wiki/Suit_(cards)
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        ranks = ['Ace'] + range(2, 11) + ['Jack', 'Queen', 'King']  # 13
        for i in deck:
            suit = suits[i // 13]
            rank = ranks[i % 13]
            print('Card %02d: %r,\t%s'% (i, rank, suit))


if __name__=='__main__':
    d = Deck_Of_Cards()
    d.shuffleCards()