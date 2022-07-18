import random

def play():
    user = input("(r) for rock, (p) for paper or (s) for scissors")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'Tie'
    
    if winner(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def winner(player, opponent):
        #return true if player wins
        
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
            return 'Winner!'
        
print(play())