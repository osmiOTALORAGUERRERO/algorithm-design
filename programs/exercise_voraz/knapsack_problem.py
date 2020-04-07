def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n)]

    # Build table K[][] in bottom up manner
    for i in range(1,n):
        for w in range(1, W+1):
            wi = wt[i]
            vi = val[i]

            if wi <= w:
              K[i][w] = max([K[i - 1][w - wi] + vi, K[i - 1][w]])
            else:
              K[i][w] = K[i - 1][w]
    for row in K:
        print(row)
    return K[n-1][W]
