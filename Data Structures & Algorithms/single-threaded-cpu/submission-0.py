class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [[1,4],[3,3],[2,1]]
        # cost, index
        # 1: 4, 0
        # 2: 1, 2
        # 3: 3, 1
        # 
        # [[5,2],[4,4],[4,1],[2,1],[3,3]]
        # curr_time: cost, index
        # 2: 1, 3
        # 3: 3, 4
        # 6: 1, 2
        # 7: 2, 0
        # 9: 4, 1
        # 13: finish
        
        # curr_time = 0
        # sort by enqueue time to not repeat
        # [[1, 4, 0], [2, 1, 2], [3, 3, 1]]
        
        n = len(tasks)
        for i, task in enumerate(tasks):
            task.append(i)

        tasks.sort(key = lambda x : x[0])
        heap = []
        res = []
        curr_time = 0
        i = 0
        while i < n or heap:
            while i < n and tasks[i][0] <= curr_time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if heap:
                cost, idx = heapq.heappop(heap)
                res.append(idx)
                curr_time += cost
            else:
                curr_time = tasks[i][0]
        return res
        #     add to heap
        #     i += 1
        #         if heap isn't empty
        #         pop and updating curr_time
        #         else move current_time to tasks[i][0]
        
