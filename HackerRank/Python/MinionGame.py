# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    stuart = 0
    kevin = 0
    vowels = "AEIOU"
    string_len = len(string)
    
    for i, ch in enumerate(string):
        # if not ch.isalpha():
        #     continue
        
        if ch in vowels:
            kevin += (string_len - i)
        else:
            stuart += (string_len - i)
    
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)