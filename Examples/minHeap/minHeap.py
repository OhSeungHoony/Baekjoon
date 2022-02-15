class MinHeap:
    def __init__(self):
        self.queue = [None] # 0번 인덱스 빔


    def swap(self, a, b):
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    @staticmethod
    def parent(index): # index에 해당하는 원소의 부모 index return하는 함수
        return index//2


    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) - 1  # Last index
        while i > 1:  # root로 올때까지 부모와 비교하며 더 작으면 바꿔주고 반복한다.
            parent = self.parent(i)
            if self.queue[i] < self.queue[parent]:
                self.swap(i, parent)
                i = parent
            else:  # 만약 부모가 더 작으면 거기서 끝.
                break
    # 이 떄 부모가 i/2로 올라가기 때문에 최대 O(log n)번 연산한다.

    def delete(self):
        self.swap(1,len(self.queue)-1) #마지막 원소와 root를 바꿔주고
        self.queue.pop(len(self.queue)-1) #마지막 원소를 제거한다.
        self.minHeapify(1) #root에서 heapify를 시작한다.

    @staticmethod
    def leftchild(index): #왼쪽자식 index를 리턴
        return index*2

    @staticmethod
    def rightchild(index): #오른쪽자식 index를 리턴
        return index*2 + 1

    def minHeapify(self, i): #이 함수가 결국 자식들과 비교해 가면서 내려가는 함수입니다.
        left = self.leftchild(i)
        right = self.rightchild(i)
        smallest = i #일단은 가장 작은 것을 자신으로 놓고
        if left <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]: #만약 왼쪽 자식이 존재하고, 가장 작은 것보다 더 작으면
            smallest = left #가장작은 것은 왼쪽자식이 된다.
        if right <= len(self.queue)-1 and self.queue[right] < self.queue[smallest]: #만약 오른쪽 자식도 존재하고, 그것이 현재까지 최소보다 더 작으면
            smallest = right #가장 작은 것은 오른쪽 자식
        if smallest != i: #만약 자신이 가장 작은 것이 아니면,
            self.swap(i, smallest) #자식들 중 가장 작은 것과 바꿔주고
            self.minHeapify(smallest) #recursive call을 하여 내려가서 다시 진행

