def isPalindrome(s):
    s=s.lower()
    s="".join(ch for ch in s if ch.isalnum())
    return s==s[::-1]

def main():
    s=input("Enter a string:")
    result=isPalindrome(s)
    print(result)

if __name__=="__main__":
    main()
