import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        time = 0

        for j, task in enumerate(tasks):

            time = max(time, j)

            # Release servers that are free
            while busy and busy[0][0] <= time:
                free_time, weight, i = heapq.heappop(busy)
                heapq.heappush(available, (weight, i))

            # If no server is available, jump to the earliest free time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] == time:
                    free_time, weight, i = heapq.heappop(busy)
                    heapq.heappush(available, (weight, i))

            # Assign task to the best available server
            weight, i = heapq.heappop(available)

            ans.append(i)

            # Update server's next free time
            heapq.heappush(busy, (time + task, weight, i))

        return ans