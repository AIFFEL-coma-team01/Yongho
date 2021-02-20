'''
### 디자인 원형 데크


순환 양방향 대기열 (deque)의 구현을 설계하십시오.

구현은 다음 작업을 지원해야합니다.

- MyCircularDeque (k) : 생성자, deque의 크기를 k로 설정합니다.
- insertFront () : Deque 앞에 항목을 추가합니다. 작업이 성공하면 true를 반환합니다.
- insertLast () : Deque의 뒤쪽에 항목을 추가합니다. 작업이 성공하면 true를 반환합니다.
- deleteFront () : Deque의 전면에서 항목을 삭제합니다. 작업이 성공하면 true를 반환합니다.
- deleteLast () : Deque 뒷면에서 항목을 삭제합니다. 작업이 성공하면 true를 반환합니다.
- getFront () : Deque에서 전면 항목을 가져옵니다. deque가 비어 있으면 -1을 반환합니다.
- getRear () : Deque에서 마지막 항목을 가져옵니다. deque가 비어 있으면 -1을 반환합니다.
- isEmpty () : Deque가 비어 있는지 여부를 확인합니다.
- isFull () : Deque가 가득 찼는 지 여부를 확인합니다.

'''

# 최소 56ms [not import deque]
# leetcode 641 : Design Circular Deque

from collections import deque
# deque 를 imort 하지 않고 leetcode내의 deque 사용시 56ms

class MyCircularDeque:

    def __init__(self, k: int):
        self.len = k
        self.deque = [None for _ in range(k)]
        self.front = (k-1) % k
        self.last = 0


    def insertFront(self, value: int) -> bool:
        if self.deque[self.front] == None :
            self.deque[self.front] = value
            self.front = (self.front - 1) % self.len
            return True
        else :
            return False
        

    def insertLast(self, value: int) -> bool:

        if self.deque[self.last] == None :
            self.deque[self.last] = value
            self.last = (self.last+1) % self.len
            return True
        else :
            return False
        

    def deleteFront(self) -> bool:

        if self.deque[(self.front+1) % self.len] != None :
            self.deque[(self.front + 1) % self.len] = None
            self.front = (self.front+1) % self.len
            return True
        else :
            return False
        

    def deleteLast(self) -> bool:

        if self.deque[(self.last-1) % self.len] != None : 
            self.deque[(self.last - 1) % self.len] = None
            self.last = (self.last-1) % self.len
            return True
        else :
            return False
        

    def getFront(self) -> int:

        return self.deque[(self.front+1) % self.len] if self.deque[(self.front+1) % self.len] !=None else -1
        

    def getRear(self) -> int:

        return self.deque[(self.last-1) % self.len]if self.deque[(self.last-1) % self.len] !=None else -1


    def isEmpty(self) -> bool:
        return (self.last - self.front) % self.len == 1 and self.deque[(self.front + 1) % self.len] == None
        

    def isFull(self) -> bool:

        return (self.last - self.front) % self.len == 1 and self.deque[(self.front + 1) % self.len] != None
