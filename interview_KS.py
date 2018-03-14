def question(q):
    global answer
    answer = input(q)
    print(answer)

question("What's your name?  ")

question("What's your favorite class?  ")
if answer == "English":
    question("Wonderful, what are you learning?  ")
    print("wow, I remember doing " + answer + " when I was your age.")

question("Do you play any sports?  ")
if answer == "Yes":
    question("What sport do you play?  ")
    print ("Cool! " + answer + " sounds fun.")
    
    
