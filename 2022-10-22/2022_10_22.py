# Import text from PDF files 

import PyPDF2
import sys

# Get all the PDF filenames.
pdfFiles = ["LIST OF PDF FILES"] # You can add your own PDF files here

for filename in sys.argv[1:]:
    pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # Loop through all the pages (except the first) and add them. You can also add the first page if you want by changing the range to range(1, pdfReader.numPages).
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
# Save the resulting PDF to a file.

pdfOutput = open('nameyourpdf.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
