import tkinter as tk
from tkinter import ttk
import pyttsx3
import os
from PIL import Image
from tkinter import Tk, filedialog
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

braille_dict = {
        'a': '⠁',
        'b': '⠃',
        'c': '⠉',
        'd': '⠙',
        'e': '⠑',
        'f': '⠋',
        'g': '⠛',
        'h': '⠓',
        'i': '⠊',
        'j': '⠚',
        'k': '⠅',
        'l': '⠇',
        'm': '⠍',
        'n': '⠝',
        'o': '⠕',
        'p': '⠏',
        'q': '⠟',
        'r': '⠗',
        's': '⠎',
        't': '⠞',
        'u': '⠥',
        'v': '⠧',
        'w': '⠺',
        'x': '⠭',
        'y': '⠽',
        'z': '⠵',
        'A': '⠈⠇',  
        'B': '⠈⠃',  
        'C': '⠈⠉',  
        'D': '⠈⠙',  
        'E': '⠈⠑',  
        'F': '⠈⠋',  
        'G': '⠈⠛',  
        'H': '⠈⠓',  
        'I': '⠈⠊',  
        'J': '⠈⠚',  
        'K': '⠈⠅',  
        'L': '⠈⠇',  
        'M': '⠈⠍',  
        'N': '⠈⠝',  
        'O': '⠈⠕',  
        'P': '⠈⠏',  
        'Q': '⠈⠟',
        'R': '⠈⠗',  
        'S': '⠈⠎',  
        'T': '⠈⠞',  
        'U': '⠈⠥',  
        'V': '⠈⠧',  
        'W': '⠈⠺',  
        'X': '⠈⠭',  
        'Y': '⠈⠽',  
        'Z': '⠈⠵',  
        '0': '⠚',    
        '1': '⠁',    
        '2': '⠂',    
        '3': '⠃',   
        '4': '⠄',    
        '5': '⠅',    
        '6': '⠆',    
        '7': '⠇',    
        '8': '⠈',    
        '9': '⠉',    
        ' ': ' ',
        '!': '⠮',    
        '"': '⠐⠶',  
        '#': '⠼⠆',  
        '$': '⠸⠌',  
        '%': '⠸⠴',  
        '&': '⠈⠯',  
        "'": '⠄',   
        '(': '⠶⠶',  
        ')': '⠶⠤',  
        '*': '⠐⠶',  
        '+': '⠤⠤',  
        ',': '⠠',    
        '-': '⠤',    
        '.': '⠲',    
        '/': '⠤⠴',
        ':': '⠒',    
        ';': '⠲',    
        '<': '⠤⠐',
        '=': '⠤⠤',
        '>': '⠤⠤',  
        '?': '⠢',   
        '@': '⠈⠹',  
        '[': '⠈⠢',  
        '\\': '⠤⠤',
        ']': '⠈⠒',  
        '^': '⠤⠴',  
        '_': '⠤⠤',  
        '`': '⠄',    
        '{': '⠈⠶',  
        '|': '⠤⠴',  
        '}': '⠈⠶',  
        '~': '⠄⠤',
        '\n':' '
    }

