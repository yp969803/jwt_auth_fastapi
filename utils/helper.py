def createFileFromString(text, email):
    with open("c:/Users/hp/Desktop/cltrH2/utils/"+email+"/test.txt") as f:
        f.write(text)
        return f.name
    return ""