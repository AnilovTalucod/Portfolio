from tkinter import *
from tkinter import ttk

co0="#444466"
co1="#feffff"
co2="#6856FF"

window = Tk()
window.title( '' )
window.geometry('295x230')
window.resizable(height=FALSE, width=FALSE)
window.configure(bg=co1)


top_frame = Frame(window, width=295, height=50, bg=co1, pady=0, padx=0)
top_frame.grid(row=0, column=0)

down_frame = Frame(window, width=295, height=50, bg=co1, pady=0, padx=0)
down_frame.grid(row=1, column=0)

app_name = Label(top_frame, text = "BMI Calculator", width = 23, height=1, padx=0, anchor="center", font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.place(x=0, y=2)

app_line = Label(top_frame, text = "", width = 400, height=1, padx=0, anchor="center", font=("Arial 1"), bg=co2, fg=co0)
app_line.place(x=0, y=35)

def calculate():
    weight = float(e_weight.get())
    height = float(e_height.get()) ** 2
    result = weight / height
    
    if result < 18.4:
        l_result_text['text'] = "Your BMI is: Underweight"
    elif result >= 18.5 and result < 24.9:
        l_result_text['text'] = "Your BMI is: Normal"
    elif l_result >= 25 and result < 29.9:
        l_result_text['text'] = "Your BMI is: Overweight"
    else:
        l_result_text['text'] = "Your BMI is: Obesity"
        
    l_result['text'] = "{:.{}f}".format(result, 2)
    
l_weight = Label(down_frame, text = "Enter your weight", height=1, padx=0, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_weight.grid(row=0, column=0, columnspan=1, pady=10, padx=3)
e_weight = Entry(down_frame, width=5, font=("Ivy 10 bold"), justify="center", relief=SOLID)
e_weight.grid(row=0, column=1, columnspan=1, pady=10, padx=3)

l_height = Label(down_frame, text = "Enter your height", height=1, padx=0, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_height.grid(row=1, column=0, columnspan=1, pady=10, padx=3)
e_height = Entry(down_frame, width=5, font=("Ivy 10 bold"), justify="center", relief=SOLID)
e_height.grid(row=1, column=1, columnspan=1, pady=10, padx=3)

l_result = Label(down_frame, width=5, text="---", height=1, padx=6, pady=12, anchor="center", font=("Ivy 24 bold"), bg=co2, fg=co1)
l_result.place(x=175, y=10)

l_result_text = Label(down_frame, width=37, text="", height=1, padx=6, pady=12, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_result_text.place(x=0, y=85)

b_calculate = Button(down_frame, text="Calculate", width=34, height=1, bg=co2, fg=co1, font=("Ivy 10 bold"), anchor="center", command=calculate)
b_calculate.grid(row=4, column=0, pady=60, padx=5, columnspan=30)

window.mainloop()