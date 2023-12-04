from random import choice

class GuessTheWord:

    def __init__(self) -> None:
        
        self.NAME = input('What is your name? ')
        
        while True:
            self.chose_word()

            self.CURRENT = ['-']*len(self.CHOSEN)

            self.TRIES = []

            self.TURNS = 12

            print(f'You have {self.TURNS} turns to guess the complete word')

            print(f'Good Luck, {self.NAME}')

            while True:
                self.guess_letter(input('\nGuess a Letter: '))

                if self.TURNS < 1 or '-' not in self.CURRENT:

                    if '-' not in self.CURRENT:
                        
                        print(f'You Won!! \nCompleted Word: {self.CHOSEN}')
                        
                        break
                    else:

                        print(f'You Lost. \nCorrect Word: {self.CHOSEN}')

                        break
                
            while True:
                match input('Wanna Play Again (s/n)? '):
                    case 's':
                        continue
                    case 'n':
                        quit()
                    case _:
                        print('Not a Verified input.')
                        continue
    
    def chose_word(self) -> None:

        with open('words.txt','r') as words:

            word_list = words.read().split('\n')
            
            self.CHOSEN = choice(word_list)

    def guess_letter(self, guess:str) -> None:
        
        while True:

            if guess not in self.TRIES:

                if guess == '' or guess not in 'abcdefghijklmnopqrstuvwxyz':
                    print('Guess must be a valid input [a-z]')
                    break

                self.TURNS -= 1

                if guess in self.CHOSEN:
                    for i in range(len(self.CHOSEN)):
                        if self.CHOSEN[i] == guess:
                            self.CURRENT[i] = guess

                    print(f'Correct!!\n{"".join(self.CURRENT)}')
                else:
                    print(f'Wrong\n{"".join(self.CURRENT)}')
                
                self.TRIES.append(guess)

                print(f'{self.TURNS} Turns left.')
                
                break

            elif guess in self.TRIES:
                print('You already Tried that.')

                guess = input('Try Another One: ')
                continue

if __name__ == '__main__':
    GuessTheWord()