braille_to_english = {'⠁': 'a',
                      '⠃': 'b',
                      '⠉': 'c',
                      '⠙': 'd',
                      '⠑': 'e',
                      '⠋': 'f',
                      '⠛': 'g',
                      '⠓': 'h',
                      '⠊': 'i',
                      '⠚': 'j',
                      '⠅': 'k',
                      '⠇': 'l',
                      '⠍': 'm',
                      '⠝': 'n',
                      '⠕': 'o',
                      '⠏': 'p',
                      '⠟': 'q',
                      '⠗': 'r',
                      '⠎': 's',
                      '⠞': 't',
                      '⠥': 'u',
                      '⠧': 'v',
                      '⠺': 'w',
                      '⠭': 'x',
                      '⠽': 'y',
                      '⠵': 'z',
                      '⠀': ' ',
                      '⠲': '.',
                      '⠂': ',',
                      '⠆': ';',
                      '⠒': ':',
                      '⠖': '!',
                      '⠦': '?',
                      '⠄': "'",
                      '⠐': '"',
                      '⠤': '-',
                      '⠜': '_',
                      '⠌': '(',
                      '⠬': ')',
                      '⠼': ']',
                      '⠴': '/',
                      '⠶': '*',
                      '⠖': '&',
                      '⠨': '#',
                      '⠸': '@',
                      '⠰': '%',
                      '⠂': '+',
                      '⠡': '=',
                      '⠌': '<',
                      '⠬': '>',
                      '⠼⠁': '1',
                      '⠼⠃': '2',
                      '⠼⠉': '3',
                      '⠼⠙': '4',
                      '⠼⠑': '5',
                      '⠼⠋': '6',
                      '⠼⠛': '7',
                      '⠼⠓': '8',
                      '⠼⠊': '9',
                      '⠼⠚': '0',
                      '⠠⠁': 'A',
                      '⠠⠃': 'B',
                      '⠠⠉': 'C',
                      '⠠⠙': 'D',
                      '⠠⠑': 'E',
                      '⠠⠋': 'F',
                      '⠠⠛': 'G',
                      '⠠⠓': 'H',
                      '⠠⠊': 'I',
                      '⠠⠚': 'J',
                      '⠠⠅': 'K',
                      '⠠⠇': 'L',
                      '⠠⠍': 'M',
                      '⠠⠝': 'N',
                      '⠠⠕': 'O',
                      '⠠⠏': 'P',
                      '⠠⠟': 'Q',
                      '⠠⠗': 'R',
                      '⠠⠎': 'S',
                      '⠠⠞': 'T',
                      '⠠⠥': 'U',
                      '⠠⠧': 'V',
                      '⠠⠺': 'W',
                      '⠠⠭': 'X',
                      '⠠⠽': 'Y',
                      '⠠⠵': 'Z'
                            }

########################################################################################################################################################################

def braille_to_text(braille):
    text = ""
    for char in braille:
        if char in braille_to_english:
            text += braille_to_english[char]
    return text

def generate_output_and_audio(braille_input):
    text_to_speech = pyttsx3.init()
    words = braille_input.split()
    final_word=""
    if english_frame.winfo_ismapped():
        english_output.delete("1.0","end")
        root.update()
    
    else:
        english_text_output.delete("1.0","end")
        root.update()
        english_text_output2.delete("1.0","end")
        root.update()
    print(braille_output)
    for word in words:
        root.update()
        text = braille_to_text(word)
        if english_frame.winfo_ismapped():
            english_output.insert(tk.END,text+"  ")
        elif english_text_frame.winfo_ismapped():
            english_text_output.insert(tk.END,text+"  ")
            english_text_output2.insert(tk.END,word+"  ")
        root.update()
        final_word+=text+" "
        text_to_speech.setProperty('rate', 140)  
        text_to_speech.say(text)
        text_to_speech.runAndWait()
        #time.sleep(delay_between_words)
    return final_word

def text_to_audio(text):
    main_frame.place_forget()
    #audio_frame.place(relx=0.5, rely=0.5, anchor="center")
    print(text)
    text_to_speech= pyttsx3.init()
    text_to_speech.setProperty('rate', 140)  
    text_to_speech.say(text)
    text_to_speech.runAndWait()
    return
    
def text_to_audio_save(text):
    text_tospeech = pyttsx3.init()
    text_to_speech.setProperty('rate', 140)  
    #engine.say(text)
    text_to_speech.save_to_file(text, 'output.mp3')
    text_to_speech.runAndWait()
    #play_audio('output.mp3')
  
def braille_save_file(final_pattern):
    with open("OUTPUT.txt", "w+", encoding="utf-8") as file:
           file.write(final_pattern)
   
def play_audio(audio_file):
    if os.name == 'nt':  
        os.system(f"start {audio_file}")  
    elif os.name == 'posix':  
        os.system(f"xdg-open {audio_file}")
    else:
        print("Unsupported operating system. Please open the audio file manually.")
        
########################################################################################################################################################################

