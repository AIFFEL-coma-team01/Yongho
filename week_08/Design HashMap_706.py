'''
### 706. Design HashMap
---

내장 된 해시 테이블 라이브러리를 사용하지 않고 HashMap을 디자인합니다.

구체적으로 설계에는 다음 기능이 포함되어야합니다.

**put (key, value)** : (key, value) 쌍을 HashMap에 삽입합니다. 값이 이미 HashMap에있는 경우 값을 업데이트하십시오.   

**get (key)** : 지정된 키가 매핑 된 값을 반환하거나이 맵에 키에 대한 매핑이없는 경우 -1을 반환합니다.   

**remove (key)** :이 맵에 키에 대한 매핑이 포함 된 경우 값 키에 대한 매핑을 제거합니다.

2개의 풀이가 있습니다. 
1. ()을 받을 list와 key 값을 찾는 list 이렇게 2개의 list를 만들어서 사용했다.  ->  [()]

2. 1과는 다르게 key와 value를 받을 2개의 list를 만들어서 사용했다.  -> [()]

'''
# -----  -----



# 1636ms (12%)  17.1MB(91%)
# hash는 [()]의 구조를 만들고, 값의 원할한 검색을 위한 key 리스트를 생성한다. 

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = []
        self.key = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in self.key :
            idx = list(map(lambda x:x[0], self.hash)).index(key) # key의 위치를 받음
            del self.hash[idx] # 해당 위치의 인덱스를 삭제 
            # 삭제하는 이유 : tuple로 생성해서 값의 변경이 안됨
            self.hash.append((key,value))
        else :
            self.key.append(key)
            self.hash.append((key,value))
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        #idx = list(map(lambda x:x[0], self.hash)).index(key)
        if key in self.key :
            return self.hash[list(map(lambda x:x[0], self.hash)).index(key)][1]
        else :
            return -1
        
        #return -1 if key not in self.key else self.hash[list(map(lambda x:x[0], self.hash)).index(key)][1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.key :
            hash_idx = list(map(lambda x:x[0], self.hash)).index(key)
            key_idx = self.key.index(key)
            del self.key[key_idx]
            del self.hash[idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# ==============================================================================================

# ----- key, value를 받을 2개의 list 구조 생성 -----
# list의 인덱스 구조를 동일하게 해서 값의 수정, 삭제, 인덱싱등을 수행하게한다.

# 764ms (17.7%)
# 17.2MB (80%)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = []
        self.value = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in self.key :
            idx = self.key.index(key) #  인덱스 위치 반환
            self.value[idx] = value
        else :
            self.key.append(key)
            self.value.append(value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        #idx = list(map(lambda x:x[0], self.hash)).index(key)
        if key in self.key :
            idx = self.key.index(key)
            return self.value[idx]
        else :
            return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.key :
            idx = self.key.index(key)
            
            del self.key[idx]
            del self.value[idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)