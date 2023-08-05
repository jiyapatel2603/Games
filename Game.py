p=int(input("press 1 for Trivia and 2 for Rock Paper Scissors:"))
if p==1:
    print('Hello peeps!!\nWelcome to Trivia!!\nHere is everything you need to know about this game:\n\n<>This is a Questionnaire Game where 4 different geners are provided \n<>Make sure you have having written the correct spelling otherwise points will not be granted.\n<>This is a quiz about the only thing you did during quarantine besides sleeping. The ones who studied might also give it a try\n\nPeace Out✌️\n')
    USER_SCORE=0
    print("The choices for genre are\n 1:Movies\n 2:Web series\n 3:TV series\n 4:Cartoon" )
    z=int(input("choose genre:"))
    if z==1:
        def choose(choice):
            global USER_SCORE
            choice=int(input("choose from movies:\n 1 for Jumanji2\n 2 for Avengers:Endgame\n 3 for Frozen2\n 4 for Annabelle Comes Home\n"))
            if choice==1:
                print("Q1  Which character turned into Dr. Bravestone(Dwayne Johnson) after entering the game?")
                Q1=input("Enter your answer: ")
                answer1="spencer"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
            
                print("Q2  Who found the Jumanji board game in 1996?")
                Q2=input("Enter your answer: ")
                answer2="alex"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")    
            
                print("Q3  Bethany was obsessed with her ______?")
                Q3=input("Enter your answer: ")
                answer3="phone"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
                print("Q4  What mode of transportation do they take from the transportation shed?")
                Q4=input("Enter your answer: ")
                answer4="helicopter"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

            elif choice==2:
                print("Q1  Who killed Thanos?")    
                Q1=input("Enter your answer: ")
                answer1="thor"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
            
                print("Q2  What is Thor's mother's name?")
                Q2=input("Enter your answer: ")
                answer2="frigga"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")    
            
                print("Q3  In which year do Tony and Steve travel to get the space stone and more pym particals?")
                Q3=input("Enter your answer: ")
                answer3="1970"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
                print("Q4  Which actor dubbs Groot")
                Q4=input("Enter your answer: ")
                answer4="vin diesel"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
        
            elif choice==3:
                print("Q1  What does Olaf name the wind spirit?")
                Q1=input("Enter your answer: ")
                answer1="gale"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
            
                print("Q2  Who became the Queen of Arendelle?")
                Q2=input("Enter your answer: ")
                answer2="anna"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")    
            
                print("Q3  Who is the fifth spirit?")
                Q3=input("Enter your answer: ")
                answer3="elsa"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
                print("Q4  Who is Christoff's bestfriend?")
                Q4=input("Enter your answer: ")
                answer4="swen"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
            
            elif choice==4:
                print("Q1  Daniela’s ______ died in a car crash while Daniela was driving.")
                Q1=input("Enter your answer: ")
                answer1="father"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
            
                print("Q2  Mary Ellen had which respiratory disease?")
                Q2=input("Enter your answer: ")
                answer2="asthma"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")    
            
                print("Q3  Which demonically possessed board game had the Warrens kept?")
                Q3=input("Enter your answer: ")
                answer3="feeley meeley"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
                print("Q4  What was Bob Palmeri's nickname?")
                Q4=input("Enter your answer: ")
                answer4="bob's got balls"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")            

    elif z==2:
        def choose(choice):
            global USER_SCORE
            choice=int(input("choose from Web series:\n 1 for 13Reasons Why\n 2 for Money Heist\n 3 for Dark\n 4 for Peaky Blinders\n"))
            if choice==1:
                print("Q1  Who died in a car accident due to a knocked out stop sign?")
                Q1=input("Enter your answer: ")
                answer1="jeff"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Which of the main characters in the show has two dads?")
                Q2=input("Enter your answer: ")
                answer2="courtney"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  Who was beaten up by Monty at one of Bryce's party?")
                Q3=input("Enter your answer: ")
                answer3="winston"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  Alex and ______ were voted for prom king and queen")
                Q4=input("Enter your answer: ")
                answer4="charlie"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
            if choice==2:
                print("Q1  What is Tokyo's real name in the series?")
                Q1=input("Enter your answer: ")
                answer1="silene oliveira"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  How many euros did the gang manage to steal from the Royal Mint of Spain?")
                Q2=input("Enter your answer: ")
                answer2="2.4 billion"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  Whose job did National Police Corps inspector Alicia Sierra take over after they left the force?")
                Q3=input("Enter your answer: ")
                answer3="raquel murillo"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  Who instructed Denver to dispose of hostage Mónica?")
                Q4=input("Enter your answer: ")
                answer4="berlin"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT") 
        
            if choice==3:
                print("Q1  In which year did Jonas realized about time travel?")
                Q1=input("Enter your answer: ")
                answer1="1986"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Who shoots young Martha in front of young Jonas?")
                Q2=input("Enter your answer: ")
                answer2="future jonas"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  What is the Origin?")
                Q3=input("Enter your answer: ")
                answer3="jonas and martha"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  By whose guidance are two duplicate worlds are created?")
                Q4=input("Enter your answer: ")
                answer4="claudia"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

            if choice==4:
                print("Q1  What part of London is Alfie's bakery in?")
                Q1=input("Enter your answer: ")
                answer1="camden"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Which singer provides the iconic Red Right Hand track?")
                Q2=input("Enter your answer: ")
                answer2="nick cave"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
    
                print("Q3  I've heard very bad, bad bad things about you ______ people")
                Q3=input("Enter your answer: ")
                answer3="birmingham"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  Who stars as Tom Hardy's wife?")
                Q4=input("Enter your answer: ")
                answer4="may carleton"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")


    elif z==3:
        def choose(choice):
            global USER_SCORE
            choice=int(input("choose from TV series:\n 1 for TMKOC\n 2 for F.R.I.E.N.D.S\n 3 for Young Sheldon \n 4 for Riverdale\n"))
            if choice==1:
                print("Q1  What does Gulabo call Jethalal?")
                Q1=input("Enter your answer: ")
                answer1="saiba"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Name the person who see the 'bhootni' first time in the Show?")
                Q2=input("Enter your answer: ")
                answer2="jethalal"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3 What was the favorite dish of dog sheru?")
                Q3=input("Enter your answer: ")
                answer3="thepla"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  How many years of Tarak Mehta will be completed in 2020?")
                Q4=input("Enter your answer: ")
                answer4="12"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
            if choice==2:
                print("Q1 Monica briefly dates billionaire Pete Becker. Where does he take her for their first date?")
                Q1=input("Enter your answer: ")
                answer1="rome"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  What’s the name of the 1950s-themed diner where Monica worked as a waitress?")
                Q2=input("Enter your answer: ")
                answer2="moondance"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3 What’s Joey’s penguin’s name?")
                Q3=input("Enter your answer: ")
                answer3="hugsy"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  What fake name does Phoebe use when she wants to remain anonymous?")
                Q4=input("Enter your answer: ")
                answer4="regina phalange"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT") 
        
            if choice==3:
                print("Q1  What fictional Texas city does the show take place in?")
                Q1=input("Enter your answer: ")
                answer1="medford"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  What is Meemaw's first and last name?")
                Q2=input("Enter your answer: ")
                answer2="connie tucker"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  What does Meemaw call sheldon?")
                Q3=input("Enter your answer: ")
                answer3="moonpie"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  What song is used to soothe sick Sheldon?")
                Q4=input("Enter your answer: ")
                answer4="soft kitty"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

            if choice==4:
                print("Q1  Who plays the character of Betty Cooper?")
                Q1=input("Enter your answer: ")
                answer1="lili reinhart"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Who is the new principal after Weatherbee?")
                Q2=input("Enter your answer: ")
                answer2="mr honey"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  Jughead and Betty desire to get into which collage?")
                Q3=input("Enter your answer: ")
                answer3="yale"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  Who gets hit by a car while saving a lady whose car had broke down")
                Q4=input("Enter your answer: ")
                answer4="fred"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

    elif z==4:
        def choose(choice):
            global USER_SCORE
            choice=int(input("choose from Cartoon:\n 1 for Tom and Jerry\n 2 for Pokemon\n 3 for Shinchan \n 4 for Phineas and Ferb\n"))
            if choice==1:
                print("Q1  What is Spike's sons name?")
                Q1=input("Enter your answer: ")
                answer1="tyke"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Who is Tom's owner?")
                Q2=input("Enter your answer: ")
                answer2="mammy two shoes"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3 In which country was Tom and Jerry made?")
                Q3=input("Enter your answer: ")
                answer3="australia"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  What is the name of the grey little mouse?")
                Q4=input("Enter your answer: ")
                answer4="nibbles"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")
                
            if choice==2:
                print("Q1 Who is the top evolved form of Bulbasaur?")
                Q1=input("Enter your answer: ")
                answer1="venusaur"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  On what bases are the names of all the professors kept?")
                Q2=input("Enter your answer: ")
                answer2="plant"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3 Who evolves from Magikarp?")
                Q3=input("Enter your answer: ")
                answer3="gyarados"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  Where is the best place to encounter wild pokemons?")
                Q4=input("Enter your answer: ")
                answer4="tall grass"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT") 
        
            if choice==3:
                print("Q1  What is the vegetable that Shinchan hates to eat?")
                Q1=input("Enter your answer: ")
                answer1="capsicum"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  What is Shinchan's full name?")
                Q2=input("Enter your answer: ")
                answer2="shinnosuke nohara"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  Who is anti-shinchan in the show?")
                Q3=input("Enter your answer: ")
                answer3="kazama"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  What is the pig called in Shinchan?")
                Q4=input("Enter your answer: ")
                answer4="buriburizaemon"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

            if choice==4:
                print("Q1  How many days of Summer Vacation are there?")
                Q1=input("Enter your answer: ")
                answer1="104"
                if Q1==answer1:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q2  Where is Ferb from?")
                Q2=input("Enter your answer: ")
                answer2="united kingdom"
                if Q2==answer2:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q3  How is Ferb related Candice?")
                Q3=input("Enter your answer: ")
                answer3="stepbrother"
                if Q3==answer3:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

                print("Q4  What is the name of Dr. Doofenshmirtz's daughters name?")
                Q4=input("Enter your answer: ")
                answer4="vanessa"
                if Q4==answer4:
                    print("CORRECT")
                    USER_SCORE+=1
                else:
                    print("INCORRECT")

    choice=[1,2,3,4]
    choose(choice)            
    print("Your score is:",USER_SCORE)                

