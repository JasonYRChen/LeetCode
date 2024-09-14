class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        position = deque(range(len(deck)))
        position_map = []
        for i in range(len(deck)):
            position_map.append(position.popleft())
            if position:
                position.append(position.popleft())
        
        deck.sort()
        new_deck = [0 for _ in range(len(deck))]
        for i in range(len(deck)):
            new_deck[position_map[i]] = deck[i]

        return new_deck
