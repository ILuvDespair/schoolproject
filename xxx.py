import random
import tkinter as tk

# Define a dictionary mapping actions to their likelihoods of leading to hell
hell_likelihoods = {
    "Stealing": 0.8,
    "Lying": 0.7,
    "Cheating": 0.9,
    "Killing": 1,
    "Blasphemy": 0.9,
    "Adultery": 0.8,
    "Coveting": 0.6,
    "Idolatry": 0.7,
    "Anger": 0.5,
    "Greed": 0.6
}

# Create a list of possible actions
hell_actions = list(hell_likelihoods.keys())

# Create a function to calculate the user's chance of going to hell
def calculate_hell_chance():
    # Get the selected action from the drop-down menu
    action = action_var.get()
    
    # Get the likelihood of going to hell for the selected action
    likelihood = hell_likelihoods[action]
    
    # Generate a random number between 0 and 1
    rand_num = random.random()
    
    # Determine if the user goes to hell based on the likelihood and the random number
    if rand_num <= likelihood:
        result = "You're going to hell!"
    else:
        result = "You're in the clear!"
    
    # Update the result label with the calculated result
    result_label.config(text=result)

# Create the tkinter window
window = tk.Tk()
window.title("Your Chances of Going to Hell Simulator")

# Create the UI elements
action_label = tk.Label(window, text="Select an action:")
action_var = tk.StringVar()
action_dropdown = tk.OptionMenu(window, action_var, *hell_actions)
chance_button = tk.Button(window, text="Calculate Your Chance of Going to Hell", command=calculate_hell_chance)
result_label = tk.Label(window, text="")

# Pack the UI elements into the window
action_label.pack()
action_dropdown.pack()
chance_button.pack()
result_label.pack()

# Start the tkinter event loop
window.mainloop()
