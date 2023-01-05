@echo off

curl -L -o "vc_buildtools.exe" "https://aka.ms/vs/16/release/vc_buildtools.exe"
call vc_buildtools.exe --quiet --wait --norestart --nocache --installPath "C:\BuildTools"

rem Check if virtualenv is already installed
pip list | findstr virtualenv
if %ERRORLEVEL% NEQ 0 (
  rem virtualenv is not installed, install it
  pip install virtualenv 
)
rem Get the file path of the batch script
for %%I in ("%~f0") do set script_path=%%~dpI

rem Check if virtual environment already exists
if exist "%script_path%\NLP_APP_VNV" (
  rem Virtual environment exists, print directory
  echo The virtual environment is located at: "%script_path%\NLP_APP_VNV"
) else (
  rem Virtual environment does not exist, create it
  virtualenv "%script_path%\NLP_APP_VNV"

)
python -V

rem Activate virtual environment
call "%script_path%\NLP_APP_VNV\Scripts\activate.bat"
python -V

rem Get the file path of the batch script
for %%I in ("%~f0") do set script_path=%%~dpI

rem Check if virtual environment is already active
if not defined VIRTUAL_ENV (
  rem Virtual environment is not active, print message
  echo Virtual environment is not active
) else (
  rem Virtual environment is active, print name
  echo The active virtual environment is located at: %VIRTUAL_ENV%
)

rem Replace the last directory of the file path with req.txt
set req_path="%script_path%\req.txt"
set app_path="%script_path%\NLPverse_Medidocx_app_5.py"
rem Install requirements from requirements.txt
pip install -r "%req_path%"

rem Run Streamlit app
streamlit run "%app_path%"
