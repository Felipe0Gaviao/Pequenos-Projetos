from customtkinter import CTk, CTkFrame, StringVar, IntVar , CTkLabel, CTkButton, CTkCheckBox, CTkEntry
from time import sleep
from random import randint

class DiceRoller(CTk):

    def __init__(self):
        
        super().__init__()

        self.title('Dice Roller')

        SIZE = 300
        self.geometry(f'{SIZE}x{SIZE}')

        self.main_frame = CTkFrame(self)
        self.main_frame.pack(expand=True, fill='both')

        self.dice_var = StringVar(self.main_frame, value=0)

        self.dice_label = CTkLabel(self.main_frame, textvariable=self.dice_var, font=('Cascadia Code', 40))
        self.dice_label.pack()

        self.roll_button = CTkButton(self.main_frame, text='Roll', height=100, width=100, font=('Cascadia Code', 30), command=self.roll)
        self.roll_button.pack(pady=20)

        self.fast_roll = CTkCheckBox(self.main_frame, text='Fast Roll')
        self.fast_roll.pack()

        self.add_frame = CTkFrame(self.main_frame)
        self.add_frame.pack(pady=10)

        self.add_var = IntVar(self.add_frame, value=5)

        self.plus_num = CTkCheckBox(self.add_frame, text='+')
        self.plus_num.grid(row=0, column=0, sticky='w')
        
        self.add_entry = CTkEntry(self.add_frame, placeholder_text='1, 2, 3', textvariable=self.add_var, width=50, justify='center')
        self.add_entry.grid(row=0, column=0, sticky='e', padx=1)

        self.mainloop()
    
    def roll(self):
        wait_time = 0.01
        ranges = {1: 1, 0: 30}[self.fast_roll.get()]
        
        for _ in range(ranges):
            result = randint(1, 20)
            self.dice_var.set(f'{result} + {self.add_var.get()} = {result+self.add_var.get()}' if self.plus_num.get() else result)
            self.dice_label.update()
            sleep(wait_time)
            wait_time += 0.01

            if self.fast_roll.get(): break

DiceRoller()