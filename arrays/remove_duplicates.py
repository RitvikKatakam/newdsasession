def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

#example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 1, 5]
    print("Array with duplicates:", arr)
    print("Array without duplicates:", remove_duplicates(arr))