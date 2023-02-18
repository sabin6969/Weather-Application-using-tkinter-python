import tkinter as tk
from tkinter import ttk
import requests

class App:
    def __init__(self):
        root=tk.Tk()
        #---title----#
        root.title("Weather App")
        #---dimensions--#
        root.geometry('500x500')
        root.minsize(500,500)
        root.maxsize(500,500)
        #---icon-----#
        root.iconbitmap('cloudy.ico')
        #---background color---#
        root.configure(bg='#2596be')
        #---name label---#
        name_label=tk.Label(root,text="Weather App",fg='blue',bg='#2596be',font=("Serif",30,'bold'))
        name_label.place(x=125,y=50,height=40)
        #---combobox---#
        name_of_city=tk.StringVar()
        cities_name=ttk.Combobox(root,textvariable=name_of_city,width=40,state='readonly')
        cities_name['values']=('Select City',"Pokhara","Kathmandu","Dharan","Butwal","Damak","Biratnagar")
        cities_name.current(0)
        cities_name.focus()
        cities_name.place(x=125,y=120,height=30)
        #------get_details function------#
        def get_details():
            city=name_of_city.get()
            api='30d4741c779ba94c470ca1f63045390a'
            data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}")
            dct=data.json()
            for key,value in dct.items():
                if key=='weather':
                    details=value[0].values()
                    for count,i in enumerate(details):
                        if count==2:
                            # print(i)
                            weather_condiion=tk.Label(root,text="{}".format(i),font=("Times New Roman",10),bg='#2596be',fg='white')
                            weather_condiion.place(x=320,y=210,height=30)
                        else:
                            pass
                for key,values in dct.items():
                    if key=='main':
                        kelvin = values.get('feels_like')
                        celsius = kelvin - 273.15
                        celsius=round(celsius,2)
                        weather_temp=tk.Label(root,text="{}".format(celsius),bg='#2596be',fg='white',font=("Times New Roman",10))
                        weather_temp.place(x=290,y=230,height=30)
        #----button----#
        get_weather=tk.Button(root,text="Get Details",command=get_details)
        get_weather.place(x=220,y=180,height=20)
        #----weather details labels----#
        weather_condiion=tk.Label(root,text="Weather Condition: ",font=("Times New Roman",8),bg='#2596be',fg='white')
        weather_condiion.place(x=210,y=210,height=30)
        weather_temp=tk.Label(root,text="Temperature",bg='#2596be',fg='white')
        weather_temp.place(x=210,y=230,height=30)
        root.mainloop()

if __name__=="__main__":
    weather=App()