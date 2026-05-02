class Solution(object):
    def totalNQueens(self, n):
        board=[["."]*n for i in range(n)]
        col=set()
        diag1=set()
        diag2=set()
        res=[]
        def generate(r):
            if(r==n):
                res.append(list("".join(i) for i in board))
            for c in range(n):
                if(c in col or (r-c) in diag1 or (r+c) in diag2):
                    continue
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                board[r][c]="Q"
                generate(r+1)
                diag1.remove(r-c)
                diag2.remove(r+c)
                col.remove(c)
                board[r][c]="."
        generate(0)
        return len(res)