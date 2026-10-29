def Remove_Elements(nums,value):
   
    k=0

    for i in range(len(nums)):
        if nums[i]!=value:
            nums[k]=nums[i]
            k+=1
    return k

def main():
    nums=list(map(int,input("Enter a numbers :").split()))
    value=int(input("Enter a value:"))

    k=Remove_Elements(nums,value)
    print("updated Array:",nums[:k])

if __name__ == "__main__":
    main()

        


        

