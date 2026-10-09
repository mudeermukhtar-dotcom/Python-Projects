import random
choice=["->YOU WANT TO ENOCE OR DECODE " , "A" , "B"]
print(choice[0])
print("A.ENCODE "          "B. DECODE".center(30))
choose=input("CHOOSE ANY ONE OF THEM :".center(30)).upper()
if choose == "A" or choose == "1":
  user = str(input("ENTER THE SENTENCE YOU WANT TO ENCODE : "))
  words = user.split()
  encoded_words = []
  for i in words:
     word=i
     if len(i) <= 3:
        word = i[::-1]
        encoded_words.append(word)
     else: 
        lists=[]
        liste=[]
        word=i[1:]+i[0]  
        for k in range(0,3):
            x=random.choice("abcdefghijklmnopqrstuvwxyz")
            lists.append(x)
            results="".join(lists)
            
             
        for w in range(0,3):
            y=random.choice("abcdefghijklmnopqrstuvwxyz")
            liste.append(y)
            resulte="".join(liste)
        final=results+word+resulte
        encoded_words.append(final)
  print(" ".join(encoded_words))
        
elif choose == "B" or choose == "2" :
    user = input("ENTER THE SENTENCE YOU WANT TO DECODE :")
    raw_form = user.split()
    decode_form = []
    for i in raw_form:
     if len(str(i)) <= 3:
        word = i[::-1]
        decode_form.append(word)
     else:
        g_word=i
        g_word = g_word[3:] 
        g_word=g_word[:-3]
        new_word=g_word[-1]+g_word[:-1]
        decode_form.append(new_word)
        
    decode_word=" ".join(decode_form)
    print(decode_word)        
   


