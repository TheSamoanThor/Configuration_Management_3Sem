import tkinter as tk
from tkinter import scrolledtext
import sys, os # sys for info about the computer, os for curr directory
import argparse # to get args from the original cmd
import configparser # to read configs
import json
import base64



class VFSNode:
#     __slots__ = ('name', 'type', 'content', 'children', 'parent', 'metadata', 'path')       
    def __init__(self, node_data):
        
        self.name = node_data['name']
        self.type = node_data['type']
        self.path = node_data['path']
        self.parent = None
        self.children = {}
        
        if ('encoding' in node_data):
            self.encoding = node_data['encoding']
        else:
            self.encoding = None
        
        if ('content' in node_data):
            if self.encoding == 'base64': # decode if encoded
                self.content = base64.b64decode(node_data['content']).decode('utf-8')
            else:
                self.content = node_data['content'].decode('utf-8')
        else:
            self.content = None
            
        if ('metadata' in node_data):
            self.metadata = node_data['metadata']
        else:
            self.metadata = None
            
        
        
    def add_child(self, node):
        node.parent = self
        #add to dict
        self.children[node.name] = node
        
        
        
    def get_path(self):
        if (not(self.path)):
            path = []
            current = self
            while current:
                path.append(current.name)
                current = current.parent
            return '/'.join(reversed(path))
        return self.path
    
    
    
    def display_data(self):
        print(f"Data: \n"+
              f"name = {self.name}\n"+
              f"type = {self.type}\n"+
              f"path = {self.path}\n"+
              f"parent = {self.parent}\n"+
              f"children = {self.children}\n"+
              f"content = {self.content}\n"+
              f"metadata = {self.metadata}\n")
       
       
       
class VFS:
    def __init__(self, vfs_path):
        self.root = self.load_vfs_from_json(vfs_path)
               
        
        
    def load_vfs_from_json(self, json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            vfs_data = json.load(f)
                
        # Создаем корневой узел VFS
        return self.build_vfs_tree(vfs_data)
    


    def build_vfs_tree(self, node_data, parent=None):
               
        if node_data['type'] == 'directory':
            # Создаем узел директории
            node = VFSNode(node_data)
            if parent:
                parent.add_child(node)
            
            # Рекурсивно обрабатываем дочерние элементы
            if 'children' in node_data:
                for child_data in node_data['children']:
                    self.build_vfs_tree(child_data, node)
            node.display_data()
            return node
            
        elif node_data['type'] == 'file':
            # Создаем узел файла
            node = VFSNode(node_data)
            if parent:
                parent.add_child(node)
            node.display_data()
            return node
    
    

class CommandLineInterface:
    def __init__(self, root, vfs_path, script_path, config_path):
        # Create window + its name
        self.root = root
        self.root.title("CMD ANALOG")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        # get paths for files
        self.vfs_path = vfs_path
        self.script_path = script_path
        self.config_path = config_path
        
        # Create the text area for output
        self.output_area = scrolledtext.ScrolledText( #insertbackground - for cursor
            root, wrap=tk.WORD, bg='black', fg='white', 
            insertbackground='white', font=('Courier', 12))
        # The pack() method positions it in the window with expansion and padding
        self.output_area.pack(expand=True, fill='both', padx=5, pady=5)
        self.output_area.config(state=tk.DISABLED)
        
        # Create the input field + position it
        self.input_frame = tk.Frame(root, bg='black')
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)
                
        # to get curr dir and show it near input field, must be updated to show location in VFS
        self.prompt = tk.Label(self.input_frame, text=f"{os.getcwd()}>>> ",
            bg='black', fg='white', font=('Courier', 12))
        self.prompt.pack(side=tk.LEFT)
               
        self.input_field = tk.Entry( #command input field
            self.input_frame, bg='black', fg='white', 
            insertbackground='white', font=('Courier', 12), relief=tk.FLAT)
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True) # expand horizontally
        self.input_field.bind('<Return>', self.execute_command) # if "Enter" is pressed - execute comm
        self.input_field.focus() # Sets focus to the input field so user can type immediately
        
        #get vfs
        self.vfs = None
        if vfs_path and os.path.exists(vfs_path):
            self.vfs = VFS(vfs_path)
        else:
            self.vfs = None
            self.display_output("VFS не загружена: файл не найден или путь не указан\n")
        self.vfs_exists = (self.vfs!=None)  
        
        # Welcome and about config messages
        self.display_welcome()
        self.display_config()
        
        if self.script_path:
            self.execute_start_script()
    
    
    
    def display_welcome(self):
        welcome_msg = (
            f"CMD ANALOG On {sys.platform}\n"
            f"Python {sys.version}\n")
        self.display_output(welcome_msg)
    
    
    
    def display_config(self):
        config_info = (
            f"Config information:\n"
            f"Config path: {self.config_path}\n"
            f"VFS path: {self.vfs_path}\n"
            f"VFS exists: {self.vfs_exists}\n"
            f"Script path: {self.script_path}\n"
            "\n"
        )
        self.display_output(config_info)
    
       

    def display_output(self, text):
        self.output_area.config(state=tk.NORMAL) # Temporarily enables the text widget
        self.output_area.insert(tk.END, text) # Inserts text at the end
        self.output_area.see(tk.END) # Scrolls to the end to show the new text
        self.output_area.config(state=tk.DISABLED) # Disables the text widget again        
        


    def execute_start_script(self):
        with open(self.script_path, 'r') as script_file:
            commands = script_file.readlines()
        
        for command in commands:
            command = command.strip()
            if command:
                # just copied the following code from execute_command(self, event)
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
                    self.display_output(f"Unknown command: {command}, the following start script cannot be done")
                    return
                # stop executing in case of some troubles, as it is in the task
                    
                words = []
                


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
    


def parse_arguments(): 
    parser = argparse.ArgumentParser(description='CMD ANALOG')
    # description - the first line of the "help" message
    parser.add_argument('--vfs', type=str,
                help='Path to VFS physical location, preferable to place this file in the same directory as this code file')
    parser.add_argument('--script', type=str,
                help='Path to startup script, preferable to place this file in the same directory as this code file')
    parser.add_argument('--config', type=str, default='config.ini',
                help='Path to config file (default: config.ini). Please, place config.ini and the default files in the same directory as this code file')
    
    # arguements: (key for search of the arg, type of this arg, the message we get in case of typing "python main.py --help")
    
    return parser.parse_args()



def parse_config_file(config_path):
    # .ini file - .txt with special structure and saved in a special way
    # struct:
    #
    # [DEFAULT]
    # vfs_path = vfs_struct_file.txt
    # script_path = vfs_start_script.txt
    #
        
    config = configparser.ConfigParser()
    vfs_path = None
    script_path = None
    
    if os.path.exists(config_path):
        config.read(config_path)
        if 'DEFAULT' in config:
            if 'vfs_path' in config['DEFAULT']:
                vfs_path = config['DEFAULT']['vfs_path']
            if 'script_path' in config['DEFAULT']:
                script_path = config['DEFAULT']['script_path']
    
    return vfs_path, script_path
     


if __name__ == "__main__":
    args = parse_arguments()
    
    vfs_path, script_path = parse_config_file(args.config)
    
    # priority
    if args.vfs:
        vfs_path = args.vfs
    if args.script:
        script_path = args.script
    
    # if file is open from cmd, then it prints information in concole
    print(f"Info: VFS path = {vfs_path}")
    print(f"Info: Script path = {script_path}")
    print(f"Info: Config file = {args.config}")
    
    root = tk.Tk()
    cli = CommandLineInterface(root, vfs_path, script_path, args.config)
    root.mainloop()
