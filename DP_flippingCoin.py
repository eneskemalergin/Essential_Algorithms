
def count(S, m, n):
    table = [[0 for x in range(m)] for x in range(n+1)] # Creating a table n+1 rows
    for i in range(m): # filling the entriest for 0 value case n = 0
        table[0][i] = 1
        
    for i in range(1 , n+1): # Filling rest of the table bottom-up manner
        for j in range(m):
            x = table[ i - S[j] ][j] if i-S[j] >= 0 else 0 # Count of solutions including S[j]
            y = table[i][j-1] if j >= 1 else 0 # Count of solutions excluding S[j]
            table[i][j] = x + y # total count
            
    return table[n][m-1]


n,m = map(int, raw_input().split())
S = map(int, raw_input().split())

print(count(S,m,n))
