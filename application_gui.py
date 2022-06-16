from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import algo

root = Tk()
root.geometry("720x500")
root.resizable(False,False)
root.title("Automated Depression Detection")
user_report_path = "No File"
def get_csv():
	global user_report_path
	user_report_path = filedialog.askopenfilename(initialdir="/", title="Select EEG Data", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
	# print(user_report_path)
def evaluate_report():
	if (user_report_path == "No File"):
		messagebox.showinfo("Invalid File", "Please Select Your EEG Report")
	else:
		data = algo.train_model()
		health = data[0]
		acc = data[1]
		# print(health)
		# print(acc)
		msg = str(health) + "   (Accuracy : " + str(acc) + ")"
		messagebox.showinfo("Result", msg)
	

def show_application():
	# Application Page
	application_frame = Frame(root, bg="white")
	application_frame.place(x = 0, y = 0, height=500, width=720)
	welcome_label = Label(application_frame, text="Welcome to ADD", font=("Times New Roman", 30), bg="white")
	welcome_label.place(relx=0.5, y= 70, anchor=CENTER)
	select_report_label = Label(application_frame, text = "Select Your EEG Report :", bg="white")
	select_report_label.place(relx=0.4, y = 200, anchor=CENTER)
	select_report_button = Button(application_frame, text="Browse", command=get_csv)
	select_report_button.place(relx=0.6, y = 200, anchor=CENTER)

	evaluate_button = Button(application_frame, command=evaluate_report, text="Evaluate Report")
	evaluate_button.place(relx=0.5, y=300, anchor=CENTER)

def validate():
	if(str(user_name_input_area.get())=="username" and str(user_password_entry_area.get()) =="password"):
		show_application()
	else:
		messagebox.showerror("Invalid User","Username and Password are not correct")
	# show_application()

# the label for user_name
user_name = Label(root, text = "Username")
user_name.place(x = 140,y = 60)
# the label for user_password
user_password = Label(root, text = "Password")
user_password.place(x = 140, y = 100)
# input box for username	
user_name_input_area = Entry(root, width = 30)
user_name_input_area.place(x = 210, y = 60)
# input box for password
user_password_entry_area = Entry(root, width = 30, show="*")
user_password_entry_area.place(x = 210, y = 100)
# Login Button
login_button = Button(root, text = "Login", command=validate).place(x = 140, y = 130)



root.mainloop()