def open_image(): 
     image_path = filedialog.askopenfilename(title="Select an image file",filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")],) 
     if image_path:
        image_text= pytesseract.image_to_string(Image.open(image_path))
        image_text=image_text[0:len(image_text)-2]+" "
        button_func2(image_text)

def open_text_file(): 
     text_path = filedialog.askopenfilename(title="Select a text file",filetypes=[("text files", "*.txt")],)  
     if text_path:
         with open(text_path, "r") as file:
             file_text=file.read()

         file_text+=" "
         button_func3(file_text)

def open_text_file_english(): 
     text_path = filedialog.askopenfilename(title="Select a text file",filetypes=[("text files", "*.txt")],)  
     if text_path:
         with open(text_path, "r",encoding="utf-8") as file:
             file_text=file.read()

         file_text+=" "
         button_func5(file_text)

def convert_braille_to_text():
    main_frame.place_forget()
    english_frame.place(relx=0.5, rely=0.5, anchor="center")
     
def convert_text_to_braille():
    main_frame.place_forget()
    braille_frame.place(relx=0.5, rely=0.5, anchor="center")

########################################################################################################################################################################

def button_func1():
        braille_output.delete("1.0","end")
        input_txt=entry_braille.get(1.0,"end-1c")+" "
        final_pattern=""
        braille_pattern =""
        word=""
    
        for char in (input_txt):
           if char is not None:
               braille_pattern+=braille_dict.get(char)
               print(braille_pattern)
               final_pattern+=braille_dict.get(char)
               if char.isspace():
                   #time.sleep()
                   braille_output.insert(tk.END,braille_pattern+"  ")
                   root.update()
                   text_to_audio(word)
                   word=""
                   braille_pattern=""
                   braille_pattern =""
               else:
                    word+=char
        with open("BRAILLE OUTPUT.txt", "w+", encoding="utf-8") as file:
                   file.write(final_pattern)

def button_func2(image_text):
    main_frame.place_forget()
    audio_frame.place(relx=0.5, rely=0.5, anchor="center")
    final_pattern=""
    braille_pattern =""
    word=""
    
    for char in (image_text):
           braille_pattern+=braille_dict.get(char)
           #print(type(braille_pattern))
           final_pattern+=braille_dict.get(char)
           if char.isspace():
               #time.sleep()
               audio_output2.insert(tk.END,word+"  ")
               audio_output.insert(tk.END,braille_pattern+"  ")
               root.update()
               text_to_audio(word)
               word=""
               braille_pattern=""
           
               braille_pattern =""
           else:
                word+=char
    with open("BRAILLE OUTPUT.txt", "w+", encoding="utf-8") as file:
           file.write(final_pattern)

def button_func3(file_text):
    print(file_text)
    main_frame.place_forget()
    text_frame.place(relx=0.5, rely=0.5, anchor="center")
    final_pattern=""
    braille_pattern =""
    word=""
    
    for char in (file_text):
       if char is not None:
           braille_pattern+=braille_dict.get(char)
           #print(type(braille_pattern))
           final_pattern+=braille_dict.get(char)
           if char.isspace():
               #time.sleep()
               text_output2.insert(tk.END,word+"  ")
               text_output.insert(tk.END,braille_pattern+"  ")
               root.update()
               text_to_audio(word)
               word=""
               braille_pattern=""
           
               braille_pattern =""
           else:
                word+=char
    with open("BRAILLE OUTPUT.txt", "w+", encoding="utf-8") as file:
           file.write(final_pattern)

def button_func4():
        braille_output.delete("1.0","end")
        input_braille=entry_english.get(1.0,"end-1c")
        words=generate_output_and_audio(input_braille)
        with open("ENGLISH OUTPUT.txt", "w+", encoding="utf-8") as file:
                   file.write(words)


def button_func5(input_braille):
        main_frame.place_forget()
        english_text_frame.place(relx=0.5, rely=0.5, anchor="center")
        braille_output.delete("1.0","end")
        print(input_braille)
        words=generate_output_and_audio(input_braille)
        with open("ENGLISH OUTPUT.txt", "w+", encoding="utf-8") as file:
                   file.write(words)


def back_to_main():
    if audio_frame.winfo_ismapped():
        audio_frame.place_forget()
    elif braille_frame.winfo_ismapped():
        braille_frame.place_forget()
    elif text_frame.winfo_ismapped():
        text_frame.place_forget()
    elif english_frame.winfo_ismapped():
        english_frame.place_forget()
    elif english_text_frame.winfo_ismapped():
        english_text_frame.place_forget()
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

########################################################################################################################################################################


root = tk.Tk()
root.title("B-E-T")
root.geometry("600x700")

background_color = '#222222'
root.configure(bg=background_color)

main_frame = tk.Frame(root, bg=background_color)
braille_frame = tk.Frame(root, bg=background_color)
audio_frame = tk.Frame(root, bg=background_color)
text_frame=tk.Frame(root, bg=background_color)
english_frame=tk.Frame(root, bg=background_color)
english_text_frame=tk.Frame(root, bg=background_color)

title_label = tk.Label(main_frame, text="B.E.T", font=('Arial', 20), fg="white", bg=background_color)
title_label.pack(pady=(20, 10))

title_label = tk.Label(main_frame, text="(BRAILLE-ENGLISH-TRANSLATOR)", font=('Arial', 20), fg="white", bg=background_color)
title_label.pack(pady=(20, 10))

title_label = tk.Label(main_frame, text="MAIN MENU\n", font=('Arial', 15), fg="white", bg=background_color)
title_label.pack(pady=(20, 10))



style = ttk.Style()
style.configure('TButton', foreground='blue', background='blue', borderwidth=0, relief="flat", font=('Arial', 12))
style.map('TButton', background=[('active', 'blue')], foreground=[('active', 'white')])

button1 = ttk.Button(main_frame, text="Input English text to Braille", command=convert_text_to_braille)
button2 = ttk.Button(main_frame, text="English from image to Braille", command=open_image)
button3 = ttk.Button(main_frame, text="English from text File To Braille",command=open_text_file)
button4 = ttk.Button(main_frame, text="Input Braille Text to English",command=convert_braille_to_text)
button5 = ttk.Button(main_frame, text="Braille from text file to English",command=open_text_file_english)
button6 = ttk.Button(main_frame, text="Exit",command=root.destroy)

button1.config(width=25)
button2.config(width=25)
button3.config(width=25)
button4.config(width=25)
button5.config(width=25)
button6.config(width=25)

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)
button6.pack(pady=10)
########################################################################################################################################################################
label_braille = tk.Label(braille_frame, text="\nENGLISH TEXT FROM KEYBOARD TO BRAILLE CONVERSION\n", bg=background_color, fg="white", font=('Arial', 13))
label_braille.pack()

