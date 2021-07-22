#linear search (unordered list)


def ls(arr,ele):
    pos=0
    found=False
    while(pos<len(arr)) and not found:
        if ele==arr[pos]:
            found=True
            print("element {} found at position {} ".format(arr[pos],pos))
        else:
            pos+=1
    if found==False:
        print("ele not found")
    
ls([1,2,3,4,11,23,5],2)


#########################

#ordered list

#[1,2,3,4,5,6,7]

def ls_ordered(arr,ele):
    found=False
    stopped=False
    pos=0
    while pos<len(arr) and not found and not stopped:
        if ele==arr[pos]:
            found=True
            print(f'element found at {pos}')
        else:
            if (arr[pos]>ele):
               
                stopped=True
            else:
                pos=pos+1
    if found==False:
        print("not found")

ls_ordered([1,3,5,6,8],8)            