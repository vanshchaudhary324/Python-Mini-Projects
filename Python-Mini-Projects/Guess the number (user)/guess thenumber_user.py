import random

def guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_num = random.randint(low, high)
        else:
            guess_num = low
        feedback = input(f"Is it {guess_num}? Too Low (L), Too High (H), or Correct (C)? ").lower()
        
        if feedback == 'l':
            low = guess_num + 1
        elif feedback == 'h':
            high = guess_num - 1
        elif feedback != 'c':
            print("Please enter 'L', 'H', or 'C'.")

    print(f"Yay! I guessed your number: {guess_num}")

# Start the game with a range up to 1000
guess(1000)
