#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Make a complete Application that takes CSV file and find the Mean ,Meadian and Mode by using
# Tkinter.


# In[3]:


import tkinter as tk
from tkinter import filedialog
import csv
from statistics import mean, median
from collections import Counter

class CSVStatsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV Stats Calculator")

        self.file_path_label = tk.Label(self.master, text="CSV File:")
        self.file_path_label.grid(row=0, column=0, padx=10, pady=10)

        self.file_path_entry = tk.Entry(self.master, width=50)
        self.file_path_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.calculate_button = tk.Button(self.master, text="Calculate Stats", command=self.calculate_stats)
        self.calculate_button.grid(row=1, column=1, pady=10)

        self.mean_label = tk.Label(self.master, text="Mean:")
        self.mean_label.grid(row=2, column=0, padx=10, pady=10)

        self.mean_result = tk.Label(self.master, text="")
        self.mean_result.grid(row=2, column=1, padx=10, pady=10)

        self.median_label = tk.Label(self.master, text="Median:")
        self.median_label.grid(row=3, column=0, padx=10, pady=10)

        self.median_result = tk.Label(self.master, text="")
        self.median_result.grid(row=3, column=1, padx=10, pady=10)

        self.mode_label = tk.Label(self.master, text="Mode:")
        self.mode_label.grid(row=4, column=0, padx=10, pady=10)

        self.mode_result = tk.Label(self.master, text="")
        self.mode_result.grid(row=4, column=1, padx=10, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def calculate_stats(self):
        file_path = self.file_path_entry.get()

        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                data = [float(row[0]) for row in reader]

                if not data:
                    raise ValueError("CSV file is empty.")

                mean_value = mean(data)
                median_value = median(data)
                mode_value = Counter(data).most_common(1)[0][0]

                self.mean_result.config(text=f"{mean_value:.2f}")
                self.median_result.config(text=f"{median_value:.2f}")
                self.mode_result.config(text=f"{mode_value:.2f}")

        except Exception as e:
            error_message = f"Error: {str(e)}"
            tk.messagebox.showerror("Error", error_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVStatsApp(root)
    root.mainloop()


# In[ ]:





# In[ ]:




