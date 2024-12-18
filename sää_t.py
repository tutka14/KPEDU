import tkinter as tk
import ttkbootstrap as ttk                  # käytän tätä kun ei se pySimpleGUI anna lisensoida
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip    # tätä saattaa tarvita, tai sitten ei

placeholder_text="Syötä paikkakunta"        # tämä txt häviää kun klikataan hiirellä


class sää:
    def __init__(self):                     # main window tässä
        self.app = ttk.Window(title="Sää haku", themename="superhero")
        self.placeholder_text = "Syötä paikkakunta"
        self.setup_window_geometry()    # koko ikkuna
        self.setup_grid()               # tällä jaetaan meidän osiot
        self.create_widgets()           #näillä tehdään ne meidän hilavitkuttimet
        self.app.mainloop()
        
        
    def setup_window_geometry(self):          # ikkunan geometria, näitä voidaan viilailla
        window_width = 500
        window_height = 400
        
        screen_width = self.app.winfo_screenmmwidth()
        screen_height = self.app.winfo_screenheight()
        
        x_position = (screen_width // 2) - (window_width // 2) # näillä saa ikkunan aukeamaan eri kohtaan
        y_position = (screen_width // 2) - (window_width // 2) # mulla ultrawide näyttö, eli joudutte näitä muokkaamaan että teillä keskellä ruutua 
        
        self.app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        
    def setup_grid(self):
        for i in range(4):              # 4 rows (ylähäältä alaspäin)
            self.app.grid_rowconfigure(1, weight=1)
        for j in range(5):              # 5 columns (vasemmalta oikealle)
            self.app.grid_columnconfigure(j, weight=1)
        
        
    def create_widgets(self):               # sitten meidän widgetit, eli päivän säät yms
        päivän_sää = ttk.Button(self.app, text="Päivän sää", bootstyle="warning")
        päivän_sää.grid(row=0, column=0, columnspan=2, rowspan=3, pady=2)
        ToolTip(päivän_sää, text="päivän sää") # tooltipit että voidaan etsiä missä menee widgettien rajat että saadaan ehkä oikeille paikoille :D

        paikkakunta = ttk.Label(self.app, text="Syötä Paikkakunta", bootstyle="primary")
        paikkakunta.grid(row=0, column=3, columnspan=2, rowspan=1, pady=2)
        ToolTip(paikkakunta, text="paikkakunta")

        kolmen_paivan = ttk.Label(self.app, text="3 päivän sää", bootstyle="success")
        kolmen_paivan.grid(row=3, column=3, columnspan=2, rowspan=3, pady=2)
        ToolTip(kolmen_paivan, text="kolmen_paivan")
        
        # hakukenttä, 3 columns
        self.let_entry = ttk.Entry(self.app, bootstyle="secondary")
        self.let_entry.insert(0, "Syötä paikkakunta")  # Placeholder text
        self.let_entry.grid(row=0, column=3, columnspan=3, rowspan=2, padx=10, pady=10)
        self.let_entry.bind("<Button-1>", self.on_entry_click)
        self.let_entry.bind("<FocusOut>", self.on_focusout)

        b2 = ttk.Button(self.app, text="Hae", bootstyle=SUCCESS) # tähän napin funktio "command=self.hae)
        b2.grid(row=0, column=5, padx=10, pady=10, sticky=E)
        
        
    def show_input(self):
        user_input = self.let_entry.get()            # hakee käyttäjän syötteen
    
    
    def on_entry_click(self, event):                  # Piilotetaan paikkakunta-txt
        if self.let_entry.get() == placeholder_text:
            self.let_entry.delete(0, tk.END)         # tyhjentää
            self.let_entry.config(bootstyle="dark")  # vaihdetaan txt mustaksi tyhjennyksen jälkeen, huom bootstrapin omat värikoodit
    
        
    def on_focusout(self, event):
        if self.let_entry.get() == "":
            self.let_entry.insert(0, placeholder_text) # tuodaan "SYötä paikkakunta" takaisin
            self.let_entry.config(bootstyle="secondary") # Secondary = harmaa
        
        
        
# ajetaan appi
if __name__ == "__main__":
    sää()