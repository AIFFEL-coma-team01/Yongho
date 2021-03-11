'''
Implement Queue using Stacks

두 개의 스택 만 사용하여 선입 선출 (FIFO) 대기열을 구현합니다. 구현 된 큐는 일반 큐의 모든 기능 (push, peek, pop 및 empty)을 지원해야합니다.

#### MyQueue 클래스를 구현합니다.

- void push (int x) 요소 x를 큐의 뒤쪽으로 푸시합니다.
- int pop () 대기열의 맨 앞에서 요소를 제거하고 반환합니다.
- int peek () 대기열의 맨 앞에있는 요소를 반환합니다.
- boolean empty () 대기열이 비어 있으면 true를 반환하고 그렇지 않으면 false를 반환합니다.

#### Notes:

스택의 표준 작업 만 사용해야합니다. 즉, 맨 위로 푸시, 맨 위에서 엿보기 / 팝, 크기 및 빈 작업 만 유효합니다.

언어에 따라 스택이 기본적으로 지원되지 않을 수 있습니다. 스택의 표준 작업 만 사용하는 한 목록 또는 deque (양방향 대기열)를 사용하여 스택을 시뮬레이션 할 수 있습니다.

후속 조치 : 각 작업이 O (1) 시간 복잡도로 분할되도록 대기열을 구현할 수 있습니까? 
즉, n 개의 작업을 수행하면 이러한 작업 중 하나가 더 오래 걸리더라도 전체 O (n) 시간이 걸립니다.
'''

# 24 ms
# leetcod 232 : Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = [] # 스택 초기화
        self.s2 = [] # 스택 초기화
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.extend([x])  # 앞쪽으로 append되는 형태이다.
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        front_stack = self.stack[0]
        del self.stack[0]
        return front_stack
        

    def peek(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()