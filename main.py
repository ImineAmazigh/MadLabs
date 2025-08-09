import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox

ListOfAvailableStories=["The Chase (Action)"
                                 ,"The Wizard’s Trial (Fantasy)"
                                 ,"Alien Encounter (Sci-Fi)"
                                 ,"The Whispering Room (Mystery)"
                                 ,"The Lost Map (Adventure)"
                                 ,"Midnight at the Lake (Horror)"
                                 ,"Awkward First Date (Romance)"
                                 ,"The Time Traveler’s Blunder (Historical)"
                                 ,"Monday Morning Mayhem (Slice of Life)"]
STORIES_TEXTS = [f"It was a night in the city. The target carried a [noun] that could destroy the world. "
                 "Agent Max had to [verb] through the crowded streets. "
                 "He finally [past participle verb] onto a speeding motorcycle and raced off [adverb], determined to save the day."]
main_window = tk.Tk()
main_window.title("MadLibs 1.0.01")
main_window.geometry("500x400")
main_window.maxsize(width=1000, height=800)

AdjText= tk.Label(main_window,text="Adjective", font="Roboto")
AdjText.grid(row=0, column=2)

NounText= tk.Label(main_window,text="Noun", font="Roboto")
NounText.grid(row=1, column=2)

VerbPresentText= tk.Label(main_window,text="Verb Present", font="roboto")
VerbPresentText.grid(row=2, column=2)

PastParticipleVerbText= tk.Label(main_window,text="Past Participle Verb" , font="roboto")
PastParticipleVerbText.grid(row=3, column=2)

Adverb=tk.Label(main_window,text="Adverb", font="roboto")
Adverb.grid(row=4,column=2)

EnterAdj=tk.Entry(main_window)
EnterAdj.grid(row=0, column=3)

EnterNoun=tk.Entry(main_window)
EnterNoun.grid(row=1,column=3)

EnterVerb=tk.Entry(main_window)
EnterVerb.grid(row=2,column=3)

EnterPastPartVerb = tk.Entry(main_window)
EnterPastPartVerb.grid(row=3,column=3)

EnterAdv=tk.Entry()
EnterAdv.grid(row=4,column=3)
#Function to get the entries
def getting_entries() :
    GetAdj = EnterAdj.get()
    GetNoun = EnterNoun.get()
    GetVerb = EnterVerb.get()
    GetPastPartVerb = EnterPastPartVerb.get()
    GetAverb = EnterAdv.get()
    CheckingAll = [GetAdj,GetNoun,GetVerb,GetAverb,GetPastPartVerb]

    STORIES_TEXTS = [
    f"It was a {GetAdj} night in the city.\n"
    f"The target carried a {GetNoun} that could destroy the world.\n"
    f"Agent Max had to {GetVerb} through the crowded streets.\n"
    f"He finally {GetPastPartVerb} onto a speeding motorcycle\n"
    f"and raced off {GetAverb}, determined to save the day.",

    f"In the ancient land of Eldrith, a {GetAdj} wizard held the last {GetNoun} of power.\n"
    f"To become a true sorcerer, young Elric had to {GetVerb} through the Forbidden Forest.\n"
    f"He {GetPastPartVerb} past shadow beasts and glowing mushrooms,\n"
    f"always moving {GetAverb} toward his destiny.",

    f"Today was supposed to be a {GetAdj} dinner party, but everything went wrong.\n"
    f"I accidentally dropped a {GetNoun} into the soup,\n"
    f"then tried to {GetVerb} it out with a ladle.\n"
    f"Instead, I {GetPastPartVerb} the tablecloth onto the ceiling fan,\n"
    f"which spun {GetAverb} until the guests were covered in gravy.",

    f"On a {GetAdj} planet orbiting Zarnok-5, I discovered a glowing {GetNoun} buried in the sand.\n"
    f"Suddenly, an alien ship began to {GetVerb} above me.\n"
    f"I was {GetPastPartVerb} into a beam of light\n"
    f"and floated {GetAverb} into their ship.",

    f"The old mansion had a {GetAdj} reputation.\n"
    f"Inside, I found a locked {GetNoun} and a strange message.\n"
    f"I decided to {GetVerb} the door open.\n"
    f"As soon as I did, the air {GetPastPartVerb},\n"
    f"and a cold wind blew {GetAverb} through the hallway.",

    f"Deep in a {GetAdj} jungle, we found an ancient {GetNoun} carved with clues.\n"
    f"Our team had to {GetVerb} through quicksand and monkey-filled trees.\n"
    f"We finally {GetPastPartVerb} the entrance to a hidden temple\n"
    f"and crept {GetAverb} inside.",

    f"The water was still and {GetAdj}.\n"
    f"I picked up a {GetNoun} floating near the dock.\n"
    f"Then I heard something {GetVerb} in the shadows.\n"
    f"I {GetPastPartVerb} my flashlight\n"
    f"and moved {GetAverb}—but something grabbed my ankle.",

    f"He showed up in a {GetAdj} suit, holding a {GetNoun} like it was a trophy.\n"
    f"We tried to {GetVerb} over dinner,\n"
    f"but he accidentally {GetPastPartVerb} his soup on me.\n"
    f"I smiled {GetAverb}, pretending not to care.",

    f"I woke up in a {GetAdj} version of ancient Rome.\n"
    f"A guard mistook my phone for a {GetNoun}\n"
    f"and tried to {GetVerb} me with a spear.\n"
    f"I {GetPastPartVerb} out of there {GetAverb},\n"
    f"promising to never touch the time machine again.",

    f"I woke up feeling {GetAdj}.\n"
    f"I couldn’t find my {GetNoun},\n"
    f"so I had to {GetVerb} to class in pajamas.\n"
    f"I had just {GetPastPartVerb} into my seat\n"
    f"when the teacher glared at me.\n"
    f"I pretended to take notes {GetAverb} while everyone laughed."
]
    if all(element for element in CheckingAll) :

        #to show the result window
        EnteredStoryName = ChooseStoryCB.get()
        #it find EnteredStoryName index using its pre-existed function in the ListOfAvailableStories
        GetIndexPos = ListOfAvailableStories.index(EnteredStoryName)
        #this print command need to be deleted after this prototype ends up
        print(GetIndexPos)
        #showing result need to be turned into another function to separate it from this pure function
        result_window = tk.Tk()
        result_window.title(EnteredStoryName)
        result_window.geometry("500x400")
        result_label = tk.Label(result_window, text=STORIES_TEXTS[GetIndexPos])
        result_label.pack()
        result_window.mainloop()

    else :
        messagebox.showwarning("Notice",message="Please, Fill Up the Fields")

ChooseStoryCB = ttk.Combobox(main_window, values=ListOfAvailableStories)
ChooseStoryCB.grid(row=8, column=2)
ChooseStoryCB.set(ListOfAvailableStories[0])

LaunchButton = tk.Button(main_window,text="Launch!", command=getting_entries,height=4,width=20).grid(row=7, column=3)

main_window.mainloop()
