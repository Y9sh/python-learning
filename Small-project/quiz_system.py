# Basic Quiz System:
# - store questions/answers in list of dict
# - ask each question
# - check answer & count score
# - display result
# Goal:
# Build a mini quiz program that:
# Stores multiple questions and answers using list of dicts.
# Loops through each question to ask user input.
# Checks user answer and keeps score count.
# Displays final score.

def title():
    banner = '''Quiz System'''
    print(banner)


def store():
    
    quiz = [
        {
            "question" : "What is 1 +1 ?" , "answer":"2"
        },
        {
            "question" : "What is 2+2? " ,"answer":"4"
        },
        {
            "question" : "What is capital of Japan?" ,"answer" : "Tokyo"
        }
    ]
    
    return quiz

def run(quiz):
    
    total_scores = len(quiz)
    
    user_score =0
    for q in quiz:
        # simple method to take question and answer on same list dict
        print(q["question"])
        user_answer =input("Answer wisely: ")
        if user_answer == q["answer"]:
            print("CORRECT")
            user_score +=1 
        else:
            print("WRONG")
            user_score-=1
    if user_score == total_scores :
        print(f"Full marks!!!{user_score}")
    else:
        print(f"It's okay: {user_score} ")
             
title()
q =store()
run(q)


'''
Where im stuck!!!!!!!!!!!!!!!!

how to take index output, from list dict -- REFER lines 40

'''