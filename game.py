import random, hmac, hashlib
import secrets

CHOICES = [ "ROCK", "PAPER", "SCISSORS", "SPOCK", "LIZARD" ]

# Delete this. And make a rule
RESULTS = {
    0: "Tie",
    1: "You win!",
    2: "You lose!",
    3: "You win!",
    4: "You lose!"
}
#

WIN_MESSAGE = "{:s} versus {:s}: {:s}"

def get_winner(computer_choice, user_choice):
    difference = (user_choice - computer_choice) % len(CHOICES)
    print(WIN_MESSAGE.format(CHOICES[computer_choice], CHOICES[user_choice], RESULTS[difference]))
    
def get_hash_code(computer_choice, key):
    return hmac.new(bytes(key, "utf-8"), bytes(computer_choice, "utf-8"), hashlib.sha256).hexdigest()
  
def main():
    while 1:
        for i, v in enumerate(CHOICES):
            print("{}: {}".format(i, v))
        key = secrets.token_hex(16)
        computer_choice = random.choice(CHOICES)
        print(get_hash_code(computer_choice, key))
        input_value = input()
        if input_value.lower() == 'q':
            return
        try:
            input_value = str(input_value) 
            input_value = CHOICES.index(input_value.upper())
        except:
            print("Error! Wrong input.")
            continue
        get_winner(CHOICES.index(computer_choice.upper()), input_value)
        print(key)
        
        
if __name__=="__main__":
    main()