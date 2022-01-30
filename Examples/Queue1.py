import queue

#Queue(): 일반적인 큐 자료구조
data_queue1 = queue.Queue()
data_queue1.put(1) #1
data_queue1.put(2) #1 2
data_queue1.put(3) #1 2 3
print(data_queue1.get()) #1출력
print(data_queue1.get()) #2출력

#LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(Stack과 동일)
data_queue2 = queue.LifoQueue()
data_queue2.put(1) #1
data_queue2.put(2) #2 1
data_queue2.put(3) #3 2 1
print(data_queue2.get()) #3 출력
print(data_queue2.get()) #2 출력

#PriorityQueue(): 데이터마다 우선순위 지정하여 정렬된 큐. 우선순위 높은순으로 출력
data_queue3 = queue.PriorityQueue()
data_queue3.put((10, 1)) #(10, 1) #우선순위 수가 작을수록 높은 우선순위
data_queue3.put((3, 2)) #(3, 2) (10, 1)
data_queue3.put((12, 3)) #(3, 2) (10, 1) (12, 3)
print(data_queue3.get()) #(3, 2)출력
print(data_queue3.get()) #(10, 1)출력