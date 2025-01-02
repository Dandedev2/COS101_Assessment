from tkinter import Button, Entry, Label, StringVar, Tk

#creating a najia dictionary
window = Tk()

#width and length of window 
window.geometry("600x250")

#dictionary title
window.title = ("Hausa Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

hausa_dict = {
    'zo': 'Come',
    'kia': 'Head',
    'je': 'Go',
    'sannu': 'Hello',
    'kudi': 'Money',
    'na gode': 'Thank you',
    'gobe': 'Tomorrow',
    'babba': 'Big',
    'yau': 'Today',
    'dare': 'Night',
    'dogon yaro': 'neem tree',
    'rakee': 'Sugar cane',
    'ruwa': 'Water',
    'dadi': 'delicious',
    'dauka': 'take',
    'kyau': 'beautiful',
    'uwa': 'mum',
    'baba': 'dad',
    'rubutu': 'text'
}


def search(word):
    if word in hausa_dict:
        result.set(hausa_dict[word])
        print(hausa_dict[word])
        
    else:
        result.set("Not Found")
        print("Not Found")
        
search_btn = Button(window, text='search', command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()
    
