class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ele in word:
            if ele not in cur.children:
                cur.children[ele] = TrieNode()
            cur = cur.children[ele]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ele in word:
            if ele not in cur.children:
                return False
            cur = cur.children[ele]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ele in prefix:
            if ele not in cur.children:
                return False
            cur = cur.children[ele]
        return True
        
        