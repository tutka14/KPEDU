import tkinter as tk
import ttkbootstrap as ttk                  # käytän tätä kun ei se pySimpleGUI anna lisensoida
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip    # tätä saattaa tarvita, tai sitten ei

self = ttk.Window(title="Sää Hässäkkä", themename="superhero") # main window
placeholder_text="Syötä paikkakunta"        # tämä txt häviää kun klikataan hiirellä



# Alla oleva lainattu hangmanista placeholderiksi, joutuu muokkailla ja jakaa yms

class sää:
    def __init__(self): # jaetaan user interface osioihin (3)
        layout = [
            [self._päivän_sää_frame(),        # Päivän sää (paikkakunta,vkon pvä, ikoni(?), lämpötila)
             self._syötä_paikkakunta_frame(),       # tähän etsi paikkakunta syöttölaatikko ja hakunappi
             ],
            [
                self._build_guessed_word_frame(),   # 3pvä sää (vkon pvä, ikoni(?), lämpötila))
            ],
        ]
        self._window = ttk.Window(title="Sää", themename="superhero",layout=layout, finalize=True)
        self._canvas = self._window["-CANVAS-"]
        
        
        
        
        
    # päivän sää frame
    
    def _päivän_sää_frame(self):
        return self._canvas(
            "Päivän sää",                   # tähän suoraan input haettu paikkakunta?
            [
                [
                    tk.Frame(
                        key="-CANVAS-",
                        canvas_size=(200, 400), # osion koko
                        graph_bottom_left=(0, 0), # etäisyys vasemmalta alhaalta
                        graph_top_right=(200, 400), # etäisyys oikealta ylhäältä
                    )
                ]
            ],
            font="Any 20",
        )
     
     # syötä paikkakunta frame
     
    def show_input():
        user_input = let.entry.get()            # hakee käyttäjän syötteen
    
    def on_entry_click(event):                  # Piilotetaan paikkakunta-txt
        if let_entry.get() == placeholder_text:
            let_entry.delete(0, tk.END)         # tyhjentää
            let_entry.config(bootstyle="dark")  # vaihdetaan txt mustaksi tyhjennyksen jälkeen, huom bootstrapin omat värikoodit
        
    def on_focusout(event):
        if let_entry.get() == "":
            let_entry.insert(0, placeholder_text) # tuodaan "SYötä paikkakunta" takaisin
            let_entry.config(bootstyle="secondary") # Secondary = harmaa

    def _syötä_paikkakunta_frame(self):
        b1 = ttk.Label(frame)                       # Käyttäjän syöttämä paikkakunta
        let_entry = ttk.Entry(frame, bootstyle="secondary") 
        let_entry.insert(0, placeholder_text)
        let_entry.pack(padx=10, pady=(0, 10), expand = True)
        let_entry.bind("<Button-1>", on_entry_click) # hiiren painalluksella
        let_entry.bind("<FocusOut>", on_focusout)   # pitäis txt tulla takaisin kun klikkaa pois, ei ilmeisesti toimi vielä
        b2 = ttk.Button(self, text="Hae", bootstyle=SUCCESS) # hakunappi
        b2.pack(side=LEFT, padx=5, pady=(0, 50))    # koitetaan saada paikkakunta-kentän perään tai alle, nyt ei jaksa
        
    

        




window_width = 800                          # ikkunaa isommaksi avatessa, viilaillaan
window_height = 600

screen_width = self.winfo_screenwidth()     # hakkeroidaan win ja urkitaan näytön leveys/korkeus
screen_height = self.winfo_screenheight()

x_position = (screen_width // 2) - (window_width // 2) # näillä saa ikkunan aukeamaan eri kohtaan
y_position = (screen_width // 6) - (window_width // 6)

self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") # jotain ihan hepreaa, paneudutaan tarkemmin jos joku ei toimixD

frame = ttk.Frame(self, padding=10)         # raamit
frame.pack(fill=BOTH, expand=YES)





self.mainloop()