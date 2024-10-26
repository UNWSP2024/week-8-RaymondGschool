# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random, os

us_states_and_capitals: dict[str, str] = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

def clear_console():
    os.system('cls')

def display_question(state: str, answers_correct: int, questions_asked: int) -> bool:
    clear_console()

    print(f"\t\t{answers_correct}/{questions_asked} correct")
    print("-" * 50)
    print(f"\t\tWhat is '{state}'s capital?\n")

    answer: str = input().lower()
# return true if correct, false if incorrect
    return answer == us_states_and_capitals[state].lower()

def ten_question_quiz() -> None:
    answers_correct: int = 0
    for question_number in range(10):
        random_state: str = random.choice(list(us_states_and_capitals.keys()))

        # adds 1 if correct, else 0
        answers_correct += display_question(state=random_state, answers_correct=answers_correct, questions_asked=question_number)
        # remmove from dictionary to prevent duplicate questions
        us_states_and_capitals.pop(random_state)

    clear_console()

    print(f"Correct: {answers_correct}/10")


if __name__ == "__main__":
    ten_question_quiz()