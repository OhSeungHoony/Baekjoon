class Node: #노드 구현
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: #링크드리스트 구현
    def __init__(self):
        self.head = None

    def add(self, data): #노드 추가
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def delete(self, data): #노드 삭제
        node = self.head
        if node.data == data:
            self.head = node.next
            del node
        else:
            while node.next:
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next
                    del next_node
                else:
                    node = node.next

    def find(self, data): #노드 탐색
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.print()

ll.delete(1)
ll.print()

print(ll.find(1))