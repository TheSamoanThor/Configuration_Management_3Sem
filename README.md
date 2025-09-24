# Configuration_Management_3Sem
<hr>
<h2>Краткое описание</h2>
<p>В коде создан класс, в котором идет обработка простейших команд, создание и отрисовка окна для взаимодействия с системой, методы по выводу сообщений от программы.</p>
<p>В репозитории хранятся стартовые файлы для возможной работы с программой. Среди них конфигурационные файлы (config2task.ini, config3task.ini и config4task.ini), файл со стартовыми командами (vfs_start_script.txt), файл с организацией файлов виртуальной файловой системы (vfs_struct_file.txt), файл с командами, который не выполнится до конца, так как это продемонстрирует одно из условий задания (vfs_start_script_w_bugs.txt), файл для 3-5 задач с структурой vfs (vfs.json), файл для создания vfs.json (json_former.py), файлы для теста кода (TESTS_task_2.bat и TESTS_task_3.bat).</p>
<p>Для тестов 5 задания пользоваться файлами vfs.json, vfs_start_script_w_bugs.txt, vfs_start_script.txt, TESTS_task_3.bat, config4task.ini.</p>
<p>Пожалуйста, храните эти файлы в одной директории с кодом, чтобы не возникло лишних проблем. Если что, Вы были предупреждены :)</p>
<p>При запуске файла для тестов (.bat) удостоверьтесь, что имя файла с кодом соответствует имени файла в тестовом файле. Сделать это возможно через "Блокнот".</p>
<p>Также прошу принять во внимание структуру vfs, описанную в .json файле. При тестировании и создании своей структуры необходимо опираться на уже существующие "теги".</p>

<h2>Методы класса CommandLineInterface</h2>
<ol>
<li>__init__</li>
<li>display_welcome</li>
<li>display_output</li>
<li>execute_command</li>
<li>display_config</li>
<li>execute_start_script</li>
<li>get_current_prompt</li>
<li>update_prompt</li>
</ol>
<hr>
<h3>__init__</h3>
<p>Отрисовывает окно взаимодействия, поля для ввода и вывода текста, заголовок рабочей зоны. Инициализирует VFS, загружает стартовый скрипт.</p>

<h3>display_welcome</h3>
<p>Выводит приветственное сообщение программы при помощи display_output.</p>

<h3>display_output</h3>
<p>Вывод работы программы на экран. Временно включает текстовый виджет, вставляет текст, прокручивает к концу и снова отключает виджет.</p>

<h3>execute_start_script</h3>
<p>Вывод на экран работы программы по обработке команд из внешнего файла со стартовыми командами.</p>

<h3>display_config</h3>
<p>Вывод на экран информации о конфиге и его содержимом.</p>

<h3>execute_command</h3>
<p>Обработчик команд. Сейчас доступны:</p>
<ol>
<li>exit/quit - завершение программы</li>
<li>ls [path] [--a] - список содержимого директории (--a для подробной информации)</li>
<li>cd path - смена директории</li>
<li>read file - чтение содержимого файла</li>
<li>write path true/false content - запись или добавление данных в файл</li>
<li>find pattern - поиск файлов и директорий по шаблону</li>
<li>display_short_path [false] - переключение отображения пути</li>
<li>who - информация о пользователе и терминале</li>
<li>help - справка по командам</li>
<li>chmod add/rm path permission - управление правами доступа к файлу</li>
<li>rmdir path - удаление пустой директории</li>
</ol>

<h3>get_current_prompt</h3>
<p>Возвращает текущий путь для отображения в приглашении командной строки.</p>

<h3>update_prompt</h3>
<p>Обновляет отображение приглашения командной строки.</p>

<hr>
<h2>Методы класса VFS</h2>
<ol>
<li>__init__</li>
<li>load_vfs_from_json</li>
<li>build_vfs_tree</li>
<li>navigate</li>
<li>list_dir</li>
<li>read_file</li>
<li>write_file</li>
<li>find</li>
</ol>
<hr>
<h3>__init__</h3>
<p>Конструктор, создает корень VFS.</p>

<h3>load_vfs_from_json</h3>
<p>Открывает .json файл и вызывает метод build_vfs_tree для построения иерархии vfs.</p>

<h3>build_vfs_tree</h3>
<p>Метод проходится рекурсивно по всем узлам в .json файле и создает их, в зависимости от их типа - директория или файл. Также добавляет дочерние файлы родительским. Сохраняет узлы в глобальный словарь dict_all_nodes.</p>

<h3>navigate</h3>
<p>Навигация по VFS. Поддерживает абсолютные и относительные пути, специальные случаи (., .., корень).</p>

<h3>list_dir</h3>
<p>Выводит содержимое директории. С модификатором --a показывает подробную информацию о файлах.</p>

<h3>read_file</h3>
<p>Читает содержимое файла из VFS.</p>

<h3>write_file</h3>
<p>Записывает или добавляет содержимое в файл VFS с проверкой прав доступа.</p>

<h3>find</h3>
<p>Поиск файлов и директорий по шаблону в имени.</p>

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
<p>Конструктор, создает элемент vfs, определяя большинство полей непосредственно из входных данных. Поддерживает base64 декодирование содержимого.</p>

<h3>add_child</h3>
<p>Добавляет дочерний узел и устанавливает родительскую связь.</p>

<h3>get_path</h3>
<p>Возвращает путь до объекта, если таковой не был задан в .json файле. Строит путь на основе родительской иерархии.</p>

<h3>display_data</h3>
<p>Возвращает строку с подробной информацией о файле или директории.</p>

