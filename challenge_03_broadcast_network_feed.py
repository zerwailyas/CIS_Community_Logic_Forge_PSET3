def broadcast_network_feed(N, Q, K, operations):
    subscriptions = [set() for _ in range(N + 1)]
    messages = []
    user_messages = [[] for _ in range(N + 1)]

    msg_id = 1
    time = 0

    for op in operations:
        time += 1
        parts = op.split()

        if parts[0] == 'B':
            u = int(parts[1])
            m = int(parts[2])
            isCritical = (m % 3 == 0)

            messages.append((msg_id, time, u, isCritical))
            user_messages[u].append(msg_id)

            if len(user_messages[u]) > K:
                user_messages[u].pop(0)

            msg_id += 1

        elif parts[0] == 'S':
            u = int(parts[1])
            v = int(parts[2])
            subscriptions[u].add(v)

        elif parts[0] == 'U':
            u = int(parts[1])
            v = int(parts[2])
            subscriptions[u].discard(v)

        elif parts[0] == 'F':
            u = int(parts[1])
            feed = []

            for mid, t, sender, critical in reversed(messages):
                if sender == u or sender in subscriptions[u]:
                    if mid in user_messages[sender]:
                        feed.append((t, critical, mid))
                if len(feed) == 10:
                    break

            if not feed:
                print("EMPTY")
            else:
                feed.sort(key=lambda x: (-x[0], -x[1]))
                print(" ".join(str(x[2]) for x in feed))

N, Q, K = 3,9,2
operations = [
    "S 1 2",
    "S 1 3",
    "B 2 5",
    "B 3 9",
    "F 1",
    "U 1 2",
    "B 3 6",
    "F 1",
    "F 2"
]

broadcast_network_feed(N, Q, K, operations)


for _ in range(Q):
    operations.append(input().strip())
broadcast_network_feed(N, Q, K, operations)