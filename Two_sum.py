def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target: "))

    result = twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()




