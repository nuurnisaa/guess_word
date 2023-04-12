secret_word="YouTube"
guess_word=""
hint_word="Watch video"
guess_count=0
guess_limit=3
out_of_guess=False

print("Hint:",(hint_word))
while guess_word!=secret_word and not(out_of_guess):
    if guess_count<guess_limit:
        guess_word=input("Enter your guess: ")
        guess_count+=1
    else:
      out_of_guess=True  

if out_of_guess:
    print("Lose chance. Try again!")
else:
    print("You are correct!")
    