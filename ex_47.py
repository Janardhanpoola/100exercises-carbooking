from collections import Counter




def character_set(lst,letter):
    
    for word in lst:
        value=1
        word_dict=Counter(word) 
        #print(word_dict)     
        for l in word_dict:
            
            
            if l not in letter:
                value=0
        if value==1:
            print(word)


lst = ['fat','tap','day','fun','man','ant','bag','aim']
letter = ['m','e','d','f','a','p','y','i','b','a','g']
(character_set(lst, letter))