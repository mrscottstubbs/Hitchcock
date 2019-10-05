import tkinter as tk
import requests
from tkinter import font
from PIL import ImageTk,Image
from tkinter import PhotoImage

############################################################################
## History Arrays ##
first_searched_list = []
second_searched_list = []
key = '<API Key>'
############################################################################

def first_movieStuff(first_entry):
    first_movieName = first_entry
    url = 'http://www.omdbapi.com/?apikey=' + key + '&t=' + first_movieName
    response = requests.get(url)
    first_movieInfo = response.json()
    label1['text'] = first_format(first_movieInfo)
    first_searched_list.append(first_movieName + ',')
    history_label['text'] = first_searched_list

############################################################################

def first_format(movieInfo):
    try:
        name = movieInfo['Title']
        year = movieInfo['Year']
        genre = movieInfo['Genre']
        rating = movieInfo['Ratings'][1]['Value']
        #plot = movieInfo['Plot']
        last = 'Title: %s \n Year: %s \n Genre: %s \n Rate: %s ' % (name, year, genre, rating)
    except:
        last = 'Correct Spelling'
    return last

############################################################################

def second_movieStuff(second_entry):
    second_movieName = second_entry
    url = 'http://www.omdbapi.com/?apikey=' + key + '&t=' + second_movieName
    response = requests.get(url)
    second_movieInfo = response.json()

    label2['text'] = second_format(second_movieInfo)
    second_searched_list.append(second_movieName + ',')
    second_history_label['text'] = second_searched_list

############################################################################

def second_format(movieInfo):
    try:
        name = movieInfo['Title']
        year = movieInfo['Year']
        genre = movieInfo['Genre']
        rating = movieInfo['Ratings'][1]['Value']
        last = 'Title: %s \n Year: %s \n Genre: %s \n Rate: %s ' % (name, year, genre, rating)
    except:
        last = 'Correct Spelling'
    return last

############################################################################

root = tk.Tk()
root.title('Movie Comparer')
root.geometry("1100x600")
root.resizable(0,0)

############################################################################
## Background##
image = Image.open("movie.jpg")
filename = ImageTk.PhotoImage(image)
background_label = tk.Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

############################################################################

frame = tk.Frame(root, bg="gray", bd=5, height=750, width=7)
frame.place(relx =0.25, rely=0.1, relwidth=0.15, relheight=0.1, anchor='n')

btn1 = tk.Button(frame, bd = 2, command=lambda: first_movieStuff(first_entry.get()))
btn1.place(relx = 0.75, rely = 0, relwidth=0.25, relheight=1)

first_entry = tk.Entry(frame)
first_entry.place(relwidth=0.75, relheight=1)

############################################################################

second_frame = tk.Frame(root, bg="gray", bd=5, height=750, width=7)
second_frame.place(relx =0.75, rely=0.1, relwidth=0.15, relheight=0.1, anchor='n')

btn2 = tk.Button(second_frame, bd = 2, command=lambda: second_movieStuff(second_entry.get()))
btn2.place(relx = 0, rely = 0, relwidth=0.25, relheight=1)

second_entry = tk.Entry(second_frame)
second_entry.place(relx = 0.25, relwidth=0.75, relheight=1)

############################################################################

lower_frame1 = tk.Frame(root)
lower_frame1.place(relx=0.25, rely=0.25, relwidth=0.35, relheight=0.15, anchor='n')

label1 = tk.Label(lower_frame1, font=('Modern', 15))
label1.place(relwidth=1, relheight=1)

first_history = tk.Frame(root)
first_history.place(relx=0.25, rely=0.65, relwidth=0.35, relheight=0.1, anchor='n')
history_label = tk.Label(first_history, font=('Modern', 15))
history_label.place(relwidth=1, relheight=1)

############################################################################

lower_frame2 = tk.Frame(root)
lower_frame2.place(relx=0.75, rely=0.25, relwidth=0.35, relheight=0.15, anchor='n')

label2 = tk.Label(lower_frame2, font=('Modern', 15))
label2.place(relwidth=1, relheight=1)

second_history = tk.Frame(root)
second_history.place(relx=0.75, rely=0.65, relwidth=0.35, relheight=0.1, anchor='n')
second_history_label = tk.Label(second_history, font=('Modern', 15))
second_history_label.place(relwidth=1, relheight=1)

############################################################################

#compareBtn = tk.Button(root, bd=2, command=lambda: print())
#compareBtn.place(relx=0.5, rely=0.7)

#compareFrame = tk.Frame(root)
#compareFrame.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='s')
#compareLabel = tk.Label(compareFrame, font=('Modern', 15))
#compareLabel.place(relwidth=1, relheight=1)

############################################################################

root.mainloop()
