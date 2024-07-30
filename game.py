import tkinter as tk
import random
rock_emoji = "🪨"
paper_emoji = "📄"
scissors_emoji = "✂️"
def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
    else:
        result = "You lose!"
    user_choice_label.config(text=f"Your choice: {emoji_map[user_choice]}")
    computer_choice_label.config(text=f"Computer's choice: {emoji_map[computer_choice]}")
    result_label.config(text=f"{result}")
    animate_result()
def on_button_click(choice):
    determine_winner(choice)
def animate_result():
    for i in range(6):
        app.after(i * 200, lambda i=i: result_label.config(bg=background_color if i % 2 == 0 else result_bg_color))
    app.after(0, lambda: result_label.config(font=("Helvetica", 20, "bold")))
    app.after(600, lambda: result_label.config(font=label_font))
app = tk.Tk()
app.title("Rock, Paper, Scissors")
app.geometry("400x500")
background_color = "#f0f8ff"
button_color = "#4caf50"
button_text_color = "#ffffff"
label_color = "#333333"
result_bg_color = "#e6f9ff"
button_font = ("Helvetica", 14)
label_font = ("Helvetica", 16)
app.configure(bg=background_color)
emoji_map = {
    'rock': rock_emoji,
    'paper': paper_emoji,
    'scissors': scissors_emoji  
}
main_frame = tk.Frame(app, bg=background_color)
main_frame.pack(pady=20)
choice_frame = tk.Frame(main_frame, bg=background_color)
choice_frame.pack(pady=10)
user_choice_label = tk.Label(choice_frame, text="Your choice: ", font=label_font, bg=background_color, fg=label_color)
user_choice_label.grid(row=0, column=0, padx=20)
computer_choice_label = tk.Label(choice_frame, text="Computer's choice: ", font=label_font, bg=background_color, fg=label_color)
computer_choice_label.grid(row=0, column=1, padx=20)
button_frame = tk.Frame(main_frame, bg=background_color)
button_frame.pack(pady=10)
rock_button = tk.Button(button_frame, text="Rock", font=button_font, bg=button_color, fg=button_text_color, width=10, height=2, relief="raised", command=lambda: on_button_click('rock'))
rock_button.grid(row=0, column=0, padx=10)
paper_button = tk.Button(button_frame, text="Paper", font=button_font, bg=button_color, fg=button_text_color, width=10, height=2, relief="raised", command=lambda: on_button_click('paper'))
paper_button.grid(row=0, column=1, padx=10)
scissors_button = tk.Button(button_frame, text="Scissors", font=button_font, bg=button_color, fg=button_text_color, width=10, height=2, relief="raised", command=lambda: on_button_click('scissors'))
scissors_button.grid(row=0, column=2, padx=10)
result_label = tk.Label(app, text="", font=label_font, bg=result_bg_color, fg=label_color, bd=2, relief="solid", padx=10, pady=10)
result_label.pack(pady=20)
description_frame = tk.Frame(app, bg=background_color)
description_frame.pack(pady=20)
rock_description = tk.Label(description_frame, text=f"{rock_emoji} Rock: Crushes Scissors", font=label_font, bg=background_color, fg=label_color)
rock_description.pack(pady=5)
paper_description = tk.Label(description_frame, text=f"{paper_emoji} Paper: Covers Rock", font=label_font, bg=background_color, fg=label_color)
paper_description.pack(pady=5)
scissors_description = tk.Label(description_frame, text=f"{scissors_emoji} Scissors: Cuts Paper", font=label_font, bg=background_color, fg=label_color)
scissors_description.pack(pady=5)
app.mainloop()
