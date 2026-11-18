def plus_one(nums):
    for i in range (len(nums)-1,-1,-1):

        if nums[i] < 9:
            nums[i]+=1
            return nums

        nums[i]=0

    return[1] + nums

def main():

    nums=list(map(int,input("Enter a numbers:").split()))

    result=plus_one(nums)
    print("Result",result)

if __name__ == "__main__":
    main()