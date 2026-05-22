class MyHashMap:

    def __init__(self):
        # Initialize with -1 to represent "no mapping"
        self.hashmap = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Direct index access is O(1)
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        # No need to search the list; just return the value at the index
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        # Reset the index to -1 instead of deleting the index
        self.hashmap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)