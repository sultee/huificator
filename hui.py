# -*- coding: utf8 -*-

word = raw_input("Enter word: ")
uword = word.decode('utf8')

#print type (uword)

letter = 0
slogi = []
range = 0

slovar = [[u"а", u"я"], [u"я", u"я"], [u"е", "е"], [u"о", u"е"], [u"и", u"и"], [u"ё", u"ё"], [u"ы", u"и"], [u"ю", u"ю"], [u"у", u"ю"]]


for i in uword:
    #print type(i)
    #letter = unicode(i, "utf-8", errors="ignore")
    #print letter
    #print type(range)
    #print type(letter)
    if i == u"а" or i== u"е" or i== u"ё" or i== u"и" or i== u"о" or i== u"у" or i== u"э" or i== u"ю" or i==u"ы" or i== u"я":
        slogi.append(uword[range: letter+1])
        range=letter+1
    letter +=1
slogi.append(uword[range:])

sloge = [x for x in slogi if x]
#print sloge

endword = u"ху"
endbutton = u"е"

if len(sloge) < 4:
    for l in sloge[0][0:]:
        for m in slovar:
            #print m[0]
            if l==m[0]:
                endbutton = m[1]
        #print endbutton
    endword +=endbutton
    for k in sloge[1:]:
        endword = endword + k
if len(sloge) >3:
    for l in sloge[1][0:]:
        for m in slovar:
            #print m[0]
            if l==m[0]:
                endbutton = m[1]
    #print endbutton
    #print endword
    endword +=endbutton
    for k in sloge[2:]:
        endword = endword + k

print endword

#for k in sloge:
#    print k

