import requests
import json
import datetime
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import geocoder
import ttkbootstrap as ttk


# Tkinter GUI-koodi
root = Tk()
root.title("Weather App")
root.geometry("450x700")
style = ttk.Style(theme="superhero")

api_key = "732e0d22eef76e52836bc01989affc8f"
placeholder_text = "Syötä paikkakunta"

# PDF-raportin luontifunktio
def create_pdf(city, country, current_temperature, humidity, temp_min, temp_max):
    report_name = f"{city}_saatiedot.pdf"
    c = canvas.Canvas(report_name, pagesize=letter)
    width, height = letter
    
    # Lisää otsikko
    c.setFont("Helvetica-Bold", 24)
    c.drawString(72, height - 72, f"Säätiedot paikkakunnalle: {city}, {country}")
    
    # Lisää säätiedot
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 100, f"Nykyinen lämpötila: {current_temperature}")
    c.drawString(72, height - 120, f"Ilmankosteus: {humidity}%")
    c.drawString(72, height - 140, f"Päivän ylin lämpötila: {temp_max}")
    c.drawString(72, height - 160, f"Päivän alin lämpötila: {temp_min}")
    
    # Tallenna PDF
    c.save()
    print(f"Raportti tallennettu: {report_name}")



# Paikkakunnan tarkistus
def etsi_paikkakunta(paikkakunta):
    tunnetut_paikkakunnat = [...]  # Lisää tunnetut paikkakunnat tähän
    return paikkakunta in tunnetut_paikkakunnat

def virheilmoitus(paikkakunta):
    messagebox.showerror("Virhe", f"Hakemaasi paikkakuntaa '{paikkakunta}' ei löydy.")

# Sijainnin haku IP-osoitteen perusteella
def oma_sijainti():
    g = geocoder.ip('me')
    if g.latlng is None:
        messagebox.showerror("Virhe", "Sijaintia ei voitu määrittää.")
        return

    # API kutsu käyttäen IP-osoitetta
    api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={g.latlng[0]}&lon={g.latlng[1]}&units=metric&appid={api_key}")
    api = json.loads(api_request.content)

    # Lämpötilat
    y = api['main']
    current_temperature = int(y['temp']), "°C"
    humidity = int(y['humidity'])
    temp_min = int(y['temp_min']), "°C"
    temp_max = int(y['temp_max']), "°C"

    # Maatiedot
    z = api['sys']
    country = z['country']
    city = api['name']

    # Lisätään saadut tiedot
    lable_temp.configure(text=current_temperature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=temp_max)
    min_temp.configure(text=temp_min)
    lable_country.configure(text=country)
    lable_citi.configure(text=city)

    # Luo PDF-raportti
    create_pdf(city, country, current_temperature[0], humidity, temp_min[0], temp_max[0])


# Pvm ja sen sijoitus
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A'), bg='white', font=("bold", 15))
date.place(x=110, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=200, y=130)

# Aika ja sen sijoitus
hour = Label(root, text=dt.strftime("%H:%M"), bg='white', font=("bold", 15))
hour.place(x=110, y=160)

# Päivä/-Yö-kuvakkeiden valinta kellonajan mukaan
if int((dt.strftime('%H'))) >= 8 & int((dt.strftime('%H'))) <= 6: #klo 8-18(6) välillä
	img = ImageTk.PhotoImage(Image.open('yo.png'))
	panel = Label(root, image=img)
	panel.place(x=125, y=520)
else:
	img = ImageTk.PhotoImage(Image.open('paiva.png'))
	panel = Label(root, image=img)
	panel.place(x=125, y=520)


# Hakee käyttäjän syötteen
def city_name():
    user_input = city_entry.get()
    
    try:
        # API kutsu
        api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")
        
        # Tarkista vastauskoodi
        if api_request.status_code != 200:
            # Kaupunkia ei löytynyt
            messagebox.showerror("Virhe", f"Hakemaasi paikkakuntaa '{user_input}' ei löydy.")
            return
        
        api = json.loads(api_request.content)

        # Lämpötilat
        y = api['main']
        current_temperature = int(y['temp']), "°C"
        humidity = int(y['humidity'])
        temp_min = int(y['temp_min']), "°C"
        temp_max = int(y['temp_max']), "°C"

        # Maatiedot
        z = api['sys']
        country = z['country']
        city = api['name']

        # Lisätään saadut tiedot
        lable_temp.configure(text=current_temperature)
        lable_humidity.configure(text=humidity)
        max_temp.configure(text=temp_max)
        min_temp.configure(text=temp_min)
        lable_country.configure(text=country)
        lable_citi.configure(text=city)

        # Tyhjennä virheilmoitus, jos aiemmin näytetty
        print("")

        # Luo PDF-raportti
        create_pdf(city, country, current_temperature[0], humidity, temp_min[0], temp_max[0])

    except requests.exceptions.RequestException as e:
        # Yleinen virhe, esimerkiksi verkkoyhteys
        print(f"Tapahtui virhe API-pyynnössä. Tarkista verkkoyhteys.")
    


    
        
# Hakunappi
city_nameButton = Button(root, text="Haku", command=city_name)
city_nameButton.grid(row=0, column=3, pady=10, padx=5, stick=W+N+E+S)

# Paikkakunnan syöttökenttä
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=0, column=1, ipady=10, pady=10, stick=W+N+E+S)
city_entry.insert(0, placeholder_text)

# Funktio, joka tyhjentää syöttökentän
def clear_entry(event):
    if city_name.get() == placeholder_text:  # Tarkista onko placeholder-teksti
        city_entry.delete(0, END)  # Tyhjennä syöttökenttä
 
# Lisää tapahtumankäsittelijä hiiren klikkaukselle
city_entry.bind("<Button-1>", clear_entry)

# Maan nimi
lable_citi = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_citi.place(x=135, y=63)

lable_country = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_country.place(x=225, y=63)

# Tämänhetkinen lämpötila
lable_temp = Label(root, text="...", width=0, bg='white', font=("Helvetica", 110), fg='black')
lable_temp.place(x=40, y=220)

# Päivän ylin-, alinlämpötila ja ilmankosteus
humi = Label(root, text="Ilmankosteus: ", width=0, bg='white', font=("bold", 15))
humi.place(x=3, y=400)

lable_humidity = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_humidity.place(x=200, y=400)

maxi = Label(root, text="Päivän ylin: ", width=0, bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=200, y=430)

mini = Label(root, text="Päivän alin: ", width=0, bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
min_temp.place(x=200, y=460)

# huom
note = Label(root, text="Lämpötilat Celsius-asteina", bg='white', font=("italic", 10))
note.place(x=95, y=495)

# Sijainnin haku -nappi
loca = PhotoImage(file=r"C:\Users\PC\Documents\python\scraper\loca.png")
PhotoImage = loca.subsample(25, 25)
locationButton = Button(root, text="Oma sijainti", image=PhotoImage, compound=LEFT, command=oma_sijainti)
locationButton.grid(row=0, column=0, pady=10, padx=5, stick=W+N+E+S)

root.mainloop()