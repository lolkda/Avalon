@echo off
setlocal enabledelayedexpansion

:: 设置要查找和替换的目标字符串
set "target=.cpython-311-x86_64-linux-gnu"
set "replacement="

echo ====================================================
echo  Cython Filename Cleanup Script
echo ====================================================
echo.
echo  Target to remove: "%target%"
echo  Searching in the current directory and subdirectories...
echo.

:: 使用 for /r 命令递归遍历当前目录(.)及其所有子目录
:: "delims=" 确保完整文件名被捕获，即使它包含空格
for /r "." %%F in ("*%target%*") do (
    set "filepath=%%~fF"
    set "filename=%%~nxF"
    set "filedir=%%~dpF"

    :: 使用字符串替换功能来生成新的文件名
    set "newfilename=!filename:%target%=%replacement%!"

    :: 检查文件名是否真的发生了改变，避免不必要的操作
    if not "!newfilename!"=="!filename!" (
        echo Renaming: "!filename!"
        echo      -->: "!newfilename!"
        
        :: 执行重命名命令
        ren "%%~fF" "!newfilename!"
        
        echo  [OK] Renamed successfully.
        echo.
    )
)

echo ====================================================
echo  Script finished.
echo ====================================================
echo.
pause