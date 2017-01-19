import random

#INVENTORY
inventory = ['HEALTH POTION', 'HINT']

#STARTING HEALTH POINTS
hp = 100

#QUESTIONS CORRECT IN A ROW
corrinrow = 0

#QUESTIONS CORRECT
corr = 0

#QUESTION ORDER
qorder = random.sample(range(1,16),15)
nextq = 0

#QUESTIONS: EACH QUESTION IS ITS OWN FUNCTION
def question1(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWho is the Scorn of the Moon?
\nA: Leona
B: Diana
C: Taric
D: Pantheon""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "leona" or choice == "taric" or choice == "pantheon":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "diana":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question1(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question1(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: She has the same name as the princess who died in a car crash"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question1(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question1(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question2(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhat primary role is Diana categorized in?
\nA: Fighter
B: Mage
C: Assassin
D: Tank""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "mage" or choice == "assassin" or choice == "tank":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "fighter":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question2(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question2(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: She has sustained damage"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question2(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question2(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question3(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhich character has a really annoying spammy dash ability, a windwall that blocks everything, and
stupid crits?
\nA: Taliyah
B: Braum
C: Akali
D: Yasuo""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "taliyah" or choice == "braum" or choice == "akali":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "yasuo":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question3(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question3(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: He 'has-a-key'"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question3(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question3(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question4(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhich character does Sp4zie main who comes from the void?
\nA: Vel'Koz
B: Karma
C: Kassadin
D: Malzahar""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "karma" or choice == "kassadin" or choice == "malzahar":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "vel'koz":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question4(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question4(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: OH DARN!!"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question4(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question4(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question5(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhat is Lux's ultimate ability?
\nA: Lunar Rush
B: Life Form Disintegration ray
C: Final Spark
D: Death Ray""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "lunar rush" or choice == "life form disintegration ray" or choice == "death ray":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "final spark":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question5(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question5(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: IMMA FIRIN' MAH LAZER!"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question5(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question5(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question6(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhat faction does Darius belong to?
\nA: Demacia
B: Noxus
C: Ionia
D: Zaun""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "demacia" or choice == "zaun" or choice == "ionia":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "noxus":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question6(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question6(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: Mortal enemies of Demacia"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question6(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question6(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question7(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhat is the maximum attack speed Kog'Maw can achieve?
\nA: 1.0
B: 2.5
C: 2.0
D: 5.0""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "1.0" or choice == "2.5" or choice == "2.0":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "5.0":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question7(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question7(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: Insane projectile vomit"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question7(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question7(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question8(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWho was exiled from Demacia by Garen due to dereliction of duty?
\nA: Lux
B: Taric
C: Jarvan
D: Yasuo""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "lux" or choice == "jarvan" or choice == "yasuo":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "taric":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question8(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question8(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: Gems are truly, truly, truly outrageous"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question8(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question8(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question9(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWho is obsessed with the 'Glorious Evolution'?
\nA: Orianna
B: Viktor
C: Heimerdinger
D: Ziggs""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "orianna" or choice == "heimerdinger" or choice == "ziggs":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "viktor":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question9(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question9(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: He is part machine and has designed many skins for other characters"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question9(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question9(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question10(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWho has an ultimate ability names 'Enchanted Crystal Arrow'?
\nA: Ashe
B: Jinx
C: Vayne
D: Ezreal""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "jinx" or choice == "vayne" or choice == "ezreal":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "ashe":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question10(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question10(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: She's married to the Khal Drogo of League of Legends"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question10(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question10(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question11(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhich character can place mini-turrets on the map?
\nA: Teemo
B: Ziggs
C: Heimerdinger
D: Corki""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "teemo" or choice == "ziggs" or choice == "corki":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "heimerdinger":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question11(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question11(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: DONGER!"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question11(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question11(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question12(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhich character used to have a non-ultimate global teleport ability on 30 second cooldown at maximum rank?
\nA: Twisted Fate
B: Graves
C: Tahm Kench
D: LeBlanc""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "graves" or choice == "tahm kench" or choice == "leblanc":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "twisted fate":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question12(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question12(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: He is a compulsive gambler"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question12(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question12(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question13(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWhich character can't have his cigar back?
\nA: Shaco
B: Sion
C: Graves
D: Gangplank""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "shaco" or choice == "sion" or choice == "gangplank":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "graves":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question13(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question13(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: Six feet under"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question13(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question13(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question14(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWho is Satan and puts Satan shrooms everywhere?
\nA: Singed
B: Cassiopeia
C: Yasuo
D: Teemo""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "singed" or choice == "cassiopeia" or choice == "yasuo":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "teemo":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question14(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question14(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: Never underestimate the power of the scout's code!"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question14(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question14(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

def question15(hp, corr, corrinrow, nextq):
    if hp > 0:
        print("""\nWho do you never chase?
\nA: Cassiopeia
B: Nocturne
C: Singed
D: Shaco""")
        print "\nYou can use items in your inventory:", inventory
        choice = raw_input("Type in your answer: ")
        choice = str.lower(choice)
        if choice == "nocturne" or choice == "cassiopeia" or choice == "shaco":
            corrinrow = 0
            hp = hp - 25
            print "\nIncorrect answer! You have lost 25 hp. HP:", hp
            print "You now have 0 questions correct in a row."
            print "Questions correct:", corr
            if hp > 0:
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nGame over: You Died"
                end(corr)
        elif choice == "singed":
            corrinrow = corrinrow + 1
            corr = corr + 1
            print "\nCorrect answer! You got", corrinrow, "correct in a row!"
            print "Questions correct:", corr
            print "HP:", hp
            if corrinrow == 3:
                inventory.append('HINT')
                print "Good job, you got 3 questions correct in a row. You have been gifted a HINT. INVENTORY:", inventory
            elif corrinrow == 6:
                inventory.append('HEALTH POTION')
                print "Good job, you got 6 questions correct in a row. You have been gifted a HEALTH POTION. INVENTORY:", inventory
            elif corrinrow == 9:
                inventory.append('ZHONYAS HOURGLASS')
                print "Good job, you got 9 questions correct in a row. You have been gifted a ZHONYAS HOURGLASS. INVENTORY:", inventory
            nextquestion(hp, corr, corrinrow, nextq)
        elif choice == "zhonyas hourglass":
            if inventory.count('ZHONYAS HOURGLASS') > 0:
                print "\nYou have been put into stasis and skipped this question."
                inventory.remove('ZHONYAS HOURGLASS')
                nextquestion(hp, corr, corrinrow, nextq)
            else:
                print "\nYou don't have a ZHONYAS HOURGLASS in your inventory. INVENTORY:", inventory
                question15(hp, corr, corrinrow, nextq)
        elif choice == "health potion":
            if inventory.count('HEALTH POTION') > 0:
                hp = hp + 25
                inventory.remove('HEALTH POTION')
                print "\nYou drank your health potion and gained 25 hp. HP:", hp
            else:
                print "\nYou don't have a HEALTH POTION in your inventory. INVENTORY:", inventory
            question15(hp, corr, corrinrow, nextq)
        elif choice == "hint":
            if inventory.count('HINT') > 0:
                inventory.remove('HINT')
                print "\nHint: One does not simply chase the bald guy with poison gas"
            else:
                print "\nYou don't have a HINT in your inventory. INVENTORY:", inventory
            question15(hp, corr, corrinrow, nextq)
        else:
            print("\nInvalid choice")
            question15(hp, corr, corrinrow, nextq)
    else:
        print "\nGame over: You Died"

#QUESTION CHOOSER FROM RANDOMLY GENERATED LIST
def nextquestion(hp, corr, corrinrow, nextq):
    nextq = nextq + 1
    if nextq < 16:
        if qorder[nextq - 1] == 1:
            question1(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 2:
            question2(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 3:
            question3(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 4:
            question4(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 5:
            question5(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 6:
            question6(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 7:
            question7(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 8:
            question8(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 9:
            question9(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 10:
            question10(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 11:
            question11(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 12:
            question12(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 13:
            question13(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 14:
            question14(hp, corr, corrinrow, nextq)
        elif qorder[nextq - 1] == 15:
            question15(hp, corr, corrinrow, nextq)
    if nextq == 16:
        print "\nCongratulations! You completed the quiz!"
        end(corr)

def end(corr):
    resultsfile = "TheQuizResults.txt"
    vFile = open(resultsfile, "r+")
    print vFile.read()

    name = raw_input("\nEnter your name: ")
    score = corr*100 + inventory.count('HINT')*50 + inventory.count('HEALTH POTION')*75 + inventory.count('ZHONYAS HOURGLASS')*100
    results = ["\n", name, " | ", str(corr), " | ", str(score)]
    vFile.writelines(results)
    vFile.close()

    resultsfile = "TheQuizResults.txt"
    vFile = open(resultsfile, "r")
    print vFile.read()
    vFile.close()


nextquestion(hp, corr, corrinrow, nextq)
