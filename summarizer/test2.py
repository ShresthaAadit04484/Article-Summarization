import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Article Summarizer")
root.geometry('1200x600')
root.config(bg="#EEF7FF")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

# Create left and right frames
left_frame = tk.Frame(root, width=300, height=400, bg='#CDE8E5')
left_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
right_frame = tk.Frame(root, width=800, height=400, bg='#CDE8E5')
right_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

# Create widgets in the left frame
tlabel = tk.Label(left_frame, text="Title", bg='#CDE8E5')
tlabel.grid(row=0, column=0, pady=(10, 5), sticky="w")

title = tk.Text(left_frame, height=1, width=40, bg="#EEF7FF")
title.config(state='disabled')
title.grid(row=1, column=0, pady=5, padx=5, sticky="w")

auth_label = tk.Label(left_frame, text="Author", bg='#CDE8E5')
auth_label.grid(row=2, column=0, pady=(10, 5), sticky="w")

author = tk.Text(left_frame, height=1, width=40, bg="#EEF7FF")
author.config(state="disabled")
author.grid(row=3, column=0, pady=5, padx=5, sticky="w")

p_label = tk.Label(left_frame, text="Publication Date", bg='#CDE8E5')
p_label.grid(row=4, column=0, pady=(10, 5), sticky="w")

publication = tk.Text(left_frame, height=1, width=40, bg="#EEF7FF")
publication.config(state="disabled")
publication.grid(row=5, column=0, pady=5, padx=5, sticky="w")

senti_label = tk.Label(left_frame, text="Sentiment Analysis", bg='#CDE8E5')
senti_label.grid(row=6, column=0, pady=(10, 5), sticky="w")

sentiment = tk.Text(left_frame, height=1, width=40, bg="#EEF7FF")
sentiment.config(state="disabled")
sentiment.grid(row=7, column=0, pady=5, padx=5, sticky="w")

# Create widgets in the right frame
sum_label = tk.Label(right_frame, text="Summary", bg='#CDE8E5')
sum_label.grid(row=0, column=0, pady=(10, 5), sticky="w")

summary = tk.Text(right_frame, height=25, width=100, bg="#EEF7FF")
summary.config(state="disabled")
summary.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

# Create URL entry at the bottom
url_label = tk.Label(root, text="URL:", bg='#EEF7FF')
url_label.grid(row=1, column=0, columnspan=2, pady=(10, 5))

url_text = tk.Text(root, height=1, width=140, bg="#EEF7FF")
url_text.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="ew")

# Add summarize button
btn = tk.Button(root, text="Summarize")
btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
