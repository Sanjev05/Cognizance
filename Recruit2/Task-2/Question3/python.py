with open("/Users/sanjevr/Documents/GitHub/Cognizance/Recruit2/Task-2/Question3/about.txt","r") as file :
    
    line=file.read().lower()
    swsp=""
    for i in line:
        if i.isalpha():
            swsp+=str(i)
        else:
            swsp+=str(" ")
    d={}
    unique=[]
    strings=[]
    lofw =swsp.split()
    for i in lofw:
        if len(i)>=6:
            strings.append(i)
    for w in lofw:
        if w not in unique:
            unique.append(w)
    for i in unique:
        d[i]=0
    for i in unique:
        for j in lofw:
            if i==j:
                d[i]=d[i]+1
    print("The words that have more than six letters are :",strings)
    print("The most frequent word that is used in the about text file is :",max(zip(d.values(), d.keys()))[1])
    