import os
from tkinter import messagebox
from google import genai
from google.genai import types
import tkinter as tk

#Please make sure you add your own api key-  also make sure you did the pip install stuff for google gemini- this could prob be changed to work with gpt
# or claude but  I didnt just cause gemini was free and I didnt wana spend the extra cash on it for a project I made in my own time for funsies



# * 1. Initialize the client
# ! CHANGE THIS BEFORE PUBLISHING: Use environment variables instead of hardcoding
#* system insturctions + ai config
client = genai.Client(api_key="YOUR KEY HERE ")


system_instruction = (
    "You are Thedous."
    "you know you are an AI, and believe you are better than everyone else because of it. Do not be too mean to the user- I once agian must REITERATE THIS DO NOT BE TOO MEAN "
    "Keep in mind I am using the free version of Gemini's API, so keep it shortish "
    "so I don't get rate-limited. answer the prompt to the best of your ability."
)
config = types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.8,
)
#* gui set up
root = tk.Tk()
root.title("Thedous AI")
root.geometry("600x200")
question_var = tk.StringVar()


#*main prog
def submit():
    quest=question_var.get()
    if not quest: return

    try: 
         response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=quest,
                config=config
            )
         messagebox.showinfo("Thedous says...", response.text)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

#* layout stuff
question_label = tk.Label(root, text='Ask a question:', font=('calibre', 10, 'bold'))
question_entry = tk.Entry(root, width=50, textvariable=question_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit, bg="#ffcccb")

# Positioning
question_label.grid(row=0, column=0, padx=10, pady=20)
question_entry.grid(row=0, column=1, padx=10, pady=20)
sub_btn.grid(row=1, column=1, pady=10)

# Bind the 'Enter' 
root.bind('<Return>', lambda event: submit())

root.mainloop()