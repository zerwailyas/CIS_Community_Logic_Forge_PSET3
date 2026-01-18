def find_suspicious_device(nums):
    freq = {}
    n = len(nums) // 2

    for x in nums:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == n:
            return x

def main():
    # 🔽 HARD-CODED INPUT
    nums = [2, 1, 2, 5, 3, 2]

    print(find_suspicious_device(nums))

if __name__ == "__main__":
    main()