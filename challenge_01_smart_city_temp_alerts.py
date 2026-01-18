def build_alert_days(temps, K):
    n = len(temps)
    alertDays = [0] * n

    # temperatures range: 30 to 100
    next_index = [-1] * 101  

    for i in range(n - 1, -1, -1):
        curr = temps[i]
        ans = float('inf')

        # warmer alert
        for t in range(curr + K, 101):
            if next_index[t] != -1:
                ans = min(ans, next_index[t])

        # colder alert
        for t in range(30, curr - K + 1):
            if next_index[t] != -1:
                ans = min(ans, next_index[t])

        if ans != float('inf'):
            alertDays[i] = ans

        # update future index
        next_index[curr] = i

    return alertDays
def preprocess(alertDays):
    n = len(alertDays)

    # Next alert index array
    nextAlert = [-1] * n
    last = -1

    for i in range(n - 1, -1, -1):
        if alertDays[i] != 0:
            last = alertDays[i]
        nextAlert[i] = last

    # Prefix sum array for COUNT queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if alertDays[i] != 0 else 0)

    return nextAlert, prefix
# INPUT
temps = [73, 74, 75, 71, 69, 72, 76, 73]
K = 3

queries = [
    ("NEXT", 2),
    ("COUNT", 1, 5),
    ("NEXT", 6)
]

# PROCESS
alertDays = build_alert_days(temps, K)
nextAlert, prefix = preprocess(alertDays)

print("Alert Days:", alertDays)

for q in queries:
    if q[0] == "NEXT":
        x = q[1]
        print("NEXT", x, "->", nextAlert[x])
    else:
        l, r = q[1], q[2]
        print("COUNT", l, r, "->", prefix[r + 1] - prefix[l])