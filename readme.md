# NLPverse for Medidocx

We designed this app to help you easily clean and improve the quality of your raw docx documents. Upload the folder containing all your files and where you want to store the results. Our advanced processing algorithms will remove non-English characters, fix grammar mistakes, and paraphrase the content to ensure that the final version is clear, concise, and easy to read. The resulting document will retain the same context and meaning as the original but with a polished, professional finish.

## Things to keep in mind
- Ensure that the documents you upload are in .docx or .doc format
- The name of the file should start with the patient name and surname examples: name_surname...docx ; name, surname...docx ; or name-surname...docx
- While reviewing resulted documents to add to the training pipeline, please do not move paragraphs or add any line breaks

## Tasks
- Inference: Cleans and paraphrases the docs presented in the directory. It also highlights the patient names and highlights any new words not found in the original document
- Auto Inference: Runs inference very time there is a new file added to the folder  
- Train: Trains the model to learn your tone of writing

