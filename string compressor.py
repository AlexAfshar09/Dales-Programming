def encoder(string, omit_ones=False):
    encoded=""
    i=0

    while i<len(string):
        count=1

        while i+1<len(string) and string[i]==string[i+1]:
            count+=1
            i+=1

        if omit_ones and count==1:
            encoded+=string[i]
        else:
            encoded+=string[i]+str(count)

        i+=1
    return encoded

while True:
    string=input("enter string or 0 to exit:")
    if string=="0":
        break
    encoded=encoder(string, omit_ones=True)
    print(encoded)


