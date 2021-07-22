#bubble sort
#In every pass the next largest element will be in place

def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        print(f'this is {n} pass')
        for k in range(n):
            print(k)
            if arr[k]>arr[k+1]:
                temp=arr[k]
                arr[k]=arr[k+1]
                arr[k+1]=temp
                print(arr)
                #print("-------------")
    return arr

print(bubble_sort([100,2,42,5]))
print("+++++++++++++")

##############################################################################################

#Selection sort

#[100,20,1,6,4]

def selection_sort(arr):
    for n in range(len(arr)-1,0,-1):
        max_pos=0
        print(n)
        for k in range(1,n+1):           
            if arr[k]>arr[max_pos]:
                max_pos=k
        arr[n],arr[max_pos]=arr[max_pos],arr[n]
        print(arr)

    return arr
        

print(selection_sort([100,20,1,6,4]))

#####################################33
#Insertion sort
########################


def Insertionsort(arr):
    for i in range(1,len(arr)):
        cur_value=arr[i]
        pos=i
        while pos>0 and  arr[pos-1]>cur_value:
            arr[pos]=arr[pos-1]
            pos=pos-1
            arr[pos]=cur_value
    return arr

print(Insertionsort([100,20,1,6,4]))