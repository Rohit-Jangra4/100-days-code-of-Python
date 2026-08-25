import random

questions = [
    "Who was the first Indian woman to win a medal in the Olympics?",
    "Who was the first person from India to win an Academy Award (Oscar)?",
    "Which country is the world's largest producer of coffee?",
    "What is the capital of Australia?",
    "Which planet is known as the Red Planet?"
]

options = [
    ["A. Karnam Malleswari", "B. Kunjarani Devi", "C. Mirabai Chanu", "D. Khumukcham Sanjita Chanu"],
    ["A. Bhanu Athaiya", "B. Satyajit Ray", "C. A.R. Rahman", "D. Gulzar"],
    ["A. Colombia", "B. Brazil", "C. Vietnam", "D. Ethiopia"],
    ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
    ["A. Jupiter", "B. Venus", "C. Saturn", "D. Mars"]
]

answers = ["A", "A", "B", "C", "D"]

prize = [10000, 50000, 100000, 120000, 150000]

total_money = 0
lifeline = True

for i in range(len(questions)):

    print("\n--------------------------------")
    print("Question", i + 1)
    print(questions[i])
    print("--------------------------------")

    # Display options
    for option in options[i]:
        print(option)

    if lifeline:
        print("Type 50-50 to use Lifeline")

    answer = input("Enter your answer: ").upper()

    # 50-50 Lifeline
    if answer == "50-50":

        if lifeline:
            lifeline = False

            print("\n🔥 50-50 Lifeline Used!")

            # Find wrong options
            wrong_options = []

            for option in options[i]:
                if option[0] != answers[i]:
                    wrong_options.append(option)

            # Randomly select 2 wrong options
            remove_options = random.sample(wrong_options, 2)

            # Remove them
            remaining_options = options[i].copy()

            for option in remove_options:
                remaining_options.remove(option)

            print("\nRemaining Options:")

            for option in remaining_options:
                print(option)

            # Ask answer again
            answer = input("Enter your answer: ").upper()

        else:
            print("❌ 50-50 Lifeline already used!")
            answer = input("Enter your answer: ").upper()

    # Check answer
    if answer == answers[i]:

        print("Correct! 🎉")

        total_money += prize[i]

        print("You won ₹", prize[i])
        print("Total Money: ₹", total_money)

    else:

        print("Wrong answer! ❌")

        total_money = 0

        print("Total Money: ₹", total_money)


print("\n================================")
print("GAME OVER 🎮")
print("Final Winning Amount: ₹", total_money)
print("================================")