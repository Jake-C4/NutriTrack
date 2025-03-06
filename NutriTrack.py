"""

Author:  Jacob Clark
Date written: 02/20/25
Assignment:   Final Project
Short Desc:   NutriTrack is a Python Tkinter GUI app that lets users log their daily food and calorie intake, then offers simple, personalized diet recommendations based on their goals.


"""

import tkinter as tk # Import Tkinter for GUI
from tkinter import messagebox # Import messagebox for pop-ups
from PIL import Image, ImageTk # Import Pillow for images

"""Initialize main window to provide navigation to other sections."""
class NutriTrackApp:
    """Initialize main GUI and components."""
    def __init__(self, root):
        self.root = root
        self.root.title("NutriTrack: Basic Nutrition Tracker")
        self.root.geometry("500x400") # Window size

        # Display image
        image_path = r"C:\Users\19jac\Desktop\Intro_to_Software_Development\NutriTrack\nutritracklogo.jpg" # Path to image
        self.logo_image = Image.open(image_path) # Opens image
        self.logo_image = self.logo_image.resize((200, 100), Image.LANCZOS) #Resize image
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Display image at the top of window
        self.image_label = tk.Label(root, image=self.logo_photo)
        self.image_label.pack(pady=5) # Spacing below image
        
        # Main Window Showing Buttons
        self.label = tk.Label(root, text="Welcome to NutriTrack!", font=("Arial", 14))
        self.label.pack(pady=10) # Padding for spacing

        # Buttons to navigate to different pages
        self.intake_button = tk.Button(root, text="Enter Daily Intake", command=self.openDailyIntake, width=25)
        self.intake_button.pack(pady=10) # Spacing between buttons

        self.summary_button = tk.Button(root, text="View Calorie Summary", command=self.openCalorieSummary, width=25)
        self.summary_button.pack(pady=10)

        self.recommendations_button = tk.Button(root, text="Basic Diet Recommendations", command=self.openDietRecommendations, width=25)
        self.recommendations_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit Application", command=root.quit, width=25)
        self.exit_button.pack(pady=10)

        # Store food entries
        self.food_entries = []

    """Opens window to allow users to enter their daily food intake."""
    def openDailyIntake(self):
        # Opens a new window for entering daily intake
        intake_window = tk.Toplevel(self.root)
        intake_window.title("Daily Intake") # Window title
        intake_window.geometry("400x300") # Window size
        
        tk.Label(intake_window, text="Food Name: ", font=("Arial", 10)).pack() # Prompt for user input
        food_entry = tk.Entry(intake_window)
        food_entry.pack(pady=5)

        tk. Label(intake_window, text="Portion Size (Grams or Milliliters): ", font=("Arial", 10)).pack()
        portion_entry = tk.Entry(intake_window)
        portion_entry.pack(pady=5)

        tk.Label(intake_window, text="Calories: ", font=("Arial", 10)).pack()
        calorie_entry = tk.Entry(intake_window)
        calorie_entry.pack(pady=5)

        # Submit button with validation
        def submit_entry():
            food = food_entry.get().strip()
            portion = portion_entry.get().strip()
            calories = calorie_entry.get().strip()

            # Validate user inputs
            if not food:
                messagebox.showerror("Error", "Food name error!")
                return
            if not portion.isdigit():
                messagebox.showerror("Error", "Portion size must be a positive number.")
                return
            if not calories.isdigit():
                messagebox.showerror("Error", "Calories must be a positive number.")
                return
            # Store user input to confirm
            self.food_entries.append({"Food": food, "Portion": int(portion), "Calories": int(calories)})
            messagebox.showinfo("Success", f"{food} was added.")
            intake_window.destroy() # Closes the window
        submit_button = tk.Button(intake_window, text="Submit", command=submit_entry)
        submit_button.pack(pady=10)

    """Opens a window displaying the user's calorie summary."""
    def openCalorieSummary(self):
        # Opens a new window displaying calorie summary.
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Calorie Summary") # Window title
        summary_window.geometry("300x200") # Window size
        
        if not self.food_entries:
            tk.Label(summary_window, text="Add items for a summary.", font=("Arial", 12)).pack(pady=10) # Calorie Summary
            return

        # Display Summary
        tk.Label(summary_window, text="Food Intake Summary", font=("Arial", 12, "bold")).pack(pady=5)
        total_calories = sum(entry["Calories"] for entry in self.food_entries)

        for entry in self.food_entries:
            tk.Label(summary_window, text=f"{entry['Food']} - {entry['Calories']} kcal", font=("Arial", 10)).pack()
        
        tk.Label(summary_window, text=f"Total Calories: {total_calories}", font=("Arial", 12)).pack(pady=10)

    """Opens a window displaying basic diet recommendations."""
    def openDietRecommendations(self):
        # Opens a new window with basic diet recommendations.
        recommendations_window = tk.Toplevel(self.root)
        recommendations_window.title("Diet Recommendations") # Window title
        recommendations_window.geometry("400x300") # Window size

        # Second image display
        rec_image_path = r"C:\Users\19jac\Desktop\Intro_to_Software_Development\NutriTrack\healthy_foods.jpg" # Path to image
        self.rec_image = Image.open(rec_image_path) # Opens image
        self.rec_image = self.rec_image.resize((100, 100), Image.LANCZOS) # Image resize
        self.rec_photo = ImageTk.PhotoImage(self.rec_image) # Tkinter format

        self.image_label = tk.Label(recommendations_window, image=self.rec_photo)
        self.image_label.pack() # Display image

        
        # Calculate Total Calories from User Input
        total_calories = sum(entry["Calories"] for entry in self.food_entries)

        # Display Recommendations
        if total_calories == 0:
            recommendation_text = "No data available. Please enter food items to show recommendations."
        elif total_calories < 1500:
            recommendation_text = "You are consuming less calories than recommended. \nConsider adding more proteins."
        elif 1500 <= total_calories <= 2500:
            recommendation_text = "You're within a healthy calorie range. \nContinue maintaining a balanced and healthy diet."
        else:
            recommendation_text = "You're consuming more calories than recommended. \nConsider cutting back, or reducing processed foods."

        tk.Label(recommendations_window, text="Your Diet Recommendations:", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(recommendations_window, text=recommendation_text, font=("Arial", 10), wraplength=300, justify="center").pack(pady=10)

# Run the Application
if __name__ == "__main__":
    root = tk.Tk() # Main Tkinter window
    app = NutriTrackApp(root) # Initialize NutriTrackApp class
    root.mainloop() # Start event loop
