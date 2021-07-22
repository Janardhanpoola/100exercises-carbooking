###Binary search

[1,2,3,4,5]

def binarys(arr,ele):
    start=0
    end=len(arr)-1
    
    found=False

    while start<=end and not found:
        mid=(start+end)//2
        if ele==arr[mid]:
            print("found at {}".format(mid))
            found=True
        elif ele<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    if found==False:
        print("nott found")


binarys([1,2,3,4,5],15)

