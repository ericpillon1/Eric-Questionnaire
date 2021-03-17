#questionnaire game
print('How well do you think you know me? I guess you will have to take the test to find out ;)')

total_questions = 8
score = 0


ans = input("1. What is my favourite video game? ")

if ans.lower() == 'grand theft auto':
    print("Correct!")
    score += 1
elif ans.lower() == 'gta':
    print("Correct!")
    score += 1
else:
    print("Incorrect! What else do I spend all my time playing... idiot.")

ans = input("2. What is my favourite flavour of chips? ")

if ans.lower() == 'all dressed':
    print("Correct!")
    score += 1
else:
    print('Incorrect! This one is a tough one!')

ans = input('3. What sport have I played the most growing up? ')

if ans.lower() == 'hockey':
    print('Correct!')
    score += 1
else:
    print('Incorrect! Do you even know me at all??')

ans = input('4. What sport do I love to watch that is not hockey? ')

if ans.lower() == 'formula 1':
    print('Correct!')
    score += 1
elif ans.lower() == 'formula one':
    print("correct!")
    score += 1
elif ans.lower() == 'f1':
    print("correct!")
    score += 1
else: 
    print('Incorrect! I feel like you barely even know me :( ')

ans = input("5. What is my favourite meal? ")

if ans.lower() == 'burger': 
    print('Correct!')
    score += 1
elif ans.lower() == 'burgers':
    print("Correct!")
    score += 1
elif ans.lower() == 'chicken parmesan':
    print('Correct!')
    score += 1
else:
    print('Incorrect! This one is a toss up!')

ans = input("6. How tall am I? ")

if ans.lower() == 'six feet':
    print('Correct!')
    score += 1
elif ans.lower() == '6 feet':
    print("Correct!")
    score += 1
elif ans.lower() == "6'0":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

ans = input("7. What is my favourite car brand? ")

if ans.lower() == 'lamborghini':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

ans = input("8. What is my favourite NHL team (city)? ")

if ans.lower() == 'toronto':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


#End of the Quiz
print("Thank you for playing! You got " + str(score) + " questions correct.")

percent = (score / total_questions *100)
print('Your final score is ' + str(percent), '%')

if percent <= 50:
    print("Maybe you don't know me that well...")
else: 
    print("Maybe you do know me! :)")
