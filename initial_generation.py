from tkinter import *
import random
import re
class Gen:
    def __init__(self):
        with open("words.csv") as file:
            self.word=random.choice(file.readlines())
        self.word=re.sub("\n","",self.word)
        self.word_characterization={letter:[] for letter in self.word}
        for letter in self.word:
            self.word_characterization[letter].append(letter)
        self.t=Tk()
        self.t.title("Budget Wordle")
        self.t.config(background="light gray")
        self.placements={0:[],1:[],2:[],3:[],4:[],5:[]}
        self.current_row=0
        for i in range(0,36):
            self.gen(i)
        self.input = Entry()
        self.input.grid(row=6, column=0, columnspan=12)
        self.btn = Button(text="Submit Guess", command=self.guess)
        self.btn.grid(row=7, column=0, columnspan=12)
        self.alphabet=["Q","W","E","R",'T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        self.alpha={}
        for i in range(0,26):
            self.gen_alpha(i)
        self.alpha2=self.alpha
    def gen(self,num):
        letter_num=num%6
        line_num=num//6
        new_letter=Label(text="#",background="light gray")
        new_letter.grid(row=line_num,column=(2*letter_num))
        self.placements[line_num].append(new_letter)
    def gen_alpha(self,col):
        new_keyboard_letter=Label(text=self.alphabet[col],background='light gray',font=("arial",6))
        self.alpha[self.alphabet[col]]=new_keyboard_letter
        col+=1
        row=8
        for i in range(0,2):
            if col>9:
                col-=9
                row+=1
        new_keyboard_letter.grid(column=col,row=row)
    def guess(self):
        guess=self.input.get()
        self.input.delete(0,99)
        if guess != "":
            if len(guess) !=6:
                self.input.insert(index=0,string="6 letter words only")
            else:
                self.word_characterization = {letter: [] for letter in self.word}
                for letter in self.word:
                    self.word_characterization[letter].append(letter)
                temp_word_characterization=self.word_characterization
                for i in range(0,6):
                    self.placements[self.current_row][i].config(text=guess[i].upper())
                    if guess[i].lower()==self.word[i]:
                        temp_word_characterization[guess[i].lower()] = temp_word_characterization[guess[i].lower()][:-1]
                        self.placements[self.current_row][i].config(background="green")
                        try:
                            self.alpha[guess[i].upper()].config(background="green")
                            self.alpha[guess[i].upper()]="null"
                            self.alpha2[guess[i].upper()] = "null"
                        except:
                            pass
                for i in range(0,6):
                    if (guess[i].lower() in self.word) and (guess[i].lower() in temp_word_characterization[guess[i].lower()]):
                        temp_word_characterization[guess[i].lower()]=temp_word_characterization[guess[i].lower()][:-1]
                        self.placements[self.current_row][i].config(background="yellow")
                        try:
                            self.alpha[guess[i].upper()].config(background="yellow")
                            self.alpha2[guess[i].upper()] = "null"
                        except:
                            pass
                    elif guess[i].lower() not in self.word:
                        try:
                            self.alpha[guess[i].upper()].config(background="gray")
                        except:
                            pass
                self.current_row+=1
                if guess.lower()==self.word:
                    if self.current_row==1:
                        self.end = Label(text=f"YOU WON ON YOUR FIRST GUESS!", background="green",font=("arial",8,"bold"))
                    else:
                        self.end = Label(text=f"YOU WON IN {self.current_row} GUESSES!", background="green")
                    self.end_(self.current_row)
                elif self.current_row==6:
                    self.end=Label(text=f"YOU LOST TO '{self.word.upper()}'",background="red",font=("arial",8,"bold"))
                    self.end_("lose")
    def end_(self,cond):
        self.input.pack_forget()
        self.btn.pack_forget()
        self.end.grid(row=6, column=0, columnspan=12)
        refresh=Label(text="Restart the game to play again",font=("arial",7,"italic"))
        refresh.grid(row=7,column=0,columnspan=12)
        with open("win-loss_ratio.csv","a") as file:
            file.write(f"{cond}\n")
    def cont(self):
        self.t.mainloop()