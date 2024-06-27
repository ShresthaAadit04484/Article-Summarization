import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Article Summarizer")
root.geometry('1200x600')
root.config(bg="skyblue")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)

# Create left and right frames
left_frame = tk.Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
right_frame = tk.Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

# Create widgets in the left frame
tlabel = tk.Label(left_frame, text="Title", bg='grey')
tlabel.pack(pady=(10, 5))

title = tk.Text(left_frame, height=1, width=40, bg="#dddddd")
title.config(state='disabled')
title.pack(pady=5)

alabel = tk.Label(left_frame, text="Author", bg='grey')
alabel.pack(pady=(10, 5))

author = tk.Text(left_frame, height=1, width=40, bg="#dddddd")
author.config(state='disabled')
author.pack(pady=5)

plabel = tk.Label(left_frame, text="Publication", bg='grey')
plabel.pack(pady=(10, 5))

publication = tk.Text(left_frame, height=1, width=40, bg="#dddddd")
publication.config(state='disabled')
publication.pack(pady=5)

slabel = tk.Label(left_frame, text="Sentiment Analysis", bg='grey')
slabel.pack(pady=(10, 5))

sentiment = tk.Text(left_frame, height=1, width=40, bg="#dddddd")
sentiment.config(state='disabled')
sentiment.pack(pady=5)

# Create widgets in the right frame
slabel = tk.Label(right_frame, text="Summary", bg='grey')
slabel.pack(pady=(10, 5))

summary = tk.Text(right_frame, height=20, width=80, bg="#dddddd")
summary.config(state='disabled')
summary.pack(pady=5)

# Create URL entry at the bottom
ulabel = tk.Label(root, text="URL", bg='skyblue')
ulabel.grid(row=1, column=0, columnspan=2, pady=(10, 5))

url = tk.Text(root, height=1, width=100, bg="#dddddd")
url.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10))

# Add summarize button
btn = tk.Button(root, text="Summarize")
btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
