"""

Author:  Jacob Clark
Date written: 02/24/25
Assignment:   Final Project
Short Desc:   NutriTrack is a Python Tkinter GUI app that lets users log their daily food and calorie intake, then offers simple, personalized diet recommendations based on their goals.


"""

import tkinter as tk # Import Tkinter for GUI
from tkinter import messagebox # Import messagebox for pop-ups

"""Initialize main window to provide navigation to other sections."""
class NutriTrackApp:
    """Initialize main GUI and components."""
    def __init__(self, root):
        self.root = root
        self.root.title("NutriTrack: Basic Nutrition Tracker")
        self.root.geometry("400x300") # Window size
        
        # Main Window Showing Buttons
        self.label = tk.Label(root, text="Welcome to NutriTrack!", font=("Arial", 14))
        self.label.pack(pady=10) # Padding for spacing

        # Buttons to navigate to different pages
        self.intake_button = tk.Button(root, text="Enter Daily Intake", command=self.openDailyIntake, width=25)
        self.intake_button.pack(pady=5) # Spacing between buttons

        self.summary_button = tk.Button(root, text="View Calorie Summary", command=self.openCalorieSummary, width=25)
        self.summary_button.pack(pady=5)

        self.recommendations_button = tk.Button(root, text="Basic Diet Recommendations", command=self.openDietRecommendations, width=25)
        self.recommendations_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit Application", command=root.quit, width=25)
        self.exit_button.pack(pady=10)

    """Opens window to allow users to enter their daily food intake."""
    def openDailyIntake(self):
        # Opens a new window for entering daily intake
        intake_window = tk.Toplevel(self.root)
        intake_window.title("Daily Intake") # Window title
        intake_window.geometry("300x200") # Window size
        tk.Label(intake_window, text="Enter your food details:", font=("Arial", 12)).pack(pady=10) # Prompt for user input

    """Opens a window displaying the user's calorie summary."""
    def openCalorieSummary(self):
        # Opens a new window displaying calorie summary.
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Calorie Summary") # Window title
        summary_window.geometry("300x200") # Window size
        tk.Label(summary_window, text="Calorie summary will be displayed here.", font=("Arial", 12)).pack(pady=10) # Calorie Summary

    """Opens a window displaying basic diet recommendations."""
    def openDietRecommendations(self):
        # Opens a new window with basic diet recommendations.
        recommendations_window = tk.Toplevel(self.root)
        recommendations_window.title("Diet Recommendations") # Window title
        recommendations_window.geometry("300x200") # Window size
        tk.Label(recommendations_window, text="Diet recommendations will be shown here.", font=("Arial", 12)).pack(pady=10)

# Run the Application
if __name__ == "__main__":
    root = tk.Tk() # Main Tkinter window
    app = NutriTrackApp(root) # Initialize NutriTrackApp class
    root.mainloop() # Start event loop
