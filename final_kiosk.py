import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image handling

# Dictionary to store user credentials and transactions
users = {
    'admin': 'admin',
    'user':'user'
}

transactions = []

# Main application class
class KioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Wash Kiosk")
        self.root.attributes('-fullscreen', True)
        
        # Variables for storing username and password
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        # Load and resize images for buttons
        self.login_image = ImageTk.PhotoImage(Image.open("img/login.jpeg").resize((150, 80), Image.LANCZOS))
        self.exit_image = ImageTk.PhotoImage(Image.open("img/exit.png").resize((150, 80), Image.LANCZOS))
        self.pay_now_image = ImageTk.PhotoImage(Image.open("img/pay_now.jpeg").resize((150, 80), Image.LANCZOS))
        self.cancel_image = ImageTk.PhotoImage(Image.open("img/cancel.png").resize((150, 80), Image.LANCZOS))
        self.logout_image = ImageTk.PhotoImage(Image.open("img/logout.jpeg").resize((150, 80), Image.LANCZOS))
        self.start_image = ImageTk.PhotoImage(Image.open("img/start.jpeg").resize((150, 80), Image.LANCZOS))
        
        # Load and resize logo
        self.logo_image = ImageTk.PhotoImage(Image.open("img/kke.jpeg").resize((150, 80), Image.LANCZOS))
        
        # Load and resize images for services
        self.basic_wash_image = ImageTk.PhotoImage(Image.open("img/basic_wash.jpeg").resize((100, 100), Image.LANCZOS))
        self.deluxe_wash_image = ImageTk.PhotoImage(Image.open("img/deluxe_wash.jpeg").resize((100, 100), Image.LANCZOS))
        self.premium_wash_image = ImageTk.PhotoImage(Image.open("img/premium_wash.jpeg").resize((100, 100), Image.LANCZOS))

        # Service indicators
        self.service_selected = tk.StringVar(value="None")
        
        # Show the start page
        self.create_start_page()

    def create_start_page(self):
        # Clear the window
        self.clear_frame()
        
        # Start page widgets
        tk.Label(self.root, image=self.logo_image).pack(pady=20)
        # tk.Label(self.root, text="Company Name", font=('Arial', 36)).pack(pady=10)
        tk.Button(self.root, image=self.start_image, command=self.create_login_page).pack(pady=20)
        tk.Button(self.root, image=self.exit_image, command=self.root.quit).pack(pady=10)

    def create_login_page(self):
        # Clear the window
        self.clear_frame()
        
        # Login page widgets
        tk.Label(self.root, text="Login", font=('Arial', 36)).pack(pady=40)
        tk.Label(self.root, text="Username", font=('Arial', 24)).pack(pady=10)
        tk.Entry(self.root, textvariable=self.username, font=('Arial', 24), width=20).pack(pady=10)
        tk.Label(self.root, text="Password", font=('Arial', 24)).pack(pady=10)
        tk.Entry(self.root, textvariable=self.password, show='*', font=('Arial', 24), width=20).pack(pady=10)
        tk.Button(self.root, image=self.login_image, command=self.login).pack(pady=20)
        tk.Button(self.root, image=self.exit_image, command=self.root.quit).pack(pady=10)

    def create_service_page(self):
        # Clear the window
        self.clear_frame()

        # Service selection page widgets
        tk.Label(self.root, text="Select Service", font=('Arial', 36)).pack(pady=40)
        
        # Service buttons with indicators and images
        self.create_service_button("Basic Wash - ₹500", 500, self.basic_wash_image)
        self.create_service_button("Deluxe Wash - ₹1000", 1000, self.deluxe_wash_image)
        self.create_service_button("Premium Wash - ₹1500", 1500, self.premium_wash_image)

        tk.Button(self.root, image=self.logout_image, command=self.create_login_page).pack(pady=20)

    def create_service_button(self, service_text, amount, image):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        service_image_label = tk.Label(frame, image=image)
        service_image_label.pack(side=tk.LEFT, padx=10)

        service_button = tk.Button(frame, text=service_text, command=lambda: self.process_payment(service_text, amount), font=('Arial', 24), width=20)
        service_button.pack(side=tk.LEFT, padx=10)

        indicator = tk.Label(frame, text="", bg="red", width=2, height=1)
        indicator.pack(side=tk.LEFT, padx=10)

        self.update_indicator(indicator, service_text)

    def update_indicator(self, indicator, service_text):
        if self.service_selected.get() == service_text:
            indicator.config(bg="green")
        else:
            indicator.config(bg="red")

    def process_payment(self, service, amount):
        # Set selected service
        self.service_selected.set(service)

        # Clear the window
        self.clear_frame()

        # Payment confirmation page widgets
        tk.Label(self.root, text=f"Confirm Payment of ₹{amount} for {service}", font=('Arial', 30)).pack(pady=40)
        tk.Button(self.root, image=self.pay_now_image, command=lambda: self.complete_transaction(service, amount)).pack(pady=20)
        tk.Button(self.root, image=self.cancel_image, command=self.create_service_page).pack(pady=20)

    def complete_transaction(self, service, amount):
        # Add transaction to the list
        transactions.append({
            'username': self.username.get(),
            'service': service,
            'amount': amount
        })
        
        # Show success message
        messagebox.showinfo("Payment Successful", f"Payment of ${amount} for {service} was successful!")
        self.service_selected.set("None")
        self.create_service_page()

    def login(self):
        # Check if username and password are correct
        if users.get(self.username.get()) == self.password.get():
            self.create_service_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def clear_frame(self):
        # Remove all widgets from the window
        for widget in self.root.winfo_children():
            widget.destroy()

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop()
