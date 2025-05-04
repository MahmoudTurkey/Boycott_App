from tkinter import *

def check():
    Brand = user_entry.get().capitalize()
    
    with open('C:\\Users\\samir\\Boycott_Proj\\Boycott Brands.txt') as file:
        content = file.read()
        
        if Brand in content:
            # Clear the canvas and display the second image
            check_now.place_forget()
            user_entry.place_forget()
            canvas.delete("all")  # Clear the canvas
            image1 = PhotoImage(file='C:\\Users\\samir\\Boycott_Proj\\pro-02.gif')
            canvas.create_image(0, 0, anchor=NW, image=image1)
            canvas.image = image1  # Keep a reference to avoid garbage collection
            
            
        else:
            # Clear the canvas and display the first image
            check_now.place_forget()
            user_entry.place_forget()
            canvas.delete("all")  # Clear the canvas
            image2 = PhotoImage(file='C:\\Users\\samir\\Boycott_Proj\\pro-03.gif')
            canvas.create_image(0, 0, anchor=NW, image=image2)
            canvas.image = image2  # Keep a reference to avoid garbage collection
            
            

# Initialize the main window
window = Tk()
window.title('Boycott')

# Create a canvas and display the initial image
canvas = Canvas(window, width=432, height=842)
canvas.pack()
initial_image = PhotoImage(file='C:\\Users\\samir\\Boycott_Proj\\pro-01.gif')
canvas.create_image(0, 0, anchor=NW, image=initial_image)
canvas.image = initial_image  # Keep a reference to avoid garbage collection

# Create an entry widget for user input
user_entry = Entry(window,borderwidth=0.25 ,fg='black', font=('times new roman', 18))
user_entry.place(x=69, y=538)

# Create a button to trigger the check function
check_now = Button(window,borderwidth=0,highlightthickness=0,relief='flat',width=17,height=2,bg='#df2314', text="Check Now",fg='white',font=('Comic Sans MS', 10, 'bold'), command=check)
check_now.place(x=140, y=613)


# Start the main event loop
window.mainloop()