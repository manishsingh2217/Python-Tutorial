sentence= '''Hello My name is  Manish singh I am the learning Python'''


if("  " in sentence):
    print("Double space is present at ",sentence.find("  "))
    
# removing double space with single space
sR=sentence.replace("  ", " ")
bool=print("  " in sentence.replace("  "," "))