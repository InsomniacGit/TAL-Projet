import csv
from textblob import TextBlob
from textblob.taggers import PatternTagger
from textblob.sentiments import PatternAnalyzer
import nltk
from nltk.corpus import wordnet
import random


# Fonction commencant la discution avec l'utilisateur
def startConversation() :
    capitale = ""
    pays = ""
    sentiment = ""

    prenom = input("Enter your surname please: ")

    while(prenom == "") :
        prenom = input("Come on, don't be shy. Enter your surname please: ")
    
    prenom = prenom[0].upper() + prenom[1:].lower()

    lieu = input("Enter your country of residence please: ")

    while(capitale == "") :

        while(lieu == "") :
            lieu = input("I'm not gonna eat you. Enter your country of residence please: ")
        
        lieu = lieu[0].upper() + lieu[1:].lower()


        with open('country.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                # print(row)
                if row[0] == lieu :
                    pays = row[0]
                    capitale = row[1]
        
        if capitale == "" :
            print("\nI don't know this country, does", lieu, "really exist ?")
            lieu = input("Enter your country of residence please: ")

    print("\nHello", prenom, "! I'm glad to meet you.")
    print("You are from", pays, "right ?")
    print("How do you find the capital of your country ?")
    print("Is", capitale, "a nice city ?\n")

    answer = input()
    analyse_phrase(answer)

    sentiment = sentiment_analysis(answer)

    if sentiment == "positive" :
        print("\nI'm glad you find", capitale, "nice.")
        print("What do you like in this city ?\n")
    elif sentiment == "neutral" :
        print("\nInteresting.")
        print("Is there something you like or dislike in this city ?\n")
    else :
        print("\nI'm sorry you don't find", capitale, "nice.")
        print("What do you dislike about this city ?\n")
    
    return prenom


# Fonction qui analyse le sentiment d'une phrase écrite en anglais
def sentiment_analysis(phrase) :
    blob = TextBlob(phrase, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    if blob.sentiment.polarity > 0 :
        return "positive"
    elif blob.sentiment.polarity == 0 :
        return "neutral"
    else :
        return "negative"


# Fonction qui analyse une phrase écrite en anglais
def analyse_phrase(answer) :

    # https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
    # CC: conjunction, coordinating
    # CD: numeral, cardinal
    # DT: determiner
    # EX: existential there
    # IN: preposition or conjunction, subordinating
    # JJ: adjective or numeral, ordinal
    # JJR: adjective, comparative
    # JJS: adjective, superlative
    # LS: list item marker
    # MD: modal auxiliary
    # NN: noun, common, singular or mass
    # NNP: noun, proper, singular
    # NNS: noun, common, plural
    # PDT: pre-determiner
    # POS: genitive marker
    # PRP: pronoun, personal
    # PRP$: pronoun, possessive
    # RB: adverb
    # RBR: adverb, comparative
    # RBS: adverb, superlative
    # RP: particle
    # TO: "to" as preposition or infinitive marker
    # UH: interjection
    # VB: verb, base form
    # VBD: verb, past tense
    # VBG: verb, present participle or gerund
    # VBN: verb, past participle
    # VBP: verb, present tense, not 3rd person singular
    # VBZ: verb, present tense, 3rd person singular
    # WDT: WH-determiner
    # WP: WH-pronoun
    # WRB: Wh-adverb

    # Tokenisez le texte en mots
    words = nltk.word_tokenize(answer)

    # Taguez les mots avec leur partie de discours
    tagged_words = nltk.pos_tag(words)

    # Créez un objet WordNetLemmatizer
    lemmatizer = nltk.WordNetLemmatizer()

    # Parcourez la liste de mots taggés
    for word, tag in tagged_words:

        # print(word, tag)

        # Récupérez la partie de discours du mot
        pos = tag[0].lower()

        # print(pos)
        
        # Vérifiez si la partie de discours est un nom
        # n = nom, v = verbe, j = adjectif, r = adverbe
        if pos in ["n", "v", "j", "r"]:

            # Si le mot est un adjectif, lemmatisez-le comme un adjectif
            if pos == "j":
                pos = "a"

            # Lemmatisez le mot en fonction de sa partie de discours
            lemma = lemmatizer.lemmatize(word, pos)
            # Vérifiez si le lemme est présent dans WordNet
            lemmas = wordnet.lemmas(lemma)
            
            if lemmas:
                sport = wordnet.synset("sport.n.01")
                religion = wordnet.synset("religion.n.01")
                art = wordnet.synset("art.n.01")
                philosophy = wordnet.synset("philosophy.n.01")
                politics = wordnet.synset("politics.n.01")
                food = wordnet.synset("food.n.01")
                clothes = wordnet.synset("clothes.n.01")
                music = wordnet.synset("music.n.01")
                travel = wordnet.synset("travel.n.01")
                botany = wordnet.synset("botany.n.01")
                lifestyle = wordnet.synset("lifestyle.n.01")
                vice = wordnet.synset("vice.n.01")
                science = wordnet.synset("science.n.01")
                technology = wordnet.synset("technology.n.01")
                history = wordnet.synset("history.n.01")
                literature = wordnet.synset("literature.n.01")
                geography = wordnet.synset("geography.n.01")
                economy = wordnet.synset("economy.n.01")
                law = wordnet.synset("law.n.01")
                education = wordnet.synset("education.n.01")
                medicine = wordnet.synset("medicine.n.01")
                psychology = wordnet.synset("psychology.n.01")
                sociology = wordnet.synset("sociology.n.01")
                association = wordnet.synset("association.n.01")
                makeup = wordnet.synset("makeup.n.01")
                computer = wordnet.synset("computer.n.01")
                pet = wordnet.synset("pet.n.01")


                

                try :
                    lemma_synset = wordnet.synset(f"{lemma}.{pos}.01")
                
                    similaritySport = sport.path_similarity(lemma_synset)
                    similarityReligion = religion.path_similarity(lemma_synset)
                    similarityArt = art.path_similarity(lemma_synset)
                    similarityPhilosophy = philosophy.path_similarity(lemma_synset)
                    similarityPolitics = politics.path_similarity(lemma_synset)
                    similarityFood = food.path_similarity(lemma_synset)
                    similarityClothes = clothes.path_similarity(lemma_synset)
                    similarityMusic = music.path_similarity(lemma_synset)
                    similarityTravel = travel.path_similarity(lemma_synset)
                    similarityBotany = botany.path_similarity(lemma_synset)
                    similarityLifestyle = lifestyle.path_similarity(lemma_synset)
                    similarityVice = vice.path_similarity(lemma_synset)
                    similarityScience = science.path_similarity(lemma_synset)
                    similarityTechnology = technology.path_similarity(lemma_synset)
                    similarityHistory = history.path_similarity(lemma_synset)
                    similarityLiterature = literature.path_similarity(lemma_synset)
                    similarityGeography = geography.path_similarity(lemma_synset)
                    similarityEconomy = economy.path_similarity(lemma_synset)
                    similarityLaw = law.path_similarity(lemma_synset)
                    similarityEducation = education.path_similarity(lemma_synset)
                    similarityMedicine = medicine.path_similarity(lemma_synset)
                    similarityPsychology = psychology.path_similarity(lemma_synset)
                    similaritySociology = sociology.path_similarity(lemma_synset)
                    similarityAssociation = association.path_similarity(lemma_synset)
                    similarityMakeup = makeup.path_similarity(lemma_synset)
                    similarityComputer = computer.path_similarity(lemma_synset)
                    similarityPet = pet.path_similarity(lemma_synset)
                    

                    if similaritySport > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in sportTab and lemma != "practice" and lemma != "i" :
                            sportTab.append(lemma)
                            # print(f"'{lemma}' = {similaritySport:.2f} sport")
                        # print(sportTab)

                    if similarityReligion > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in religionTab and lemma != "i" :
                            religionTab.append(lemma)
                            # print(f"'{lemma}' = {similarityReligion:.2f} religion")
                        # print(religionTab)

                    if similarityArt > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in artTab and lemma != "i" :
                            artTab.append(lemma)
                            # print(f"'{lemma}' = {similarityArt:.2f} art")
                        # print(artTab)
                    
                    if similarityPhilosophy > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in philosophyTab and lemma != "i" :
                            philosophyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityPhilosophy:.2f} philosophy")
                        # print(philosophyTab)
                    
                    if similarityPolitics > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in politicsTab and lemma != "i" :
                            politicsTab.append(lemma)
                            # print(f"'{lemma}' = {similarityPolitics:.2f} politics")
                        # print(politicsTab)
                    
                    if similarityFood > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in foodTab and lemma != "i":
                            foodTab.append(lemma)
                            # print(f"'{lemma}' = {similarityFood:.2f} food")
                        # print(foodTab)
                    
                    if similarityClothes > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in clothesTab and lemma != "i" :
                            clothesTab.append(lemma)
                            # print(f"'{lemma}' = {similarityClothes:.2f} clothes")
                        # print(clothesTab)
                    
                    if similarityMusic > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in musicTab and lemma != "i" :
                            musicTab.append(lemma)
                            # print(f"'{lemma}' = {similarityMusic:.2f} music")
                        # print(musicTab)
                    
                    if similarityTravel > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in travelTab and lemma != "i" :
                            travelTab.append(lemma)
                            # print(f"'{lemma}' = {similarityTravel:.2f} travel")
                        # print(travelTab)
                    
                    if similarityBotany > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in botanyTab and lemma != "i" :
                            botanyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityBotany:.2f} botany")
                        # print(botanyTab)
                    
                    if similarityLifestyle > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in lifestyleTab and lemma != "i" :
                            lifestyleTab.append(lemma)
                            # print(f"'{lemma}' = {similarityLifestyle:.2f} lifestyle")
                        # print(lifestyleTab)
                    
                    if similarityVice > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in viceTab and lemma != "i" :
                            viceTab.append(lemma)
                            # print(f"'{lemma}' = {similarityVice:.2f} vice")
                        # print(viceTab)
                    
                    if similarityScience > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in scienceTab and lemma != "i" :
                            scienceTab.append(lemma)
                            # print(f"'{lemma}' = {similarityScience:.2f} science")
                        # print(scienceTab)
                    
                    if similarityTechnology > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in technologyTab and lemma != "i" :
                            technologyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityTechnology:.2f} technology")
                        # print(technologyTab)
                    
                    if similarityHistory > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in historyTab and lemma != "i" :
                            historyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityHistory:.2f} history")
                        # print(historyTab)
                    
                    if similarityLiterature > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in literatureTab and lemma != "i" :
                            literatureTab.append(lemma)
                            # print(f"'{lemma}' = {similarityLiterature:.2f} literature")
                        # print(literatureTab)
                    
                    if similarityGeography > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in geographyTab and lemma != "i" :
                            geographyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityGeography:.2f} geography")
                        # print(geographyTab)
                    
                    if similarityLaw > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in lawTab and lemma != "i" :
                            lawTab.append(lemma)
                            # print(f"'{lemma}' = {similarityLaw:.2f} law")
                        # print(lawTab)
                    
                    if similarityPsychology > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in psychologyTab and lemma != "i" :
                            psychologyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityPsychology:.2f} psychology")
                        # print(psychologyTab)
                    
                    if similarityEconomy > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in economyTab and lemma != "i" :
                            economyTab.append(lemma)
                            # print(f"'{lemma}' = {similarityEconomy:.2f} economy")
                        # print(economyTab)
                    
                    if similarityMedicine > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in medicineTab and lemma != "i" :
                            medicineTab.append(lemma)
                            # print(f"'{lemma}' = {similarityMedicine:.2f} medicine")
                        # print(medicineTab)
                    
                    if similarityEducation > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in educationTab and lemma != "i" :
                            educationTab.append(lemma)
                            # print(f"'{lemma}' = {similarityEducation:.2f} education")
                        # print(educationTab)
                    
                    if similaritySociology > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in sociologyTab and lemma != "i" :
                            sociologyTab.append(lemma)
                            # print(f"'{lemma}' = {similaritySociology:.2f} sociology")
                        # print(sociologyTab)
                    
                    if similarityAssociation > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in associationTab and lemma != "i" :
                            associationTab.append(lemma)
                            # print(f"'{lemma}' = {similarityAssociation:.2f} association")
                        # print(associationTab)
                    
                    if similarityMakeup > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in makeupTab and lemma != "i" :
                            makeupTab.append(lemma)
                            # print(f"'{lemma}' = {similarityMakeup:.2f} makeup")
                        # print(makeupTab)
                    
                    if similarityComputer > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in computerTab and lemma != "i" :
                            computerTab.append(lemma)
                            # print(f"'{lemma}' = {similarityComputer:.2f} computer")
                        # print(computerTab)
                    
                    if similarityPet > 0.15:
                        # Verifie si le lemma n'est pas déjà dans le tableau
                        if lemma not in petTab and lemma != "i":
                            petTab.append(lemma)
                            # print(f"'{lemma}' = {similarityPet:.2f} pet")
                        # print(petTab)
                except:
                    pass
                      
        #     else:
        #         print(f"'{lemma}' n'est pas présent dans WordNet.")
        # else:
        #     print(f"'{word}' n'est pas un nom, un verbe, un adjectif ou un adverbe.")