<hr>
<h2>Дополнительные функции</h2>
<ol>
<li>parse_arguments</li>
<li>parse_config_file</li>
</ol>
<hr>
<h3>parse_arguments</h3>
<p>Функция для получения аргуметов из командной строки ОС и их передачи в программу. Поддерживает аргументы: --vfs, --script, --config, --root_name.</p>

<h3>parse_config_file</h3>
<p>Функция для чтения базовых значений из файла конфига - по умолчанию config.ini. Этот файл идет вместе с другими в этом репозитории. Чтает параметры из секции [DEFAULT].</p>






<hr>
<h2>Brief Description</h2>
<p>The code creates a class that processes basic commands, creates and draws a window for interacting with the system, and contains methods for displaying program messages.</p>
<p>The repository stores startup files for working with the program. These include configuration files (config2task.ini and config3task.ini), a file with startup commands (vfs_start_script.txt), a file with the virtual file system file organization (vfs_struct_file.txt), a file with commands that will not be executed to completion because one of the task conditions demonstrates this (vfs_start_script_w_bugs.txt), a file for task 3 with the vfs structure (vfs.json), a file for creating vfs.json (json_former.py), and files for testing the code (TESTS_task_2.bat and TESTS_task_3.bat).</p>
<p>For testing task 4, use the files from task 3.</p>
<p>Please store these files in the same directory as your code to avoid unnecessary problems. Just in case, you've been warned :)</p>
<p>When running the test file (.bat), make sure the filename containing the code matches the filename in the test file. You can do this using Notepad.</p>
<p>Also, please take into account the vfs structure described in the .json file. When testing and creating your own structure, you should rely on existing "tags."</p>

<h2>CommandLineInterface Class Methods</h2>
<ol>
<li>__init__</li>
<li>display_welcome</li>
<li>display_output</li>
<li>execute_command</li>
<li>display_config</li>
<li>execute_start_script</li>
<li>get_current_prompt</li>
<li>update_prompt</li>
</ol>
<hr>
<h3>__init__</h3>
<p>Renders the interaction window, text input and output fields, and the workspace title. Initializes the VFS and loads the startup script.</p>

<h3>display_welcome</h3>
<p>Displays the program's welcome message using display_output.</p>

<h3>display_output</h3>
<p>Displays the program's work on the screen. Temporarily enables the text widget, inserts text, scrolls to the end, and disables the widget again.</p>

<h3>execute_start_script</h3>
<p>Displays the program's work processing commands from an external file with startup commands.</p>

<h3>display_config</h3>
<p>Displays information about the configuration file and its contents.</p>

<h3>execute_command</h3>
<p>Command handler. Currently available:</p>
<ol>
<li>exit/quit - exit the program</li>
<li>ls [path] [--a] - list directory contents (--a for details)</li>
<li>cd path - change directory</li>
<li>read file - read file contents</li>
<li>write path true/false content - write or append data to a file</li>
<li>find pattern - search for files and directories by pattern</li>
<li>display_short_path [false] - toggle path display</li>
<li>who - user and terminal information</li>
<li>help - command help</li>
<li>chmod add/rm path permission - manage file access rights</li>
<li>rmdir path - delete empty Directories</li>
</ol>

<h3>get_current_prompt</h3>
<p>Returns the current path to display in the command prompt.</p>

<h3>update_prompt</h3>
<p>Updates the command prompt.</p>

<hr>
<h2>VFS Class Methods</h2>
<ol>
<li>__init__</li>
<li>load_vfs_from_json</li>
<li>build_vfs_tree</li>
<li>navigate</li>
<li>list_dir</li>
<li>read_file</li>
<li>write_file</li>
<li>find</li>
</ol>
<hr>
<h3>__init__</h3>
<p>Constructor, creates root VFS.</p>

<h3>load_vfs_from_json</h3>
<p>Opens a .json file and calls the build_vfs_tree method to build a VFS hierarchy.</p>

<h3>build_vfs_tree</h3>
<p>This method recursively loops through all nodes in the .json file and creates them depending on their type—directory or file. It also appends child files to their parent. Saves nodes to the global dictionary dict_all_nodes.</p>

<h3>navigate</h3>
<p>Navigates the VFS. Supports absolute and relative paths, special cases (., .., root).</p>

<h3>list_dir</h3>
<p>Displays the contents of a directory. With the --a modifier, displays detailed file information.</p>

<h3>read_file</h3>
<p>Reads the contents of a file from the VFS.</p>

<h3>write_file</h3>
<p>Writes or appends contents to a VFS file, checking access rights.</p>

<h3>find</h3>
<p>Search for files and directories based on a pattern in their names.</p>

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
<p>Constructor; creates a VFS element, defining most of the fields directly from the input data. Supports base64 decoding of content.</p>

<h3>add_child</h3>
<p>Adds a child node and establishes a parent relationship.</p>

<h3>get_path</h3>
<p>Returns the path to the object if one is not specified in the .json file. Builds the path based on the parent hierarchy.</p>

<h3>display_data</h3>
<p>Returns a string with detailed information about a file or directory.</p>

<hr>
<h2>Additional Functions</h2>
<ol>
<li>parse_arguments</li>
<li>parse_config_file</li>
</ol>
<hr>
<h3>parse_arguments</h3>
<p>A function for receiving arguments from the OS command line and passing them to a program. Supports the following arguments: --vfs, --script, --config, --root_name.</p>

<h3>parse_config_file</h3>
<p>A function for reading basic values ​​from a configuration file - config.ini by default. This file is included with others in this repository. Reads parameters from the [DEFAULT] section.</p>
<hr>

