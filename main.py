import tkinter as tk
from tkinter import scrolledtext
import sys, os # sys for info about the computer, os for curr directory

class CommandLineInterface:
    def __init__(self, root):
        # Create window + its name
        self.root = root
        self.root.title("CMD ANALOG")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        # Create the text area for output
        self.output_area = scrolledtext.ScrolledText( #insertbackground - for cursor
            root, wrap=tk.WORD, bg='black', fg='green', 
            insertbackground='green', font=('Courier', 12))
        # The pack() method positions it in the window with expansion and padding
        self.output_area.pack(expand=True, fill='both', padx=5, pady=5)
        self.output_area.config(state=tk.DISABLED)
        
        # Create the input field + position it
        self.input_frame = tk.Frame(root, bg='black')
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # to get curr dir and show it near input field
        self.prompt = tk.Label( self.input_frame, text=f"{os.getcwd()}>>> ",
            bg='black', fg='green', font=('Courier', 12))
        self.prompt.pack(side=tk.LEFT)
        
        self.input_field = tk.Entry( #command input field
            self.input_frame, bg='black', fg='green', 
            insertbackground='green', font=('Courier', 12), relief=tk.FLAT)
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True) # expand horizontally
        self.input_field.bind('<Return>', self.execute_command) # if "Enter" is pressed - execute comm
        self.input_field.focus() # Sets focus to the input field so user can type immediately
        
        # Welcome message
        self.display_welcome()

        global words
        
    def display_welcome(self):
        welcome_msg = (
            f"CMD ANALOG On {sys.platform}\n"
            f"Python {sys.version}\n")
        self.display_output(welcome_msg)
    
    def display_output(self, text):
        self.output_area.config(state=tk.NORMAL) # Temporarily enables the text widget
        self.output_area.insert(tk.END, text) # Inserts text at the end
        self.output_area.see(tk.END) # Scrolls to the end to show the new text
        self.output_area.config(state=tk.DISABLED) # Disables the text widget again        
        
    def execute_command(self, event):
        # get command and clear the field
        command = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)
        
        # Display the command
        self.display_output(f">>> {command}\n")
        
        # split the input line into several words
        
        words = [i for i in command.split()]
        
        # commands
        if (command == ''):
            pass
        elif (words[0].lower() in ['exit', 'quit']): # lower - get NON-CAPS version of command
            self.display_output("Exiting...\n")
            self.root.after(1000, self.root.destroy)
        elif (words[0].lower() == "help" and len(words)==1):
            help_msg = ("help - to see this message\n"
                        "exit/quit - to stop the program\n"
                        "ls/cd - not yet implemented\n")
            self.display_output(help_msg)
        elif (words[0].lower() == 'ls'):
            self.display_output(f"The command and arguements: {words[0]}, '{words[1:]}'\n")
        elif (words[0].lower() == 'cd'):
            self.display_output(f"The command and arguements: {words[0]}, '{words[1:]}'\n")
        else:
            self.display_output(f"Unknown command: {command}\n")
            
        words = []
       

if __name__ == "__main__":
    root = tk.Tk()
    cli = CommandLineInterface(root)
    root.mainloop()
