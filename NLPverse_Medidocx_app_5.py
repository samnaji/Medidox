import streamlit as st
import time
import subprocess
import os
import sys


st.set_page_config(page_title="NLPverse for Medidocx", layout='centered')

# Set the app title and theme
st.title("NLPverse for Medidocx")
st.markdown("We designed this app to help you easily clean and improve the quality of your raw docx documents. Upload the folder containing all your files and where you want to store the results. Our advanced processing algorithms will remove non-English characters, fix grammar mistakes, and paraphrase the content to ensure that the final version is clear, concise, and easy to read. The resulting document will retain the same context and meaning as the original but with a polished, professional finish.")
st.subheader("Things to keep in mind")
st.write("* Ensure that the documents you upload are in .docx or .doc format")
st.write("* The name of the file should start with the patient name and surname examples: name_surname...docx ; name, surname...docx ; or name-surname...docx")
st.write("* While reviewing resulted documents to add to the training pipeline, please do not move paragraphs or add any line breaks")

st.sidebar.title("Choose a task:")

# Find the path to the Python executable in the virtual environment
#python_path = subprocess.run(['which', 'python'], capture_output=True).stdout.strip()
python_path = sys.executable
# Add a tab selector to the sidebar
#selected_tab = st.sidebar.radio("", ["Auto Inference","Inference", "Train"])
selected_tab = st.sidebar.radio("", ["Inference", "Train"])

#scripts relative location 
script_path = os.path.realpath(__file__)
head, tail = os.path.split(script_path)
full_path=os.path.join(head, "")
# Display the Auto Inference tab
if selected_tab == "Auto Inference":
    st.markdown("## Auto Inference")
    dir_in = st.text_input("Enter the directory of the input folder:")
    dir_out = st.text_input("Enter the directory of the output folder:")
    dir_train = st.text_input("Enter the directory of the folder to move docs to:")
    dir_model = st.text_input("Enter the directory of the folder that has the models:")
    Marker_input = st.text_input("Please enter the marker you used to mark sensetive text:")
    num_outputs = st.number_input("Number of outputs (default: 1):", value=1)
    num_v = st.number_input("The version of the model (most recent: 1; 2 is the second most recent):", value=1)
    delay= st.number_input("Time to wait before processing the folder again, in minutes:", value=1)

    #dir_in=r"/Users/mayssamnaji/Desktop/train/input"
    #dir_out=r"/Users/mayssamnaji/Desktop/train/output"
    #dir_model= r"/Users/mayssamnaji/Desktop/train/model"
    #dir_train=r"/Users/mayssamnaji/Desktop/train/train"
    num_v=num_v-1
    Start=False
    if st.button("Start"): 
      Start=True
      print("Inference started")
      # run this command every delay 
        #subprocess.run(["python", "scripts/dummy.py"])
      # stop the inverence
       # subprocess.run(["python", "scripts/inference_fulltext_v4.py", dir_in, dir_out, dir_train, dir_model, str(num_outputs), str(num_v), Marker_input])
    while Start:
      subprocess.run(["python", os.path.join(full_path,"inference_fulltext_v5.py"), dir_in, dir_out, dir_train, dir_model, str(num_outputs), str(num_v), Marker_input])
      if st.button("Stop"): 
        Start=False
        print("stopped")
      time.sleep(delay)


if selected_tab == "Inference":
    st.markdown("## Inference")
    dir_in = st.text_input("Enter the directory of the input folder:")
    dir_out = st.text_input("Enter the directory of the output folder:")
    dir_train = st.text_input("Enter the directory of the folder to move docs to:")
    dir_model = st.text_input("Enter the directory of the folder that has the models:")
    Marker_input = st.text_input("Please enter the marker you used to mark sensetive text:",value="Ğ")
    num_outputs = st.number_input("Number of outputs (default: 1):", value=1)
    num_v = st.number_input("The version of the model (most recent: 1; 2 is the second most recent):", value=1)
    
    dir_in=r"/Users/mayssamnaji/Desktop/train/input"
    dir_out=r"/Users/mayssamnaji/Desktop/train/output"
    dir_model= r"/Users/mayssamnaji/Desktop/train/model"
    dir_train= r"/Users/mayssamnaji/Desktop/train/train"

    # dir_in=r"C:\Users\mayss\OneDrive\Desktop\train\input"
    # dir_out=r"C:\Users\mayss\OneDrive\Desktop\train\output"
    # dir_model= r"C:\Users\mayss\OneDrive\Desktop\train\model"
    # dir_train=r"C:\Users\mayss\OneDrive\Desktop\train\train"
    Marker_input="Ğ"
    num_v=num_v-1
    if st.button("Process"): 
        #subprocess.run(["python", os.path.join(full_path,"inference_fulltext_v5.py"), dir_in, dir_out, dir_train, dir_model, str(num_outputs), str(num_v), Marker_input])
        subprocess.run([python_path, os.path.join(full_path,"scripts","inference_fulltext_v5.py"), dir_in, dir_out, dir_train, dir_model, str(num_outputs), str(num_v), Marker_input])

# Display the Train tab
if selected_tab == "Train":
    st.markdown("## Train")
    dir_in = st.text_input("Enter the directory of the input folder:")
    dir_out = st.text_input("Enter the directory of the output folder:")
    dir_model = st.text_input("Enter the directory of the folder that has the models:")
    num_v = st.number_input("The version of the model (most recent: 1; 2 is the second most recent):", value=1)

    # Get the directory of the folder that has the models
    # dir_model = st.text_input("Enter the directory of the folder that has the models:")
    # dir_in  = st.file_uploader("Select a the input folder", type="directory")
    # dir_out = st.file_uploader("Select a the output folder", type="directory")
    # dir_model = st.file_uploader("Select the folder that has the models", type="directory")


    #dir_in=r"/Users/mayssamnaji/Desktop/train/input"
    #dir_out=r"/Users/mayssamnaji/Desktop/train/output"
    #dir_model= r"/Users/mayssamnaji/Desktop/train/model"
    num_v=num_v-1

    if st.button("Train"):
       subprocess.run([python_path, "scripts", os.path.join(full_path,"medidocs_training.py"), dir_in, dir_out, dir_model, str(num_v)])


# # Display the Cleaning tab
# if selected_tab == "Text Cleaning":
#     st.markdown("## Text Cleaning")
#     dir_in = st.file_uploader("Select a the input folder", type="directory")
#     dir_out = st.file_uploader("Select a the output folder", type="directory")
#     if st.button("Process"):
#         clean(dir_in, dir_out)



