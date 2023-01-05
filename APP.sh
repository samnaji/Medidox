#!/bin/bash

# Check if Python is already installed
python3 -V
if [ $? -ne 0 ]; then
  # Python is not installed, install it
  apt-get update
  apt-get install -y python3
fi

# Check if virtualenv is already installed
pip3 list | grep virtualenv
if [ $? -ne 0 ]; then
  # virtualenv is not installed, install it
  pip3 install virtualenv
fi
# Get the file path of the bash script
#script_path=$(dirname "$0")
#script_path="${BASH_SOURCE[0]}"
cd "$(dirname "$0")"
script_path=$(pwd)
echo $script_path
# Check if virtual environment already exists
if [ -d "$script_path/NLP_APP_VNV" ]; then
  # Virtual environment exists, print directory
  echo "The virtual environment is located at: $script_path/NLP_APP_VNV"
else
  # Virtual environment does not exist, create it
  virtualenv "$script_path/NLP_APP_VNV" 

fi

# Activate virtual environment
source "$script_path/NLP_APP_VNV/bin/activate"


# Replace the last directory of the file path with req.txt
req_path="${script_path}/req.txt"
app_path="${script_path}/NLPverse_Medidocx_app_5.py"
# Install requirements from requirements.txt
pip install -r "$req_path"

# Run Streamlit app
streamlit run  "$app_path"