# Function qui créé une question en anglais a partir des mots clés présents dans le tableau sportTab
def create_sport_question() :
    question = "Do you like sport ? Do you practice "

    for i in range(len(sportTab)) :
        question += sportTab[i]
        if i == len(sportTab) - 2 :
            question += " and "
        elif i < len(sportTab) - 1 :
            question += ", "
        else :
            question += " ?\n"

    sportTab.clear()
    return question

# Function qui créé une question en anglais a partir des mots clés présents dans le tableau religionTab
def create_religion_question() :
    question = "Are you religious ? Do you trust in "

    for i in range(len(religionTab)) :
        question += religionTab[i]
        if i == len(religionTab) - 2 :
            question += " and "
        elif i < len(religionTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    religionTab.clear()
    return question

# Function qui créé une question en anglais a partir des mots clés présents dans le tableau artTab
def create_art_question() :
    question = "Do you have the soul of an artist ? Are you interested in "

    for i in range(len(artTab)) :
        question += artTab[i]
        if i == len(artTab) - 2 :
            question += " and "
        elif i < len(artTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    artTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau philosophyTab
def create_philosophy_question() :
    question = "Do you like philosophy ? Have you already think about "

    for i in range(len(philosophyTab)) :
        question += philosophyTab[i]
        if i == len(philosophyTab) - 2 :
            question += " and "
        elif i < len(philosophyTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    philosophyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau politicsTab
def create_politics_question() :
    question = "Are you interested in politics ? What do you think about "

    for i in range(len(politicsTab)) :
        question += politicsTab[i]
        if i == len(politicsTab) - 2 :
            question += " and "
        elif i < len(politicsTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    politicsTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau foodTab
def create_food_question() :
    question = "Do you like food ? Would you take "

    for i in range(len(foodTab)) :
        question += foodTab[i]
        if i == len(foodTab) - 2 :
            question += " and "
        elif i < len(foodTab) - 1 :
            question += ", "
        else :
            question += " right now ?\n"
    
    foodTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau clothesTab
def create_clothes_question() :
    question = "Are you interested in clothes or fashion ? Are you wearing "

    for i in range(len(clothesTab)) :
        question += clothesTab[i]
        if i == len(clothesTab) - 2 :
            question += " and "
        elif i < len(clothesTab) - 1 :
            question += ", "
        else :
            question += " sometimes ?\n"
    
    clothesTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau travelTab
def create_travel_question() :
    question = "Are you a traveler ? Do you love "

    for i in range(len(travelTab)) :
        question += travelTab[i]
        if i == len(travelTab) - 2 :
            question += " and "
        elif i < len(travelTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    travelTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau musicTab
def create_music_question() :
    question = "Are you often listening to music ? Do you love "

    for i in range(len(musicTab)) :
        question += musicTab[i]
        if i == len(musicTab) - 2 :
            question += " and "
        elif i < len(musicTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    musicTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau botanyTab
def create_botany_question() :
    question = "Have you got green-fingered ? Is "

    for i in range(len(botanyTab)) :
        question += botanyTab[i]
        if i == len(botanyTab) - 2 :
            question += " and "
        elif i < len(botanyTab) - 1 :
            question += ", "
        else :
            question += " interest you ?\n"
    
    botanyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau geographyTab
def create_geography_question() :
    question = "Do you like geography ? Things like "

    for i in range(len(geographyTab)) :
        question += geographyTab[i]
        if i == len(geographyTab) - 2 :
            question += " and "
        elif i < len(geographyTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    geographyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau historyTab
def create_history_question() :
    question = "Are you interested in history ? Have you heard about "

    for i in range(len(historyTab)) :
        question += historyTab[i]
        if i == len(historyTab) - 2 :
            question += " and "
        elif i < len(historyTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    historyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau literatureTab
def create_literature_question() :
    question = "Do you read books ? Do you love "

    for i in range(len(literatureTab)) :
        question += literatureTab[i]
        if i == len(literatureTab) - 2 :
            question += " and "
        elif i < len(literatureTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    literatureTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau scienceTab
def create_science_question() :
    question = "Do you have a scientific mind ? Are you interested in "

    for i in range(len(scienceTab)) :
        question += scienceTab[i]
        if i == len(scienceTab) - 2 :
            question += " and "
        elif i < len(scienceTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    scienceTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau technologyTab
def create_technology_question() :
    question = "Are you passionnate about technology ? Is "

    for i in range(len(technologyTab)) :
        question += technologyTab[i]
        if i == len(technologyTab) - 2 :
            question += " and "
        elif i < len(technologyTab) - 1 :
            question += ", "
        else :
            question += " attract you ?\n"
    
    technologyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau lifestyleTab
def create_lifestyle_question() :
    question = "Have you got a special lifestyle ? Do you love "

    for i in range(len(lifestyleTab)) :
        question += lifestyleTab[i]
        if i == len(lifestyleTab) - 2 :
            question += " and "
        elif i < len(lifestyleTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    lifestyleTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau viceTab
def create_vice_question() :
    question = "Have you got vices ? Are you trying to change "

    for i in range(len(viceTab)) :
        question += viceTab[i]
        if i == len(viceTab) - 2 :
            question += " and "
        elif i < len(viceTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    viceTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau economyTab
def create_economy_question() :
    question = "What's your thoughts on the current state of the economy ? Are you concerned about "

    for i in range(len(economyTab)) :
        question += economyTab[i]
        if i == len(economyTab) - 2 :
            question += " and "
        elif i < len(economyTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    economyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau lawTab
def create_law_question() :
    question = "Have you ever had any legal problems ? What do you think about "

    for i in range(len(lawTab)) :
        question += lawTab[i]
        if i == len(lawTab) - 2 :
            question += " and "
        elif i < len(lawTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    lawTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau educationTab
def create_education_question() :
    question = "Do you like school ? Do you love "

    for i in range(len(educationTab)) :
        question += educationTab[i]
        if i == len(educationTab) - 2 :
            question += " and "
        elif i < len(educationTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    educationTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau medicineTab
def create_medicine_question() :
    question = "Do you like medicine ? Are you attract by "

    for i in range(len(medicineTab)) :
        question += medicineTab[i]
        if i == len(medicineTab) - 2 :
            question += " and "
        elif i < len(medicineTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    medicineTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau psychologyTab
def create_psychology_question() :
    question = "Are you interested by psychology ? Things like "

    for i in range(len(psychologyTab)) :
        question += psychologyTab[i]
        if i == len(psychologyTab) - 2 :
            question += " and "
        elif i < len(psychologyTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    psychologyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau sociologyTab
def create_sociology_question() :
    question = "Are you social or shy ? Do you love "

    for i in range(len(sociologyTab)) :
        question += sociologyTab[i]
        if i == len(sociologyTab) - 2 :
            question += " and "
        elif i < len(sociologyTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    sociologyTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau associationTab
def create_association_question() :
    question = "Have you ever volunteered for an association ? Do you like "

    for i in range(len(associationTab)) :
        question += associationTab[i]
        if i == len(associationTab) - 2 :
            question += " and "
        elif i < len(associationTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    associationTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau makeupTab
def create_makeup_question() :
    question = "Do you use makeup ? Things like "

    for i in range(len(makeupTab)) :
        question += makeupTab[i]
        if i == len(makeupTab) - 2 :
            question += " and "
        elif i < len(makeupTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    makeupTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau computerTab
def create_computer_question() :
    question = "Are you confortable with a computer ? Do you use "

    for i in range(len(computerTab)) :
        question += computerTab[i]
        if i == len(computerTab) - 2 :
            question += " and "
        elif i < len(computerTab) - 1 :
            question += ", "
        else :
            question += " often ?\n"
    
    computerTab.clear()
    return question

# Fonction qui ajoute une question avec les mots clés présents dans le tableau petTab
def create_pet_question() :
    question = "Have you got a pet ? Do you love "

    for i in range(len(petTab)) :
        question += petTab[i]
        if i == len(petTab) - 2 :
            question += " and "
        elif i < len(petTab) - 1 :
            question += ", "
        else :
            question += " ?\n"
    
    petTab.clear()
    return question



# Fonction qui gère les questions
def question_add() :
    # print(len(generalQuestion))

    if len(sportTab) > 0 and askedQuestion[0] == False :
        questionTab.append([create_sport_question(), "sport"])
        askedQuestion[0] = True
        if generalQuestion[0] in generalQuestionTab :
            elementRemove = generalQuestion[0]
            generalQuestionTab.remove(elementRemove)
    
    if len(religionTab) > 0 and askedQuestion[1] == False :
        questionTab.append([create_religion_question(), "religion"])
        askedQuestion[1] = True
        if generalQuestion[1] in generalQuestionTab :
            elementRemove = generalQuestion[1]
            generalQuestionTab.remove(elementRemove)

    if len(artTab) > 0 and askedQuestion[2] == False:
        questionTab.append([create_art_question(), "art"])
        askedQuestion[2] = True
        if generalQuestion[2] in generalQuestionTab :
            elementRemove = generalQuestion[2]
            generalQuestionTab.remove(elementRemove)
    
    if len(philosophyTab) > 0 and askedQuestion[3] == False:
        questionTab.append([create_philosophy_question(), "philosophy"])
        askedQuestion[3] = True
        if generalQuestion[3] in generalQuestionTab :
            elementRemove = generalQuestion[3]
            generalQuestionTab.remove(elementRemove)
    
    if len(politicsTab) > 0 and askedQuestion[4] == False:
        questionTab.append([create_politics_question(), "politics"])
        askedQuestion[4] = True
        if generalQuestion[4] in generalQuestionTab :
            elementRemove = generalQuestion[4]
            generalQuestionTab.remove(elementRemove)
    
    if len(foodTab) > 0 and askedQuestion[5] == False:
        questionTab.append([create_food_question(), "food"])
        askedQuestion[5] = True
        if generalQuestion[5] in generalQuestionTab :
            elementRemove = generalQuestion[5]
            generalQuestionTab.remove(elementRemove)
    
    if len(clothesTab) > 0 and askedQuestion[6] == False:
        questionTab.append([create_clothes_question(), "clothes"])
        askedQuestion[6] = True
        if generalQuestion[6] in generalQuestionTab :
            elementRemove = generalQuestion[6]
            generalQuestionTab.remove(elementRemove)
    
    if len(travelTab) > 0 and askedQuestion[7] == False:
        questionTab.append([create_travel_question(), "travel"])
        askedQuestion[7] = True
        if generalQuestion[7] in generalQuestionTab :
            elementRemove = generalQuestion[7]
            generalQuestionTab.remove(elementRemove)
    
    if len(musicTab) > 0 and askedQuestion[8] == False:
        questionTab.append([create_music_question(), "music"])
        askedQuestion[8] = True
        if generalQuestion[8] in generalQuestionTab :
            elementRemove = generalQuestion[8]
            generalQuestionTab.remove(elementRemove)
    
    if len(botanyTab) > 0 and askedQuestion[9] == False:
        questionTab.append([create_botany_question(), "botany"])
        askedQuestion[9] = True
        if generalQuestion[9] in generalQuestionTab :
            elementRemove = generalQuestion[9]
            generalQuestionTab.remove(elementRemove)
    
    if len(lifestyleTab) > 0 and askedQuestion[10] == False:
        questionTab.append([create_lifestyle_question(), "lifestyle"])
        askedQuestion[10] = True
        if generalQuestion[10] in generalQuestionTab :
            elementRemove = generalQuestion[10]
            generalQuestionTab.remove(elementRemove)
    
    if len(viceTab) > 0 and askedQuestion[11] == False:
        questionTab.append([create_vice_question(), "vice"])
        askedQuestion[11] = True
        if generalQuestion[11] in generalQuestionTab :
            elementRemove = generalQuestion[11]
            generalQuestionTab.remove(elementRemove)
    
    if len(scienceTab) > 0 and askedQuestion[12] == False:
        questionTab.append([create_science_question(), "science"])
        askedQuestion[12] = True
        if generalQuestion[12] in generalQuestionTab :
            elementRemove = generalQuestion[12]
            generalQuestionTab.remove(elementRemove)
    
    if len(technologyTab) > 0 and askedQuestion[13] == False:
        questionTab.append([create_technology_question(), "technology"])
        askedQuestion[13] = True
        if generalQuestion[13] in generalQuestionTab :
            elementRemove = generalQuestion[13]
            generalQuestionTab.remove(elementRemove)
    
    if len(historyTab) > 0 and askedQuestion[14] == False:
        questionTab.append([create_history_question(), "history"])
        askedQuestion[14] = True
        if generalQuestion[14] in generalQuestionTab :
            elementRemove = generalQuestion[14]
            generalQuestionTab.remove(elementRemove)

    if len(literatureTab) > 0 and askedQuestion[15] == False:
        questionTab.append([create_literature_question(), "literature"])
        askedQuestion[15] = True
        if generalQuestion[15] in generalQuestionTab :
            elementRemove = generalQuestion[15]
            generalQuestionTab.remove(elementRemove)
    
    if len(geographyTab) > 0 and askedQuestion[16] == False:
        questionTab.append([create_geography_question(), "geography"])
        askedQuestion[16] = True
        if generalQuestion[16] in generalQuestionTab :
            elementRemove = generalQuestion[16]
            generalQuestionTab.remove(elementRemove)
    
    if len(economyTab) > 0 and askedQuestion[17] == False:
        questionTab.append([create_economy_question(), "economy"])
        askedQuestion[17] = True
        if generalQuestion[17] in generalQuestionTab :
            elementRemove = generalQuestion[17]
            generalQuestionTab.remove(elementRemove)
    
    if len(lawTab) > 0 and askedQuestion[18] == False:
        questionTab.append([create_law_question(), "law"])
        askedQuestion[18] = True
        if generalQuestion[18] in generalQuestionTab :
            elementRemove = generalQuestion[18]
            generalQuestionTab.remove(elementRemove)
    
    if len(educationTab) > 0 and askedQuestion[19] == False:
        questionTab.append([create_education_question(), "education"])
        askedQuestion[19] = True
        if generalQuestion[19] in generalQuestionTab :
            elementRemove = generalQuestion[19]
            generalQuestionTab.remove(elementRemove)
    
    if len(medicineTab) > 0 and askedQuestion[20] == False:
        questionTab.append([create_medicine_question(), "medicine"])
        askedQuestion[20] = True
        if generalQuestion[20] in generalQuestionTab :
            elementRemove = generalQuestion[20]
            generalQuestionTab.remove(elementRemove)
    
    if len(psychologyTab) > 0 and askedQuestion[21] == False:
        questionTab.append([create_psychology_question(), "psychology"])
        askedQuestion[21] = True
        if generalQuestion[21] in generalQuestionTab :
            elementRemove = generalQuestion[21]
            generalQuestionTab.remove(elementRemove)
    
    if len(sociologyTab) > 0 and askedQuestion[22] == False:
        questionTab.append([create_sociology_question(), "sociology"])
        askedQuestion[22] = True
        if generalQuestion[22] in generalQuestionTab :
            elementRemove = generalQuestion[22]
            generalQuestionTab.remove(elementRemove)
    
    if len(associationTab) > 0 and askedQuestion[23] == False:
        questionTab.append([create_association_question(), "association"])
        askedQuestion[23] = True
        if generalQuestion[23] in generalQuestionTab :
            elementRemove = generalQuestion[23]
            generalQuestionTab.remove(elementRemove)
    
    if len(makeupTab) > 0 and askedQuestion[24] == False:
        questionTab.append([create_makeup_question(), "makeup"])
        askedQuestion[24] = True
        if generalQuestion[24] in generalQuestionTab :
            elementRemove = generalQuestion[24]
            generalQuestionTab.remove(elementRemove)
    
    if len(computerTab) > 0 and askedQuestion[25] == False:
        questionTab.append([create_computer_question(), "computer"])
        askedQuestion[25] = True
        if generalQuestion[25] in generalQuestionTab :
            elementRemove = generalQuestion[25]
            generalQuestionTab.remove(elementRemove)
    
    if len(petTab) > 0 and askedQuestion[26] == False:
        questionTab.append([create_pet_question(), "pet"])
        askedQuestion[26] = True
        if generalQuestion[26] in generalQuestionTab :
            elementRemove = generalQuestion[26]
            generalQuestionTab.remove(elementRemove)


# Fonction qui pose les questions
def question_ask(prenom) :
    if len(questionTab) > 0 :
        # Index de question aléatoire
        indexRand = random.randint(0, len(questionTab) - 1)

        # Affiche la question aléatoire
        print(questionTab[indexRand][0])

        sujet = questionTab[indexRand][1]

        # Supprime la question posée
        questionTab.pop(indexRand)

        # Retourne le sujet de la question
        return sujet

    elif len(generalQuestionTab) > 0 :
            # Index de question aléatoire
            indexRand = random.randint(0, len(generalQuestionTab) - 1)

            # Affiche la question aléatoire
            print(generalQuestionTab[indexRand][0])

            sujet = generalQuestionTab[indexRand][1]

            # Supprime la question posée
            generalQuestionTab.pop(indexRand)

            # Retourne le sujet de la question
            return sujet

    else :
        print("Oh no I'm sorry", prenom, "i have forget something, i got to go. It has been a pleasure to talk with you, happy new year and see you soon.\n")
        print("\nOk no problem, Bye !\n")
        exit()   


sportTab = []
religionTab = []
artTab = []
philosophyTab = []
politicsTab = []
foodTab = []
clothesTab = []
travelTab = []
musicTab = []
botanyTab = []
lifestyleTab = []
viceTab = []
scienceTab = []
technologyTab = []
historyTab = []
literatureTab = []
geographyTab = []
economyTab = []
lawTab = []
educationTab = []
medicineTab = []
psychologyTab = []
sociologyTab = []
associationTab = []
makeupTab = []
computerTab = []
petTab = []
questionTab = []
generalQuestion = [ ["Do you follow any sports teams or players ?\n", "sport"],
                    ["What role does religion play in your life ?\n", "religion"],
                    ["Have you visited any art galleries or museums recently ?\n", "art"],
                    ["What philosophical ideas interest you the most ?\n", "philosophy"],
                    ["What are your thoughts on current political events ?\n", "politics"],
                    ["What's your favorite type of food ?\n", "food"],
                    ["Do you have a favorite clothing brand or style ?\n", "clothes"],
                    ["Where is the most interesting place you've traveled to ?\n", "travel"],
                    ["What music do you like to listen to ?\n", "music"],
                    ["Do you have any plants or gardens at home ?\n", "botany"],
                    ["What's your overall lifestyle like ?\n", "lifestyle"],
                    ["Do you have any vices or habits you're trying to change ?\n", "vice"],
                    ["What scientific or technological advancements are you most excited about ?\n", "science"],
                    ["What are your thoughts on the role of technology in society ? Do you believe it has mostly positive or negative effects ?\n", "technology"],
                    ["What period of history do you find the most interesting ?\n", "history"],
                    ["What's your favorite type of literature ?\n", "literature"],
                    ["Do you enjoy learning about different cultures and geography ?\n", "geography"],
                    ["What are your thoughts on the current state of the economy ?\n", "economy"],
                    ["Do you have any legal issues or questions you'd like to talk about ?\n", "law"],
                    ["What was your experience in education like ?\n", "education"],
                    ["Do you have any medical conditions or concerns you'd like to discuss ?\n", "medicine"],
                    ["What psychological topics are you most interested in ?\n", "psychology"],
                    ["What do you think about the role of sociology in understanding society ?\n", "sociology"],
                    ["Are you involved in any associations or clubs ?\n", "association"],
                    ["Do you enjoy trying out new makeup looks or products ?\n", "makeup"],
                    ["What do you like most about using computers ?\n", "computer"],
                    ["Do you have any pets ? What are they like ?\n", "pet"]
                ]

generalQuestionTab = []
for i in range(len(generalQuestion)) :
    generalQuestionTab.append(generalQuestion[i])


askedQuestion = []
for i in range(len(generalQuestion)) :
    askedQuestion.append(False)

prenom = ""
sujet = "city"

prenom = startConversation()
while(1) :
    answer = input()
    analyse_phrase(answer)

    sentiment = sentiment_analysis(answer)

    if sentiment == "positive" :
        print("\nYou are interested in", sujet, ". Do you want to tell me more about it ?\n")

        answer = input()
        analyse_phrase(answer)

        sentiment = sentiment_analysis(answer)

        if sentiment == "positive" :
            print("\nI'm glad to hear that you like", sujet, ". Let's talk about something else.")
        
        else :
            print("\nLet's talk about something else.")

    elif sentiment == "negative" :
        print("\nYou are not interested in", sujet, ". Let's talk about something else.")

    elif sentiment == "neutral" :
        print("\nI see that", sujet, "isn't interesting you that much. Let's talk about something else.")


    question_add()
    sujet = question_ask(prenom)
