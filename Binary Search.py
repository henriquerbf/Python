list = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(list, value, begin, end):
    if end > begin:
        return "value not found"
    
    mid = (begin + end) // 2

    if value > list[mid]:
        binarySearch(list, value, mid + 1, end)
    elif value < list[mid]:
        binarySearch(list, value, begin, mid - 1)
    else:
        return mid

print("index of value: ", binarySearch(list, 6, 0, len(list)-1))