import csv
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer


def sentiment_analysis(sentence):
    blob = TextBlob(sentence, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    
    if blob.sentiment[0] > 0:
        return 'positive'
    elif blob.sentiment[0] == 0:
        return 'neutral'
    else:
        return 'negative'


capitale = ""
pays = ""
sentiment = ""


prenom = input("\nEntres ton prénom: ")

while(capitale == "") :
    lieu = input("Entres ton pays: ")

    with open('listePays.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            element = row[0]
            element = element.split(";")
            if element[0] == lieu or element[1] == lieu or element[2] == lieu or element[4] == lieu :
                pays = element[0]
                capitale = element[5]
                determinant = element[3]
    
    if capitale == "" :
        print("\nJe ne connais pas ce pays,", lieu, "existe-t-il réellement ?")


if determinant == "le" :
    print("\nBonjour", prenom,", Je vois que tu habites au", pays, ".")
elif determinant == "les" :
    print("\nBonjour", prenom,", Je vois que tu habites aux", pays, ".")
else :
    print("\nBonjour", prenom,", Je vois que tu habites en", pays, ".")


print("Comment trouves tu la capitale de ton pays ?")
print(capitale, "est-elle une jolie ville ?\n")

answer = input()
sentiment = sentiment_analysis(answer)

if sentiment == "positive" :
    print("\nJe suis content que tu trouves", capitale, "jolie.")
elif sentiment == "neutral" :
    print("\nIntéressant.")
else :
    print("\nJe suis désolé que tu ne trouves pas", capitale, "jolie.")

print()


    


