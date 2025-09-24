import tkinter as tk
from tkinter import scrolledtext
import sys, os # sys for info about the computer, os for curr directory
import argparse # to get args from the original cmd
import configparser # to read configs
import json
import base64
from datetime import datetime



global dict_all_nodes
dict_all_nodes = {}
        
        

class VFSNode:
#     __slots__ = ('name', 'type', 'content', 'children', 'parent', 'metadata', 'path')       
    def __init__(self, node_data):
        
        self.name = node_data['name']
        self.type = node_data['type']
        self.parent = None
        self.children = {}
#         "path": "/SUB_CAT_3_fun/music.mp3",
        self.path = ""
        
        self.permissions = None
        if (self.type == "file"):
            self.permissions = ['r']
        
        if ('encoding' in node_data):
            self.encoding = node_data['encoding']
        else:
            self.encoding = None
        
        if ('content' in node_data):
            if self.encoding == 'base64': # decode if encoded
                self.content = base64.b64decode(node_data['content']).decode('utf-8')
            else:
                self.content = node_data['content']
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
        
        
        
    def get_path(self, root_name = "MAIN_CAT"):
        if (not(self.path)):
            path = []
            current = self
            while current:
                if (current.name!=root_name):
                    path.append(current.name)
                current = current.parent
            return "/"+'/'.join(reversed(path))
        return self.path
    
    
    
    def display_data(self):
        return(f"Data: \n"+
              f"name = {self.name}\n"+
              f"type = {self.type}\n"+
              f"path = {self.path}\n"+
              f"parent = {self.parent}\n"+
              f"children = {self.children}\n"+
              f"content = {self.content}\n"+
              f"metadata = {self.metadata}\n"+
              f"permissions = {self.permissions}\n")
       
       
       