label_braille = tk.Label(braille_frame, text="\nENTER THE INPUT TEXT\n", bg=background_color, fg="white", font=('Arial', 13))
label_braille.pack()

entry_braille = tk.Text(braille_frame, height=10, width=40, wrap="word", font=('Arial', 12))
entry_braille.pack(pady=10)

convert_button_braille = ttk.Button(braille_frame, text="Convert to Braille", command=button_func1)
convert_button_braille.pack(pady=10)

label_braille = tk.Label(braille_frame, text="\nTHE OUTPUT BRAILLE IS\n", bg=background_color, fg="white", font=('Arial', 13))
label_braille.pack()

braille_output = tk.Text(braille_frame, height=10, width=40, wrap="word", font=('Arial', 12))
braille_output.pack(pady=10)


back_button_braille = ttk.Button(braille_frame, text="Back", command=back_to_main)
back_button_braille.pack(pady=15)
########################################################################################################################################################################
label_audio = tk.Label(audio_frame, text="\nRECOGNIZE ENGLISH TEXT FROM IMAGE AND COVERSION TO BRAILLE\n", bg=background_color, fg="white", font=('Arial', 13))
label_audio.pack()

label_audio3 = tk.Label(audio_frame, text="THE INPUT TEXT RECOGNIZED IS\n", bg=background_color, fg="white", font=('Arial', 12))
label_audio3.pack()

audio_output2 = tk.Text(audio_frame, height=10, width=40, wrap="word", font=('Arial', 12))
audio_output2.pack(pady=10)

