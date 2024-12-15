import tkinter as tk
import ttkbootstrap as ttk                  # käytän tätä kun ei se pySimpleGUI anna lisensoida
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip    # tätä saattaa tarvita, tai sitten ei

def show_input():
    user_input = let_entry.get()            # hakee käyttäjän syötteen
    
def on_entry_click(event):                  # Piilotetaan paikkakunta-txt
    if let_entry.get() == placeholder_text:
        let_entry.delete(0, tk.END)         # tyhjentää
        let_entry.config(bootstyle="dark")  # vaihdetaan txt mustaksi tyhjennyksen jälkeen, huom bootstrapin omat värikoodit
        
def on_focusout(event):
    if let_entry.get() == "":
        let_entry.insert(0, placeholder_text) # tuodaan "SYötä paikkakunta" takaisin
        let_entry.config(bootstyle="secondary") # Secondary = harmaa

root = ttk.Window(title="Sää Hässäkkä", themename="superhero") # main window

window_width = 800                          # ikkunaa isommaksi avatessa, viilaillaan
window_height = 600

screen_width = root.winfo_screenwidth()     # hakkeroidaan win ja urkitaan näytön leveys/korkeus
screen_height = root.winfo_screenheight()

x_position = (screen_width // 2) - (window_width // 2) # näillä saa ikkunan aukeamaan eri kohtaan
y_position = (screen_width // 6) - (window_width // 6)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") # jotain ihan hepreaa, paneudutaan tarkemmin jos joku ei toimixD

frame = ttk.Frame(root, padding=10)         # raamit
frame.pack(fill=BOTH, expand=YES)

placeholder_text="Syötä paikkakunta"        # tämä txt häviää kun klikataan hiirellä

b1 = ttk.Label(frame)                       # Käyttäjän syöttämä paikkakunta
let_entry = ttk.Entry(frame, bootstyle="secondary") 
let_entry.insert(0, placeholder_text)
let_entry.pack(padx=10, pady=(0, 10), expand = True)
let_entry.bind("<Button-1>", on_entry_click) # hiiren painalluksella
let_entry.bind("<FocusOut>", on_focusout)   # pitäis txt tulla takaisin kun klikkaa pois, ei ilmeisesti toimi vielä

b2 = ttk.Button(root, text="Hae", bootstyle=SUCCESS) # hakunappi
b2.pack(side=BOTTOM, padx=5, pady=(0, 50))    # koitetaan saada paikkakunta-kentän perään tai alle, nyt ei jaksa



root.mainloop()