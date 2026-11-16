def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    if sorted(str1)==sorted(str2):
        return True
    else:
        return False

def main():
    str1=input("Enter a string 1:")
    str2=input("Enter a string 2:")

    if is_anagram(str1,str2):
        print("Strings are Anagrams.")
    else:
        print("Strings are not anagrams.")

if __name__=="__main__":
    main()