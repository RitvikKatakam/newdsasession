def find_missing_and_repeating(arr):
    n = len(arr)
    repeating = -1
    missing = -1
    visit = [0] * (n + 1)
    for num in arr:
        if visit[num] == 1:
            repeating = num
        visit[num] = 1
    for i in range(1, n + 1):
        if visit[i] == 0:
            missing = i
            break
    return missing, repeating

# driver code
if __name__ == "__main__":
    arr = [4, 3, 6, 2, 1, 1]  # n=6, missing=5, repeating=1
    missing, repeating = find_missing_and_repeating(arr)
    print(f"Missing: {missing}, Repeating: {repeating}")