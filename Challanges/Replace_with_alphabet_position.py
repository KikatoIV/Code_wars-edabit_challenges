def alphabet_position(text):
    new_text = text.lower()
    last_text = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pairs = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    for x in new_text:
        if x in alphabet:
            last_text.append(x)
    return ' '.join(pairs[x] for x in last_text)

    
print(alphabet_position('Nine years'))

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()) 