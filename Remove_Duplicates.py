def Removeduplicates(nums):
    if len(nums) == 0:
        return 0
    k=1

    for i in range (1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1

    return k

def main():
    nums=list(map(int,input("Enter a numbers:").split()))

    k = Removeduplicates(nums)
    print("Unique elements :", nums[:k])

if __name__=="__main__":
    main()


