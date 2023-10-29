def createFileFromString(text, email):
    with open("c:/Users/hp/Desktop/cltrH2/transciptModel/files/"+email+"/"+email+".txt",'w') as f:
        f.write(text)
        return f.name
    return ""

