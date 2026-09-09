class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, reachable):
            if (r, c) in reachable:
                return
            reachable.add((r, c))

            directions = [(1, 0), [-1, 0], [0, 1],[0, -1]]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # Skip positions outside the island.
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                #Trace water backward: move uphill or across.
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)
        # Left edge: Pacific. Right edge: Atlantic.
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        result =[]
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result


