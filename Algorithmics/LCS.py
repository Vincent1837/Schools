
s1 = "BADBCBA"
s2 = "ABACDBC"

def LCS(s1, s2):
    m, n = len(s1), len(s2)
    DP = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])
    print(DP)
    lcs_length = DP[m][n]
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif DP[i-1][j] > DP[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs

if __name__ == "__main__": 
    print(LCS(s1, s2))