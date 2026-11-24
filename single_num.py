def single_num(nums):
    for i in nums:
        if nums.count(i)==1:
            return i

def main():
    nums = list(map(int,input("Enter a numbers:").split()))

    result=single_num(nums)
    print(result)

if __name__=="__main__":
    main()