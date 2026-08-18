class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        queue = collections.deque() #[-cnt, idleTime]
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    idleTime = time + n
                    queue.append([cnt, idleTime])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time


