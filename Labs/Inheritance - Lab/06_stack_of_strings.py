from typing import List


class Stack:

    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        element = self.data.pop()
        return element

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[" + ", ".join(reversed(self.data)) + "]"