class VFS:
    def __init__(self, vfs_path, root_name="MAIN_CAT"):
        self.root_name = root_name
        self.root = self.load_vfs_from_json(vfs_path)
        self.current_dir = self.root
        
        
        
    def load_vfs_from_json(self, json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            vfs_data = json.load(f)
        return self.build_vfs_tree(vfs_data)
    
    
    
    def build_vfs_tree(self, node_data, parent=None):
        node = VFSNode(node_data)
        
        if parent:
            parent.add_child(node)
        
        # Устанавливаем путь
        if 'path' in node_data:
            node.path = node_data['path']
        else:
            node.path = node.get_path(self.root_name)
        
        # Сохраняем узел в словарь с полным путем как ключом
        dict_all_nodes[node.path] = node
        
        # Рекурсивно обрабатываем детей для директорий
        if node.type == 'directory' and 'children' in node_data:
            for child_data in node_data['children']:
                self.build_vfs_tree(child_data, node)
        
        return node
    
    
    
    def navigate(self, path):
        # Навигация по пути
        if not path or path == '.':
            return self.current_dir
                
        path = path.strip()
        
        if path == root_name:
            path = "/"
        
        # Абсолютный путь
        if path.startswith('/'):
            target_path = path
        else:
            # Относительный путь
            current_path = self.current_dir.get_path(self.root_name)
            target_path = current_path.rstrip('/') + '/' + path
        
        # Нормализуем путь
        target_path = '/'.join(part for part in target_path.split('/') if part)
        target_path = '/' + target_path
        
        # Особые случаи
        if path == '..':
            if self.current_dir.parent:
                return self.current_dir.parent
            return self.current_dir
        
        # Ищем путь в словаре
        if target_path in dict_all_nodes:
            return dict_all_nodes[target_path]
        
        return None
    
    
    
    def list_dir(self, path='', modificator = ""):
        target_dir = self.navigate(path)
                    
        if not target_dir:
            target_dir = self.current_dir
        
        if target_dir.type != 'directory':
            return f"It is a file: {path}"
        
        if (modificator == '--a'):
            result = []
            if target_dir.parent:  # Добавляем родительскую директорию если не корень
                result.append(('..', 'directory'))
            
            for name, node in target_dir.children.items():
                result.append((name, node.display_data()))
        else:
            result = []
            if target_dir.parent:  # Добавляем родительскую директорию если не корень
                result.append(('..', 'directory'))
            
            for name, node in target_dir.children.items():
                result.append((name, node.type))
        
        return result
    
    
    
    def read_file(self, path):
        target_file = self.navigate(path)
        if not target_file:
            return f"File not found: {path}"
        
        if target_file.type != 'file':
            return f"It is a directory: {path}"
        
        if ('r' in target_file.permissions and 'n' not in target_file.permissions):
            return target_file.content
        
        return f"Check file. You might not have enough permissions"
    
    
    
    def write_file(self, path, new_content, add = False):
        target_file = self.navigate(path)
        if not target_file:
            return f"File not found: {path}"
        
        if target_file.type != 'file':
            return f"It is a directory: {path}"
        
        if ('w' in target_file.permissions and 'n' not in target_file.permissions and add):
            target_file.content += str(new_content)
            return f"Success! Content added: {target_file.content}\n"
        elif ('w' in target_file.permissions and 'n' not in target_file.permissions and not add):
            target_file.content = str(new_content)
            return f"Success! Content written: {target_file.content}\n"
        
        return f"Check file. You might not have enough permissions"
    
    
    
    def find(self, pattern):
        results = []
        
        if (pattern == "/"):
            return ['/']
        
        for path, node in dict_all_nodes.items():
            if pattern.lower() in node.name.lower():
                results.append(path)
        
        return results
    
    

class CommandLineInterface:
    def __init__(self, root, vfs_path, script_path, config_path, root_name):
        self.creation_time = datetime.now()
        
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
        self.current_vfs_path = "/"  # Начинаем с корня VFS
        self.prompt = tk.Label(self.input_frame, text=f"{self.get_current_prompt()}>>> ",
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
            self.vfs = VFS(vfs_path, root_name)
        else:
            self.vfs = None
            self.display_output("VFS не загружена: файл не найден или путь не указан\n")
        self.vfs_exists = (self.vfs!=None)  
        self.update_prompt()
        
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
    
    
    def get_current_prompt(self, not_show_all_path = True):
        try:
            if self.vfs_exists and self.vfs:
                # Получаем текущий путь из VFS
                current_path = self.vfs.current_dir.get_path(self.vfs.root_name)
                if not_show_all_path:
                    return current_path if current_path != "" else "/"
                return str(os.getcwd())+'/'+self.vfs_path+(current_path if current_path != "" else "/")
            
        except AttributeError: # костыль. Работает в период от инициализации окна cmd до момента инициализации vfs
            # Fallback на реальную файловую систему
            return str(os.getcwd())
    
    
    
    def update_prompt(self, not_show_all_path = True):
        new_prompt = self.get_current_prompt(not_show_all_path)
        self.prompt.config(text=f"{new_prompt}>>> ")
        
    

    def execute_start_script(self):
        with open(self.script_path, 'r') as script_file:
            commands = script_file.readlines()
        
        for command in commands:
            command = command.strip()
            if command:
                # copied from exec method
                
                if (self.execute_command(start_script = True, command = command)=="ERR"):
                    self.display_output(f"The current start script cannot be done\n")
                    break                
                


    def execute_command(self, event=None, start_script = False, command = ""):
        # get command and clear the field
        if not start_script:
            command = self.input_field.get().strip()
            self.input_field.delete(0, tk.END)
        
        # Display the command
        self.display_output(f">>> {command}\n")
        
        # split the input line into several words
        words = [i for i in command.split()]
        
        # commands
        if (command == ''):
            pass
        
        elif (words[0].lower() in ['exit', 'quit']):
            self.display_output("Exiting...\n")
            self.root.after(1000, self.root.destroy)
            
        elif (words[0].lower() == "help" and len(words)==1):
            help_msg = ("help - to see this message\n"+
                        "exit/quit - to stop the program\n"+
                        "ls [path] [--a] - list directory contents, --a for more info about files in catalogue\n"+
                        "cd <path> - change directory\n"+
                        "find <pattern> - search files and directories with included pattern\n"+
                        "display_short_path [false] - toggle path display\n"+
                        "who - show user and terminal info\n"+
                        "read <path> - get data from file\n"+
                        "write <path> <true/false> - write or add (toggle switch to true) data in file\n"+
                        "chmod <add/rm> <path> <permission> , (permissions: r - read, w - write, n - no access. Can get only 1 at a time)\n"+
                        "rmdir <path> - remove an empty catalogue\n")
            self.display_output(help_msg)
        
        elif (words[0].lower() == 'rmdir'):
            path = words[1]
            target_dir = self.vfs.navigate(path)
            if target_dir:
                if target_dir.type!="file":
                    if target_dir.children:
                        self.display_output("Catalogue is not empty\n")
                    else:
                        del target_dir.parent.children[target_dir.name]
                        if target_dir.path in dict_all_nodes:
                            del dict_all_nodes[target_dir.path]
                            
                        
                        self.display_output(f"Directory removed: {path}")
                else:
                    self.display_output("Got not a catalogue\n")
                
            else:
                self.display_output("Wrong path\n")
            
            
        elif (words[0].lower() == 'chmod'):
            
            if (len(words)<4):
                self.display_output("Not enough args\n")
                return
            
            sub_comm = words[1]
            path = words[2]
            permissions = words[3]
            
            file_for_work = self.vfs.navigate(path)
            
            if file_for_work:
                if file_for_work.type == "file":
                    if (sub_comm.lower() == "add" and (permissions not in file_for_work.permissions)):
                        file_for_work.permissions.append(permissions)
                        self.display_output("Added permissions\n")
                    elif (sub_comm.lower() == "rm" and (permissions in file_for_work.permissions)):
                        file_for_work.permissions.remove(permissions)
                        self.display_output("Removed permissions\n")
                    else:
                        self.display_output("Got wrong arguements\n")
                else:
                    self.display_output("Got directory, not file\n")
            else:
                self.display_output("Wrong path\n")
                
        elif (words[0].lower() == 'ls'):
            if ('--a' in words):
                result = self.vfs.list_dir(command[command.find(' '):].strip(), "--a")           
            else:
                result = self.vfs.list_dir(command[command.find(' '):].strip())
                
            if isinstance(result, list): # if result.type() == list
                for name, type_ in result:
                    self.display_output(f"{name} ({type_})\n")
            else:
                self.display_output(f"{result}\n")
        
        elif (words[0].lower() == 'read'):
            self.display_output(f"{self.vfs.read_file(command[command.find(' '):])}\n")
            
        elif (words[0].lower() == 'write'):
            path = words[1]
            add = False
            if words[2] == "true":
                add = True
            cont = ' '.join(words[3:])
            self.display_output(f"{self.vfs.write_file(path, cont, add)}\n") #path, new_content, add = False
            
        elif (words[0].lower() == 'cd'):
            path = command[command.find(' '):].strip()
            new_dir = self.vfs.navigate(path)
            
            if new_dir and new_dir.type == 'directory':
                self.vfs.current_dir = new_dir
                self.display_output(f"Changed directory to {new_dir.get_path(self.vfs.root_name)}\n")
            else:
                self.display_output(f"Directory not found: {path}\n")
            
            # ОБНОВЛЯЕМ ПРОМПТ ПОСЛЕ СМЕНЫ ДИРЕКТОРИИ
            self.update_prompt()
        
        elif (words[0].lower() == 'display_short_path'):
            if ('false' in words):
                self.update_prompt(False)
            else:
                self.update_prompt()
            self.display_output(f"The output changed \n")
        
        elif (words[0].lower() == 'who'):
            self.display_output(f"Current user: {os.getlogin()} \n"
                                + f"Current terminal: CMD ANALOG \n"
                                + f"Time of accessing this terminal: {self.creation_time} \n"
                                + f"Time of using this terminal: {datetime.now() - self.creation_time} \n")
        
        elif (words[0].lower() == 'find'):
            if len(words) > 1:
                pattern = ' '.join(words[1:])
                results = self.vfs.find(pattern)
                if results:
                    for result in results:
                        self.display_output(f"{result}\n")
                else:
                    self.display_output("No files or directories found\n")
            else:
                self.display_output("Usage: find <pattern>\n")
            
        else:               
            self.display_output(f"Unknown command: {command}\n")
            if start_script:
                return "ERR"
        
        words = []
    


def parse_arguments(): 
    parser = argparse.ArgumentParser(description='CMD ANALOG')
    # description - the first line of the "help" message
    parser.add_argument('--vfs', type=str,
                help='Path to VFS physical location, preferable to place this file in the same directory as this code file')
    parser.add_argument('--script', type=str,
                help='Path to startup script, preferable to place this file in the same directory as this code file')
    parser.add_argument('--config', type=str, default='config4task.ini',
                help='Path to config file (default: config4task.ini). Please, place config3task.ini and the default files in the same directory as this code file')
    parser.add_argument('--root_name', type=str,
                help='Name of the root in vfs, default: "MAIN_CAT"')
    # arguements: (key for search of the arg, type of this arg, the message we get in case of typing "python main.py --help")
    
    return parser.parse_args()



def parse_config_file(config_path):
    # .ini file - .txt with special structure and saved in a special way
    # struct:
    #
    # [DEFAULT]
    # vfs_path = vfs.json
    # script_path = vfs_start_script.txt
    # root_name = MAIN_CAT
        
    config = configparser.ConfigParser()
    vfs_path = None
    script_path = None
    root_name = "MAIN_CAT"
    
    if os.path.exists(config_path):
        config.read(config_path)
        if 'DEFAULT' in config:
            if 'vfs_path' in config['DEFAULT']:
                vfs_path = config['DEFAULT']['vfs_path']
            if 'script_path' in config['DEFAULT']:
                script_path = config['DEFAULT']['script_path']
            if 'root_name' in config['DEFAULT']:
                root_name = config['DEFAULT']['root_name']
    
    return vfs_path, script_path, root_name
     


if __name__ == "__main__":
    args = parse_arguments()
    
    vfs_path, script_path, root_name = parse_config_file(args.config)
    
    # priority
    if args.vfs:
        vfs_path = args.vfs
    if args.script:
        script_path = args.script
    
    # if file is open from cmd, then it prints information in concole
#     print(f"Info: VFS path = {vfs_path}")
#     print(f"Info: Script path = {script_path}")
#     print(f"Info: Config file = {args.config}")
    
    root = tk.Tk()
    cli = CommandLineInterface(root, vfs_path, script_path, args.config, root_name)
    root.mainloop()

