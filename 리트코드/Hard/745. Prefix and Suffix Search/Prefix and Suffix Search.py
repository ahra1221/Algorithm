class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.dict = dict()
        for idx, word in enumerate(words):
            for i in range(1, len(word)+1):
                for j in range(1, len(word)+1):
                    self.dict[(word[:i], word[-j:])] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.dict.get((pref, suff), -1)
