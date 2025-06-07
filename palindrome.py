def pali(word):
    reword=word[::-1]
    if word==reword:
        print(word,"is a palindrome")
    else:
        print(word,"is not a palindrome")

word=(input("Enter a word,I will tell is it a palindrome or not: "))
pali(word)