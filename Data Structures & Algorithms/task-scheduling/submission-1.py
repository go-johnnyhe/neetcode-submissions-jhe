class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq:
                    queue.append([freq, time + n])
            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(maxHeap, freq)
        return time