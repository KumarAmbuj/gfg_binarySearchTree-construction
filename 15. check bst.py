max=12345
min=-12345
arr = [5123, 3300, 783, 1111, 890]
flag=True
for i in range(1,len(arr)):
    if arr[i]> arr[i-1] and arr[i]>min and arr[i]<max:
        min = arr[i-1]

    elif arr[i]<arr[i-1] and arr[i]>min and arr[i]<max:
        max=arr[i-1]

    else:
        flag=False
        break
if (flag):
    print('bst')
else:
    print('not bst')