label_audio = tk.Label(audio_frame, text="\nTHE OUTPUT BRAILLE IS\n", bg=background_color, fg="white", font=('Arial', 12))
label_audio.pack()


audio_output = tk.Text(audio_frame, height=10, width=40, wrap="word", font=('Arial', 12))
audio_output.pack(pady=10)

audio_label = tk.Label(audio_frame, text="", bg=background_color, fg="white", font=('Arial', 12))
audio_label.pack(pady=10)

back_button_audio = ttk.Button(audio_frame, text="Back", command=back_to_main)
back_button_audio.pack(pady=15)
########################################################################################################################################################################
text_label = tk.Label(text_frame, text="\nREAD ENGLISH TEXT FROM A TEXT FILE AND CONVERSION TO BRAILLE\n", bg=background_color, fg="white", font=('Arial', 13))
text_label.pack()

text_label = tk.Label(text_frame, text="\nTHE INPUT IS\n", bg=background_color, fg="white", font=('Arial', 12))
text_label.pack()

text_output2 = tk.Text(text_frame, height=10, width=40, wrap="word", font=('Arial', 12))
text_output2.pack(pady=10)

text_label = tk.Label(text_frame, text="\nTHE BRAILLE OUTPUT IS\n", bg=background_color, fg="white", font=('Arial', 12))
text_label.pack()

text_output = tk.Text(text_frame, height=10, width=40, wrap="word", font=('Arial', 12))
text_output.pack(pady=10)

text_label = tk.Label(text_frame, text="", bg=background_color, fg="white", font=('Arial', 12))
text_label.pack(pady=10)

back_button_text = ttk.Button(text_frame, text="Back", command=back_to_main)
back_button_text.pack(pady=15)
########################################################################################################################################################################
label_english = tk.Label(english_frame, text="\nBRAILLE TEXT FROM KEYBOARD TO ENGLISH CONVERSION", bg=background_color, fg="white", font=('Arial', 13))
label_english.pack()

label_english1= tk.Label(english_frame, text="\nENTER THE BRAILLE TEXT\n", bg=background_color, fg="white", font=('Arial', 12))
label_english1.pack()


entry_english = tk.Text(english_frame, height=10, width=40, wrap="word", font=('Arial', 12))
entry_english.pack(pady=10)

convert_button_english = ttk.Button(english_frame, text="Convert to English", command=button_func4)
convert_button_english.pack(pady=10)

label_english1= tk.Label(english_frame, text="\nTHE OUTPUT IN ENGLISH IS\n", bg=background_color, fg="white", font=('Arial', 12))
label_english1.pack()

english_output = tk.Text(english_frame, height=10, width=40, wrap="word", font=('Arial', 12))
english_output.pack(pady=10)


back_button_english = ttk.Button(english_frame, text="Back", command=back_to_main)
back_button_english.pack(pady=15)
########################################################################################################################################################################
english_text_label = tk.Label(english_text_frame, text="\n READ BRAILLE TEXT FROM TEXT FILE AND CONVERT TO ENGLISH", bg=background_color, fg="white", font=('Arial', 13))
english_text_label.pack()

english_text_label = tk.Label(english_text_frame, text="\n\nTHE INPUT BRAILLE TEXT IS\n", bg=background_color, fg="white", font=('Arial', 12))
english_text_label.pack()

english_text_output2= tk.Text(english_text_frame, height=10, width=40, wrap="word", font=('Arial', 12))
english_text_output2.pack(pady=10)

english_text_label = tk.Label(english_text_frame, text="\nTHE OUTPUT ENGLISH IS\n", bg=background_color, fg="white", font=('Arial', 12))
english_text_label.pack()

english_text_output = tk.Text(english_text_frame, height=10, width=40, wrap="word", font=('Arial', 12))
english_text_output.pack(pady=10)

english_text_label = tk.Label(english_text_frame, text="", bg=background_color, fg="white", font=('Arial', 12))
english_text_label.pack(pady=10)

back_button_english_text = ttk.Button(english_text_frame, text="Back", command=back_to_main)
back_button_english_text.pack(pady=15)
#########################################################################################################################################################################
main_frame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()