if p==2:
    print('Hello peeps!!\n Welcome to Rock Paper Scissors!!\n Here is everything you need to know about this game:\n <> You’ll be playing against the Computer\n <> You’ll have to choose one of the three choices(i.e. rock or paper or scissors)\n <> REMEMBER:\n     Scissors cuts Paper\n     Paper wraps around Rock\n     Rock breaks Scissors \n <> If both yours and computers choices match then it is a TIE.\n <> Points will be counted in the dialog box.\n\n Results will be displayed below:\n Happy Gaming!!')
    import random
    import tkinter as tk
    
    window = tk.Tk()
    window.geometry("250x200")
    window.title("Rock Paper Scissors Game")

    USER_SCORE = 0
    COMP_SCORE = 0
    USER_CHOICE = ""
    COMP_CHOICE = "" 

    def choice_to_number(choice):
        rps = {'rock':0,'paper':1,'scissor':2}
        return rps[choice]

    def number_to_choice(number):
        rps={0:'rock',1:'paper',2:'scissor'}
        return rps[number]
    def random_computer_choice():
        return random.choice(['rock','paper','scissor']) 

    def result(human_choice,comp_choice):
        global USER_SCORE
        global COMP_SCORE
        user=choice_to_number(human_choice)
        comp=choice_to_number(comp_choice)
        if(user==comp):
            print("Tie")
        elif((user-comp)%3==1):
            print("You win")
            USER_SCORE+=1
        else:
            print("Comp wins")
            COMP_SCORE+=1
        text_area = tk.Text(master=window,height=10,width=50,bg="lightblue")
        text_area.grid(column=0,row=4)
        answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
        text_area.insert(tk.END,answer)
        
    def rock():
        global USER_CHOICE
        global COMP_CHOICE
        USER_CHOICE='rock'
        COMP_CHOICE=random_computer_choice()
        result(USER_CHOICE,COMP_CHOICE)
    
    def paper():
        global USER_CHOICE
        global COMP_CHOICE
        USER_CHOICE='paper'
        COMP_CHOICE=random_computer_choice()
        result(USER_CHOICE,COMP_CHOICE)
                 
    def scissor():
        global USER_CHOICE
        global COMP_CHOICE
        USER_CHOICE='scissor'
        COMP_CHOICE=random_computer_choice() 
        result(USER_CHOICE,COMP_CHOICE)
 
    button1 = tk.Button(text="       Rock       ",bg="grey",command=rock)
    button1.grid(column=0,row=1)
    button2 = tk.Button(text="       Paper      ",bg="white",command=paper)
    button2.grid(column=0,row=2)
    button3 = tk.Button(text="      Scissor     ",bg="orange",command=scissor)
    button3.grid(column=0,row=3)

    window.mainloop()
       
            


            