from Examples.minHeap import minHeap
import random

minheap = minHeap.MinHeap()
for i in range(10):
    num = random.randint(1, 50)
    minheap.insert(num)
print('heap :', minheap.queue)

for i in range(10):
    minheap.delete()
    print(f'delete {i+1}', minheap.queue)