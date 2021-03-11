
'''
Implement Stack using Queues

두 개의 대기열 만 사용하여 LIFO (후입 선출) 스택을 구현합니다. 구현 된 스택은 일반 대기열 (push, top, pop 및 empty)의 모든 기능을 지원해야합니다.

MyStack 클래스를 구현합니다.

void push (int x) 요소 x를 스택의 맨 위로 푸시합니다.
int pop () 스택 맨 위에있는 요소를 제거하고 반환합니다.
int top () 스택 맨 위에있는 요소를 반환합니다.
boolean empty () 스택이 비어 있으면 true를 반환하고 그렇지 않으면 false를 반환합니다.
노트:

큐의 표준 작업 만 사용해야합니다. 즉, 푸시 투 백, 앞쪽에서 픽 / 팝, 크기 및 빈 작업 만 유효합니다.
언어에 따라 대기열이 기본적으로 지원되지 않을 수 있습니다. 
대기열의 표준 작업 만 사용하는 한 목록 또는 deque (양방향 대기열)를 사용하여 대기열을 시뮬레이션 할 수 있습니다.

'''

# 28ms
# leetcod 225 : Implement Stack using Queues
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dq = deque()  # 스택 초기화 ( deque )
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # 스택의 위로 계속 쌓기
        self.dq.extend(deque([x]))   # 최소 속도 28ms
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.dq.pop()  # 스택에 가장 위의 있는 값 제거하고 반환

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.dq[-1] # 스택 맨 위의 있는 요소 반환
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.dq else True
        # 스택이 비어있는 경우 True  아닌 경우 False