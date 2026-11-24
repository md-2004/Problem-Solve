def Majority_elem(nums):
    for i in nums:
        if nums.count(i)>len(nums)//2:
            return i

def main():
    nums=list(map(int,input("Enter a numbers:").split()))

    result=Majority_elem(nums)
    print(result)

if __name__=="__main__":
    main()