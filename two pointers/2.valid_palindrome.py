def valid_palindrome(string):
    n = len(string)
    l,r = 0,n-1
    while l<r:
        if string[l]!=string[r]:
            return False
        l+=1
        r-=1
    return True

#example usage
if __name__ == '__main__':
    string = "riku"
    print(valid_palindrome(string))