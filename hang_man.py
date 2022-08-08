import random
def hangman():
    print("hello word")
    list_of_words=["educar","hangman","india","laptop"]
    word=random.choice(list_of_words)
    print(word)
    turns=10
    guessmade=""
    valid_entery=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word=""
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else :
                main_word=main_word+"_"
            if main_word ==word:
                print(main_word)
                print("you won !!!!")


        print("guess the words ",main_word)
        guess=input()
        if guess in valid_entery:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
        if turns==9:
            print("9 turns left !!!")
            print("_ _ _ _ _ _ _ _ _ _ _ _ _")
        if turns==8:
               print("8 turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("          O            ")
        if turns==7:
               print("7 turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("          O            ")
               print("          |           ")
        if turns==6:
               print("6  turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("          O            ")
               print("          |            ")
               print("         /             ")
        if turns==5:
               print("5 turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("          O            ")
               print("          |            ")
               print("         / \           ")
        if turns==4:
               print("4 turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("         \O            ")
               print("          |            ")
               print("         / \           ")
        if turns==3:
               print("3 turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("         \O/           ")
               print("          |            ")
               print("         / \            ")
               
        if turns==2:
               print("2 turns left !!!")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("         \O/ |         ")
               print("          |            ")
               print("         / \           ")
               
        if turns==1:
               print("only 1 turns left !!! hangman on his last breath")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("         \O/_|        ")
               print("          |            ")
               print("         / \           ")
        if turns==0:
               print("you lose")
               print("let you die a good man")
               print("_ _ _ _ _ _ _ _ _ _ _ _")
               print("         \O/_|        ")
               print("          |            ")
               print("         / \           ")
               break                
        
   
               
name=input("ENTER YOUR NAME")
print("welcome",name,"!")
print("_ _ _ _ _  _ _ _ _ _ _ _")
print("try to guess the word in less than to 10 attemts")
hangman()