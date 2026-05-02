class Solution(object):
    def solveNQueens(self, n):
        col=set()
        diag1=set()
        diag2=set()
        board=[['.']*n for i in range(n)]
        res=[]
        def generate(r):
            if(r==n):
                res.append(list("".join(i) for i in board))
                return
            for c in range(n):
                if(c in col or (r-c) in diag1 or (r+c) in diag2):
                    continue
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                board[r][c]='Q'
                generate(r+1)
                board[r][c]='.'
                diag1.remove(r-c)
                diag2.remove(r+c)
                col.remove(c)
        generate(0)
        return((res))