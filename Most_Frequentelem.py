def most_frequent(arr):
    freq={}

    for num in arr:
        freq[num]=freq.get(num,0)+1

    max_element= None
    max_count= 0

    for num,count in freq.items():
        if count > max_count:
            max_count=count
            max_element=num

    return max_element,max_count

def main():
    arr=list(map(int,input("Enter a numbers:").split()))

    element,count=most_frequent(arr)

    print("most frequent number:",element)

if __name__== "__main__" :
    main()