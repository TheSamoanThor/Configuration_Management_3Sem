# Configuration_Management_3Sem
<hr>

<h2>Краткое описание</h2>

В коде создан класс, в котором идет обработка простейших команд, создание и отрисовка окна для взаимодействия с системой, методы по выводу сообщений от программы.<br>
В репозитории хранятся стартовые файлы для возможной работы с программой. Среди них конфигурационный файл (config.ini), файл со стартовыми командами (vfs_start_script.txt), файл с организацией файлов виртуальной файловой системы (vfs_struct_file.txt), файл с командами, который не выполнится до конца, так как это продемонстрирует одно из условий задания (vfs_start_script_w_bugs.txt)<br>
Пожалуйста, храните эти файлы в одной директории с кодом, чтобы не возникло лишних проблем. Если что, Вы были предупреждены :) <br>

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

The code contains a class that processes basic commands, creates and draws a window for interacting with the system, and contains methods for displaying program messages.<br>
The repository contains startup files for running the program. These include the configuration file (config.ini), a file with startup commands (vfs_start_script.txt), a file organizing the virtual file system files (vfs_struct_file.txt), and a file with commands that will not be executed completely due to one of the task conditions (vfs_start_script_w_bugs.txt).<br>
Please store these files in the same directory as the code to avoid unnecessary problems. Just in case, you've been warned :) <br>

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
Draws the interaction window, text input and output fields, and the title of the work area.

<h3>display_welcome</h3>
Displays the program's welcome message using display_output.

<h3>display_output</h3>
Displaying the program's progress on the screen.

<h3>execute_start_script</h3>
Displaying the program's progress in processing commands from an external file with startup scripts. Commands

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

<h2>Additional functions</h2>

<ol>
<li>parse_arguments</li>
<li>parse_config_file</li>
</ol>

<hr>

<h3>parse_arguments</h3>
Function for receiving arguments from the OS command line and passing them to a program.

<h3>parse_config_file</h3>
Function for reading basic values ​​from a configuration file - config.ini by default. This file is included with others in this repository.

<hr>

