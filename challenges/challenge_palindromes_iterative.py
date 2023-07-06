def is_palindrome_iterative(word):
    if word == "":
        return False
    else:
        for i in range(len(word)):
            if word[i] != word[-i - 1]:
                return False
        return True


is_palindrome_iterative("arara")
