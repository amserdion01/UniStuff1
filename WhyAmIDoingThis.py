from textblob import TextBlob as GoogleTranslate    #pip install textblob for whoever wants to use this program
from CommonWords import CommonWords

#EDIT THE VARIABLE Letter. LANGUAGE DOES NOT MATTER
Letter = "Buna Mos Craciun, Apropo, ma cheama Alex Alexandru Si De Craciun As Dori Un Ford Verde. Tatal meu se numeste Louis Grozav si poti sa ma gasesti Pe Strada Ceahlaului Nr 555, Ap 4, Scara A. Te Astept!!  Multumesc!"
Letter2 = "My name is George , I am 11 years old and I live on Nordalveien 11 in Oslo, Norway and this year I’ve been really nice! For Christmas I would like a pretty red race car and a ton of sweets.Thank you so much!!!"
Letter1 = "Draga mosule , ma numesc Popescu Levi si am 12 ani.Cadoul de anul trecut mi-a placut foarte mult , acum te rog sa mi aduci o masina cu telecomanda."

try:
    _Letter = GoogleTranslate(Letter)
    LetterInEN = _Letter.translate(to='en')
    print(LetterInEN)
except:
    LetterInEN = Letter
    print(LetterInEN)

Name = ""
Location = ""
Wish = ""

LetterInEN = LetterInEN.replace("really",'')
LetterInEN = LetterInEN.replace(",",', ').replace(".",'. ').replace("!",'! ')
LetterInEN = LetterInEN.replace(",  ",', ').replace(".  ",'. ').replace("!  ",'! ')

for i in range (len(LetterInEN.split())):

    tempword = LetterInEN.split()[i].lower().replace(',',"").replace('.',"").replace('!',"")
    # print (tempword)

    if tempword == "i'm" and LetterInEN.split()[i+1][0].isupper():
         swName = 1
         j = 1
         while swName == 1:
             if LetterInEN.split()[i+j][0].isupper() and LetterInEN.split()[i+j].lower().replace(',',"").replace('.',"").replace('!',"") not in CommonWords:
                 Name = Name + LetterInEN.split()[i+j].replace(',',"").replace('.',"").replace('!',"") + " "
             else:
                 swName = 0
             j+=1

    if tempword == "is" and LetterInEN.split()[i+1][0].isupper() and LetterInEN.split()[i-1].lower().replace(',',"").replace('.',"").replace('!',"") == "name" and LetterInEN.split()[i-2].lower().replace(',',"").replace('.',"").replace('!',"") == "my":
         swName = 1
         j = 1
         while swName == 1:
             if LetterInEN.split()[i+j][0].isupper() and LetterInEN.split()[i+j].lower().replace(',',"").replace('.',"").replace('!',"") not in CommonWords:
                 Name = Name + LetterInEN.split()[i+j].replace(',',"").replace('.',"").replace('!',"") + " "
             else:
                 swName = 0
             j+=1


    if ((tempword == "want") or (tempword == "for") or (tempword == "love") or (tempword == "like")) and ((LetterInEN.split()[i-1].lower().replace(',',"").replace('.',"").replace('!',"") == "would") or (LetterInEN.split()[i-1].lower().replace(',',"").replace('.',"").replace('!',"") == "wish")):
       swGift = 1
       j = 1
       while swGift == 1:
            if ((((LetterInEN.split()[i+j][len(LetterInEN.split()[i+j])-1::]) == "." or (LetterInEN.split()[i+j][len(LetterInEN.split()[i+j])-1::] == "!")) or ((LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "thank") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "thanks") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "please")))):
               swGift = 0
            Wish = Wish+LetterInEN.split()[i+j].replace(',',"").replace('.',"").replace('!',"") + " "
            j+=1

    if ((tempword == "me") and ((LetterInEN.split()[i-1].replace(',',"").replace('.',"").replace('!',"").lower()) == "bring" or (LetterInEN.split()[i-1].replace(',',"").replace('.',"").replace('!',"").lower() == "give"))):
       swGift = 1
       j = 1
       while swGift == 1:
            if ((((LetterInEN.split()[i+j][len(LetterInEN.split()[i+j])-1::]) == "." or (LetterInEN.split()[i+j][len(LetterInEN.split()[i+j])-1::] == "!")) or ((LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "thank") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "thanks") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "please")))):
               swGift = 0
            Wish = Wish+LetterInEN.split()[i+j].replace(',',"").replace('.',"").replace('!',"") + " "
            j+=1



    if (tempword == "live") or (((tempword == "at") or (tempword == "on")) and (LetterInEN.split()[i-1].replace(',',"").replace('.',"").replace('!',"").lower() == "found")) or (((tempword == "at") or (tempword == "on")) and (LetterInEN.split()[i-1].replace(',',"").replace('.',"").replace('!',"").lower() == "me") and (LetterInEN.split()[i-2].replace(',',"").replace('.',"").replace('!',"").lower() == "find")):
        swPlace = 1
        j = 1
        while swPlace == 1:
            if LetterInEN.split()[i+j][len(LetterInEN.split()[i+j])-1::] == "." or ((LetterInEN.split()[i+j][len(LetterInEN.split()[i+j])-1::]) == "!") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "thank") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "and") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "please") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "this") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "I") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "I'm") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "I' m") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "I've") or (LetterInEN.split()[i+j+1].replace(',',"").replace('.',"").replace('!',"").lower() == "I' ve"):
                swPlace = 0
            Location = Location + LetterInEN.split()[i+j].replace(',',"").replace('.',"").replace('!',"") + " "
            j+=1


print ("\n\n\nName:" ,Name.strip())
print ("Wish:" ,Wish.strip())
print ("Lives:", Location.strip())


