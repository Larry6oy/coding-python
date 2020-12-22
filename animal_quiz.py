score = 0
def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        print('Correct answer')
        score = score + 1
print('gess the animal!')
guess1 = input('Which bear lives at the North pole?')
print(guess1)
check_guess(guess1, 'polar bear')
guess2 = input('Which is the bigest animal?')
print(guess2)
check_guess(guess2, 'blue whale')
guess3 = input('Which bear lives in Alaska?')
print(guess3)
check_guess(guess3, 'kodiak bear')


print('Your score is ' +str(score))