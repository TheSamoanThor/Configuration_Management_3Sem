@echo off
echo === Basic Test ===
echo Test 1: No parameters 
python file_for_tasks.py --help
echo.

echo Test 2: Only VFS 
python file_for_tasks.py --vfs vfs.json
echo.

echo Test 3: Only script
python file_for_tasks.py --script vfs_start_script.txt
echo.

echo Test 4: Both parameters
python file_for_tasks.py --vfs vfs.json --script vfs_start_script.txt
echo.

echo Test 5: Script with stop
python file_for_tasks.py --script vfs_start_script_w_bugs.txt
echo.

echo Test 6: Config
python file_for_tasks.py --config config.ini
echo.

echo Basic tests were finished successfully
pause
