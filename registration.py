import tkinter as tk
from tkinter import ttk, messagebox


def submit_action():
    student_id = entry_student_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    address = entry_address.get()
    phone = entry_phone.get()
    #major = entry_major.get()

    if student_id and first_name and last_name and email and age and gender and address and phone and major:
        try:
            age = int(age)  
            phone = int(phone)  
            messagebox.showinfo("Registration Successful", f"Student ID: {student_id}\nName: {first_name} {last_name}\nEmail: {email}\nAge: {age}\nGender: {gender}\nAddress: {address}\nPhone: {phone}\nMajor: {major}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid age and phone number")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")


root = tk.Tk()
root.title("Student Registration Form")


root.geometry("400x600")


main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)


def create_label_entry(frame, text):
    label = ttk.Label(frame, text=text)
    label.pack(pady=5)
    entry = ttk.Entry(frame)
    entry.pack(pady=5)
    return entry

entry_student_id = create_label_entry(main_frame, "Student ID")
entry_first_name = create_label_entry(main_frame, "First Name")
entry_last_name = create_label_entry(main_frame, "Last Name")
entry_email = create_label_entry(main_frame, "Email")
entry_age = create_label_entry(main_frame, "Age")


label_gender = ttk.Label(main_frame, text="Gender")
label_gender.pack(pady=5)
gender_var = tk.StringVar(value="Male")
gender_frame = ttk.Frame(main_frame)
gender_frame.pack(pady=5)
radio_male = ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
radio_female = ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
radio_other = ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other")
radio_male.grid(row=0, column=0, padx=5)
radio_female.grid(row=0, column=1, padx=5)
radio_other.grid(row=0, column=2, padx=5)

entry_address = create_label_entry(main_frame, "Address")
entry_phone = create_label_entry(main_frame, "Phone Number")


submit_button = ttk.Button(main_frame, text="Submit", command=submit_action)
submit_button.pack(pady=20)


root.mainloop()
