def Find_Difference(A,B):
    for char in B:
        if B.count(char)!=A.count(char):
            return char
def main():
    A=input("Enter a string:")
    B=input("Enter a string:")

    result=Find_Difference(A,B)
    print(result)

if __name__=="__main__":
    main()