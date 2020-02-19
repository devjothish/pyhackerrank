if __name__ == '__main__':
   L = []

N = int(input())

for i in range(0, N):
    arr = input().split()

    if arr[0] == 'insert':
        L.insert(int(arr[1]), int(arr[2]))
    elif arr[0] == 'print':
        print (L)
    elif arr[0] == 'remove':
        L.remove(int(arr[1]))
    elif arr[0] == 'append':
        L.append(int(arr[1]))
    elif arr[0] == 'sort':
        L.sort()
    elif arr[0] == 'pop':
        L.pop()
    elif arr[0] == 'reverse':
        L.reverse()