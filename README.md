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
<h2>Short description</h2>
<p>The code has created a class in which the simplest commands are processed, a window is created and drawn for interacting with the system, and methods for outputting messages from the program.</p>
<p>The repository stores the startup files for possible work with the program. Among them are configuration files (config2task.ini, config3task.ini and config4task.ini), a file with startup commands (vfs_start_script.txt ), a file with the organization of virtual file system files (vfs_struct_file.txt ), a command file that will not run to the end, as this will demonstrate one of the conditions of the task (vfs_start_script_w_bugs.txt ), file for 3-5 tasks with a vfs structure (vfs.json), a file for creating a vfs.json (json_former.py ), files for the code test (TESTS_task_2.bat and TESTS_task_3.bat).</p>
<p>For the 5 task tests, use vfs files.json, vfs_start_script_w_bugs.txt, vfs_start_script.txt, TESTS_task_3.bat, config4task.ini.</p>
<p>Please keep these files in the same directory as the code so that there are no unnecessary problems. If anything, you've been warned :)</p>
<p>When running the test file (.bat) make sure that the file name with the code matches the file name in the test file. This can be done through Notepad.</p>
<p>I also ask you to take into account the vfs structure described in .a json file. When testing and creating your own structure, you need to rely on existing "tags".</p>

<h2>Methods of the CommandLineInterface class</h2>
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
<p>Renders the interaction window, text input and output fields, and the workspace title. Initializes the VFS, loads the startup script.</p>

<h3>display_welcome</h3>
<p>Displays the welcome message of the program using display_output.</p>

<h3>display_output</h3>
<p>Displaying the program on the screen. Temporarily enables the text widget, inserts the text, scrolls to the end, and disables the widget again.</p>

<h3>execute_start_script</h3>
<p>Displaying the program for processing commands from an external file with the start commands.</p>

<h3>display_config</h3>
<p>Displays information about the configuration and its contents.</p>

<h3>execute_command</h3>
<p>The command handler. Available now:</p>
<ol>
<li>exit/quit - program termination</li>
<li>ls [path] [--a] - list of directory contents (--a for details)</li>
<li>cd path - directory change</li>
<li>read file - reading the contents of a file</li>
<li>write path true/false content - write or add data to a file</li>
<li>find pattern - search for files and directories using a template</li>
<li>display_short_path [false] - switching the path display</li>
<li>who - information about the user and the terminal</li>
<li>help - help on commands</li>
<li>chmod add/rm path permission - file access rights management</li>
<li>rmdir path - deleting an empty directory</li>
</ol>

<h3>get_current_prompt</h3>
<p>Returns the current path to display in the command prompt.</p>

<h3>update_prompt</h3>
<p>Updates the display of the command prompt.</p>

<hr>
<h2>Methods of the VFS class</h2>
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
<p>The constructor creates the VFS root.</p>

<h3>load_vfs_from_json</h3>
<p>Opens it .a json file and calls the build_vfs_tree method to build the vfs hierarchy.</p>

<h3>build_vfs_tree</h3>
<p>The method traverses recursively through all nodes in .a json file and creates them, depending on their type - directory or file. It also adds child files to the parent files. Saves nodes to the global dict_all_nodes dictionary.</p>

<h3>navigate</h3>
<p>VFS navigation. Supports absolute and relative paths, special cases (., .., root).</p>

<h3>list_dir</h3>
<p>Outputs the contents of the directory. With the --a modifier, it shows detailed information about files.</p>

<h3>read_file</h3>
<p>Reads the contents of the file from VFS.</p>

<h3>write_file</h3>
<p>Writes or adds content to a VFS file with access verification.</p>

<h3>find</h3>
<p>Search for files and directories by the template in the name.</p>

<hr>
<h2>Methods of the VFSNode class</h2>
<ol>
<li>__init__</li>
<li>add_child</li>
<li>get_path</li>
<li>display_data</li>
</ol>
<hr>
<h3>__init__</h3>
<p>The constructor creates a vfs element by defining most of the fields directly from the input data. Supports base64 content decoding.</p>

<h3>add_child</h3>
<p>Adds a child node and establishes a parent relationship.</p>

<h3>get_path</h3>
<p>Returns the path to the object, if none was specified in .a json file. Builds a path based on the parent hierarchy.</p>

<h3>display_data</h3>
<p>Returns a string with detailed information about the file or directory.</p>

<hr>
<h2>Additional functions</h2>
<ol>
<li>parse_arguments</li>
<li>parse_config_file</li>
</ol>
<hr>
<h3>parse_arguments</h3>
<p>A function for receiving arguments from the OS command line and transferring them to the program. Supports arguments: --vfs, --script, --config, --root_name.</p>

<h3>parse_config_file</h3>
<p>The function for reading basic values from the config file is config.ini by default. This file goes along with others in this repository. Reads parameters from the [DEFAULT] section.</p>

