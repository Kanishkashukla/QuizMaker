import time

class ques:
    option = []
    idk = []
    corans = []
    rightans_of_student = []

    print("\n**Hey Welcome to the Edyoda Quiz Platform**\n")
    passwrd = input("If you are logging in as the examiner, enter the password as EXAMINER\nIf you are logging in as a student, please enter EdYoda\n")
    if passwrd == "EXAMINER":
        print("")
    elif passwrd == "EdYoda":
        print("\nHey Learner, there is no quiz uploaded for you today. Please come back later!!\n")
        exit()
    else:
        print("Wrong Password!!\n")
        exit()

    def __init__(self):
        l = input("Set the difficulty level\nPress E/e for Easy, M/m for medium, D/d for difficult\n")
        if l=="E" or l=="e":
            self.level = "Easy Level"
        elif l=="M" or l=="m":
            self.level = "Medium Level"
        elif l=="D" or l=="d":
            self.level = "Difficult Level"
        else:
            print("What type of level is that? I hope it isn't out of the world!\nPlease try again\n")
            self.__init__()
        self.topic = input("What's this quiz about? Write the topic below : \n")

        self.addQues()

    def addQues(self):
        ans = True
        self.no_of_ques = 0
        while ans:
            statement = input("Enter the question : ")
            ques.idk.append(statement)
            ol = []
            for ono in range(1,5):
                ol.append(input("Enter option : "))
            ques.option.append(ol)
            self.correctans = input("Which one is the correct answer? Enter the option number : \n")
            ques.corans.append(self.correctans)

            self.no_of_ques = self.no_of_ques+1

            cont = input("Do you want to add more questions ? Y/N : \n")
            if cont=="N" or cont=="n":
                ans = False
        self.display()

    def display(self):
        print("\n")
        for i in range(len(ques.idk)):
            print("Question",i+1,")",ques.idk[i])
            for j in range(len(ques.option[i])):
                print(j+1,")",ques.option[i][j])
        #print("\n")
        print("Hey! We hope you have successfuly updated your questionnaire. Kindly ask the students to "
              "login through the password 'EdYoda'\n\n")
        self.student_info()

    def student_info(self):
        passw=input("Hello Learner, please enter your password to enter the test portal : ")
        if passw != "EdYoda":
            print("Wrong Password, Try Again!")
            self.student_info()
        else:
            self.name = input("Enter your name :")
            self.age = input("Enter your age :")
            self.countd()


    def countd(self):
        print("\nYou have successfully registered. We are all set to take the quiz\nYou are going to take the",self.topic,"'s",self.level,"quiz in")
        t=5
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f'\r{timer}', end='')
            time.sleep(1)
            t -= 1
        print("\nLet's go!!")
        self.test()

    def test(self):
        self.score = 0
        for i in range(len(ques.idk)):
            print("Question",i+1,")",ques.idk[i])
            for j in range(len(ques.option[i])):
                print(j+1,")",ques.option[i][j])
            choice = input("\nChoose the correct option number\n")
            if choice == ques.corans[i]:
                self.score = self.score+10
            else:
                pass
        self.result()

    def result(self):
        print("\nYou have completed the quiz. Here are your details :\n")
        print("Your name :",self.name)
        print("Your age :", self.age)
        print("Quiz Topic :", self.topic)
        print("Difficulty level :", self.level)
        print("Your score :", self.score, "out of",self.no_of_ques*10)

        for i in range(len(ques.idk)):
            print("Question",i+1,")",ques.idk[i])
            for j in range(len(ques.option[i])):
                print(j+1,")",ques.option[i][j])
            print("Correct Ans : ",ques.corans[i],"\n")

k = ques()