class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, blocks, empty = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3,j//3)].add(board[i][j])
                else:
                    empty.append((i,j))
    
        def dfs():
            if not empty:
                return True
            
            r, c = empty[0]
            b = (r // 3, c // 3)
            for n in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                if n not in rows[r] and n not in cols[c] and n not in blocks[b]:
                    board[r][c]=n
                    rows[r].add(n)
                    cols[c].add(n)
                    blocks[b].add(n)
                    empty.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = '.'
                        rows[r].discard(n)
                        cols[c].discard(n)
                        blocks[b].discard(n)
                        empty.appendleft((r, c))
            return False
        
        dfs()
