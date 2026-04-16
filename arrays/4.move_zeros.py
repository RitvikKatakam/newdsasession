def move_zeros(arr):
    j = 0
    n = len(arr)

    for i in range(n):
        if arr[i] != 0:
            arr[j],arr[i] = arr[i],arr[j]
            j+=1
    return arr

#example useage
if __name__ == '__main__':
    arr = [0,1,2,0,0,3,5,0,0]
    print(move_zeros(arr))