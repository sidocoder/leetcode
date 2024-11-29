class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        pq = [(grid[0][0], 0, 0)]

        while pq:
            time, row, col = heapq.heappop(pq)
            if (row, col) == (rows - 1, cols - 1):
                return time
            if (row, col) in visited:
                continue
            visited.add((row, col))

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                if not self._is_valid(visited, next_row, next_col, rows, cols):
                    continue
                wait_time = (
                    1 if (grid[next_row][next_col] - time) % 2 == 0 else 0
                )
                next_time = max(grid[next_row][next_col] + wait_time, time + 1)
                heapq.heappush(pq, (next_time, next_row, next_col))

        return -1

    def _is_valid(self, visited, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols and (row, col) not in visited