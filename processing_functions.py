
username_list = [] # List to store usernames for checking duplicates

def view_questions(current_questions): # Function to view current questions
    if not current_questions: # Check if there are no questions
        print("No questions available.")
    else: # If there are questions, print them
        print("Current Questions:")
        i = 1
        for question in current_questions:
            print(f"{i}. {question}")
            i += 1
        print(f"You have surveyed {get_total_answers()} people so far.")


def add_answer(question, answer): # Function to add an answer to a question
    if answer in question: # Check if the answer already exists
        question[answer] += 1
    else: # If the answer does not exist, add it to the dictionary
        question[answer] = 1


def check_username(username): # Function to check if the username already exists
    if username in username_list: # Check if the username is already in the list
        print("It appears that you have already taken the survey.")
        return False
    else: # If the username is not in the list, add it to the list
        username_list.append(username)
        return True


def get_total_answers(): # Function to get the total number of people who have taken the survey
    return len(username_list)


def check_validity(current_questions, name):
    if not current_questions: # Check if there are no questions
        print("No questions available to answer.")
        return False
    else: # If there are questions, prompt the user to answer them
        print("====================================") 
            age_check = input("Please enter your age:\n")
            if int(age_check) >= 18: # Check if the user is 18 or older
                return True
            else:
                print("Sorry, this survey is intended for adults only.")
                return False
    


def top_answers(question, total_answers): # Function to get the top answers for a question
    if not question: # Check if there are no answers
        print("No answers available for this question.")
        return
    sorted_answers = sorted(question, key=lambda x: question[x], reverse=True)
    print(f"Top answers for question '{question}':")
    for answer in sorted_answers:
        total_answers -= question[answer]
        if total_answers >= 0:
            print(f"- {answer}: {question[answer]}")
        else:
            ending_answer = question[answer] + total_answers
            print(f"- {answer}: {ending_answer}")
            break
    

def analyse_answers(current_questions): # Function to analyse answers
    if not current_questions: # Check if there are no questions
        print("No questions available to analyse.")
    else: # If there are questions, begin analysis
        if input("Would you like to analyse all answers or just the top answers? (all/top): ").lower() == 'all':
            total_answers = float('inf')
            for question in current_questions:
                print("====================================")
                print(f"Question: {question}")
                top_answers(current_questions[question], total_answers)
                print("====================================")
        else:
            total_answers = 50 # Set the total number of top answers to display
            for question in current_questions:
                print("====================================")
                print(f"Question: {question}")
                top_answers(current_questions[question], total_answers)
                print("====================================")
                