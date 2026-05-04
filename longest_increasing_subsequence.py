from bisect import bisect_left

# returns length of longest increasing subsequence from input list of string
def lengthOfLIS(codes):
    tails = []
    for code in codes:
        # find position where 'code' should go
        idx = bisect_left(tails, code)
        if idx == len(tails):
            tails.append(code)
        else:
            tails[idx] = code
    return len(tails)

def lengthOfLIS_dp(codes):
    dp = [1] * len(codes)
    for i in range(1, len(codes)):
        for j in range(i):
            if codes[j] < codes[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def lengthOfLIS_dfs(codes):
    len_lis = 0
    seq = []

    def dfs(i):
        nonlocal len_lis
        if  i == len(codes):
            return 0
        if len(seq) == 0 or codes[i] > seq[-1]:
            seq.append(codes[i])
            len_lis = max(len_lis, len(seq))
            dfs(i+1)
            seq.pop()
        dfs(i+1)
    
    dfs(0)
    return len_lis

tests = [
    [["A1", "B2", "C3", "D4", "B1", "C2", "D3", "E4"], 5],
    [["A1", "B2", "C3", "D4", "B1"], 4],
    [["A1", "B2", "B1", "C3", "C2"], 3],
    [["A1", "C3", "B2", "B1", "C2"], 3],
    [["A1", "C3", "C2", "B1", "B2"], 3],
    [["A1", "C3", "C2", "B2", "B1"], 2],
    [["A1", "A1", "A1"], 1],
    [["C3", "B2", "A1"], 1],
    [["A1", "B2", "C3"], 3],
    [["A1", "B2"], 2],
    [["A1"], 1]
]

if __name__ == "__main__":
    for test in tests:
        result = lengthOfLIS(test[0])
        print(f"Input: {test[0]}, Expected: {test[1]}, Got: {result}" + (" <-- FAIL" if result != test[1] else ""))
