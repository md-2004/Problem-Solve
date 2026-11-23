def isvalid(s):
    stack=[]
    brackets={
        ")":"(",
        "]":"[",
        "}":"{"
    }
    for char in s:
        if char in brackets:
            if not stack or stack[-1]!=brackets[char]:
                return False
            stack.pop()

        else:
            stack.append(char)

    return len(stack)==0

def main():
    s=input("Enter brackets:")

    result=isvalid(s)
    print(result)

if __name__=="__main__":
    main()