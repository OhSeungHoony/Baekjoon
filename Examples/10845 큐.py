class Queue:
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        if (self.empty()):
            return -1
        else:
            output = self.list[0]
            self.list = self.list[1:]

            return output

    def empty(self):
        return 1 if len(self.list) == 0 else 0

    def size(self):
        return len(self.list)

    def front(self):
        if (self.empty()):
            return -1
        else:
            return self.list[0]

    def back(self):
        if (self.empty()):
            return -1
        else:
            return self.list[-1]


Case = int(input())
queue = Queue()

while (Case > 0):
    Case -= 1
    input_split = input().split()

    order = input_split[0]

    if (order == 'push'):
        queue.push(input_split[1])
    elif (order == 'pop'):
        print(queue.pop())
    elif (order == 'size'):
        print(queue.size())
    elif (order == 'empty'):
        print(queue.empty())
    elif (order == 'front'):
        print(queue.front())
    elif (order == 'back'):
        print(queue.back())
    else:
        print('xx')