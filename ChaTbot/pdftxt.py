import PyPDF2
import shutil
import os
 
#create file object variable
#opening method will be rb
 
#create reader variable that will read the pdffileobj

pdffile = r"C:\Users\euddbha\OneDrive - Ericsson\Desktop\ChaTbot\insurances_pdf\1.pdf"
textfile = r"C:\Users\euddbha\OneDrive - Ericsson\Desktop\ChaTbot\output\1.txt"

if os.listdir(os.path.dirname(textfile)):
    shutil.rmtree(os.path.dirname(textfile))

os.mkdir(os.path.dirname(textfile))

pdfreader=PyPDF2.PdfFileReader(pdffile)
 
#This will store the number of pages of this pdf file
x=pdfreader.numPages
 
#create a variable that will select the selected number of pages
for i in range(x):
    pageobj=pdfreader.getPage(i)
    text=pageobj.extractText()
    print(text)
     
    #save the extracted data from pdf to a txt file
    #we will use file handling here
    #dont forget to put r before you put the file path
    #go to the file location copy the path by right clicking on the file
    #click properties and copy the location path and paste it here.

    with open(textfile, 'a') as f:
        f.writelines(text)
