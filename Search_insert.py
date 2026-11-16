def search_insert(nums,target):
    left=0
    right=len(nums)-1

    while left <= right:

        mid=(left+right)//2

        if nums[mid]==target:
            return mid

        elif nums[mid]<target:
            left=mid+1

        else:
            right=mid-1

    return left

def main():
    nums=list(map(int,input("Enter a numbers:").split()))
    target=int(input("Enter a target:"))

    result=search_insert(nums,target)

    print("insert position",result)

if __name__=="__main__":
    main()