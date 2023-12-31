class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall(r"[a-zA-Z]+", paragraph.lower())
        counter = Counter(w for w in words if w not in banned)
        return counter.most_common(1)[0][0]
