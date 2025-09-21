# Configuration_Management_3Sem
<hr>

<h2>Краткое описание</h2>

В коде создан класс, в котором идет обработка простейших команд, создание и отрисовка окна для взаимодействия с системой, методы по выводу сообщений от программы.<br>
В репозитории хранятся стартовые файлы для возможной работы с программой. Среди них конфигурационные файлы (config2task.ini и config3task.ini), файл со стартовыми командами (vfs_start_script.txt), файл с организацией файлов виртуальной файловой системы (vfs_struct_file.txt), файл с командами, который не выполнится до конца, так как это продемонстрирует одно из условий задания (vfs_start_script_w_bugs.txt), файл для 3 задачи с структурой vfs (vfs.json), файл для создания vfs.json (json_former.py), файлы для теста кода (TESTS_task_2.bat и TESTS_task_3.bat) <br>
Пожалуйста, храните эти файлы в одной директории с кодом, чтобы не возникло лишних проблем. Если что, Вы были предупреждены :) <br>
При запуске файла для тестов (.bat) удостоверьтесь, что имя файла с кодом соответствует имени файла в тестовом файле. Сделать это возможно через "Блокнот". <br>
Также прошу принять во внимание структуру vfs, описанную в .json файле. При тестировании и создании своей структуры необходимо опираться на уже существующие "теги" <br>
<h2>Методы класса CommandLineInterface</h2>

<ol> 
  <li>__init__</li>
  <li>display_welcome</li>
  <li>display_output</li>
  <li>execute_command</li>
  <li>display_config</li>
  <li>execute_start_script</li>
</ol>

<hr>

<h3>__init__</h3>
Отрисовывает окно взаимодействия, поля для ввода и вывода текста, заголовок рабочей зоны

<h3>display_welcome</h3>
Выводит приветственное сообщение программы при помощи display_output 

<h3>display_output</h3>
Вывод работы программы на экран

<h3>execute_start_script</h3>
Вывод на экран работы программы по обработке команд из внешнего файла со стартовыми командами

<h3>display_config</h3>
Вывод на экран информации о конфиге и его содержимом

<h3>execute_command</h3>
Обработчик команд. Сейчас доступны:
<ol> 
  <li>exit/quit</li>
  <li>ls</li>
  <li>cd</li>
  <li>help</li>
</ol>
<hr>

<h2>Методы класса VFS</h2>

<ol> 
  <li>__init__</li>
  <li>load_vfs_from_json</li>
  <li>build_vfs_tree</li>
</ol>

<hr>

<h3>__init__</h3>
Конструктор, создает корень

<h3>load_vfs_from_json</h3>
Открывает .json файл и вызывает метод build_vfs_tree для построения иерархии vfs

<h3>build_vfs_tree</h3>
Метод проходится рекурсивно по всем узлам в .json файле и создает их, в зависимости от их типа - директория или файл. Также добавляет дочерние файлы родительским

<hr>

<h2>Методы класса VFSNode</h2>

<ol> 
  <li>__init__</li>
  <li>add_child</li>
  <li>get_path</li>
  <li>display_data</li>
</ol>

<hr>

<h3>__init__</h3>
Конструктор, создает элемент vfs, определяя большинство полей непосредственно из входных данных

<h3>add_child</h3>
Добавляет дочерний файл

<h3>get_path</h3>
Возвращает путь до объекта, если таковой не был задан в .json файле

<h3>display_data</h3>
Выводит информацию о файле или директории

<hr>

<h2>Дополнительные функции</h2>

<ol> 
  <li>parse_arguments</li>
  <li>parse_config_file</li>
</ol>

<hr>

<h3>parse_arguments</h3>
Функция для получения аргуметов из командной строки ОС и их передачи в программу

<h3>parse_config_file</h3>
Функция для чтения базовых значений из файла конфига - по умолчанию config.ini. Этот файл идет  вместе с другими в этом репозитории

<hr>









<h2>Brief Description</h2>

The code creates a class that processes basic commands, creates and draws a window for interacting with the system, and contains methods for displaying program messages.<br>
The repository stores startup files for working with the program. These include configuration files (config2task.ini and config3task.ini), a file with startup commands (vfs_start_script.txt), a file with the virtual file system file structure (vfs_struct_file.txt), a file with commands that will not be executed completely due to one of the task conditions (vfs_start_script_w_bugs.txt), a file for task 3 with the vfs structure (vfs.json), a file for creating vfs.json (json_former.py), and files for testing the code (TESTS_task_2.bat and TESTS_task_3.bat). <br>
Please store these files in the same directory as the code to avoid any problems. Just in case, you've been warned :) <br>
When running the test file (.bat), make sure the code filename matches the filename in the test file. This can be done using Notepad. <br>
Also, please take into account the vfs structure described in the .json file. When testing and creating your own structure, you should rely on existing "tags" <br>
<h2>CommandLineInterface Class Methods</h2>

<ol>
<li>__init__</li>
<li>display_welcome</li>
<li>display_output</li>
<li>execute_command</li>
<li>display_config</li>
<li>execute_start_script</li>
</ol>

<hr>

<h3>__init__</h3>
Draws the interaction window, text input and output fields, and the title of the work area

<h3>display_welcome</h3>
Displays the program's welcome message using display_output

<h3>display_output</h3>
Displaying the program's work on the screen

<h3>execute_start_script</h3>
Displaying the program's work on the screen for processing commands from an external file with start-up Commands

<h3>display_config</h3>
Displays information about the configuration file and its contents.

<h3>execute_command</h3>
Command handler. Currently available:
<ol>
<li>exit/quit</li>
<li>ls</li>
<li>cd</li>
<li>help</li>
</ol>
<hr>

<h2>VFS Class Methods</h2>

<ol>
<li>__init__</li>
<li>load_vfs_from_json</li>
<li>build_vfs_tree</li>
</ol>

<hr>

<h3>__init__</h3>
Constructor, creates root

<h3>load_vfs_from_json</h3>
Opens a .json file and calls the build_vfs_tree method to build a vfs hierarchy.

<h3>build_vfs_tree</h3>
This method recursively loops through all nodes in the .json file and creates them based on their type. - directory or file. Also adds child files to the parent.

<hr>

<h2>VFSNode Class Methods</h2>

<ol>
<li>__init__</li>
<li>add_child</li>
<li>get_path</li>
<li>display_data</li>
</ol>

<hr>

<h3>__init__</h3>
Constructor; creates a VFS element, defining most fields directly from the input data.

<h3>add_child</h3>
Adds a child file.

<h3>get_path</h3>
Returns the path to the object if one was not specified in the .json file.

<h3>display_data</h3>
Displays information about a file or directory.

<hr>

<h2>Additional Functions</h2>

<ol>
<li>parse_arguments</li>
<li>parse_config_file</li>
</ol>

<hr>

<h3>parse_arguments</h3>
A function for receiving arguments from the OS command line and passing them to a program.

<h3>parse_config_file</h3>
A function for reading basic values ​​from a configuration file - config.ini by default. This file is included with others in this repository.

<hr>
