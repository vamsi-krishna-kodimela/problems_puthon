def palin(word):
    if(len(word) == 1 or len(word) == 0):
        print(True)
    if(word[0] == word[-1]):
        palin(word[1:-1]) if (len(word) > 1) else palin("")

    else:
        print(False)


palin("hello")
palin("MOM")
