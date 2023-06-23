class Solution:
    def canWinNim(self, n: int) -> bool:
        """
            Observe from n = 1 to 8, you can figure out the only way you
            lose the game is when you have 4 stones remain in your turn.
            Then your competitor just to make no matter how you move you
            always have 4 remaining stone in your turn at last, until it
            doesn't. With this idea, you can partition 'n' by 4. As long
            as 'n' is multiple of 4, your competitor just to make sure
            every round you both take 4 stones in total, then they can win.
            Otherwise, they lose.
        """

        return True if n % 4 else False
