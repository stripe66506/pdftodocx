#Simple script to convert PDF to DOCX Format

# How to use when PDF is in same foler as script
#
# from pdf2docx import parse
#
# pdf_file = 'EPS52.pdf'
# docx_file = 'Economic_Problems.docx' (Output file will be in same directory as pdf)
# 
# parse(pdf_file,docx_file)

# How to use when when PDF is in different directory from script
#
# from pdf2docx import parse
#
# pdf_file = 'C:\PDFtoDOCX\EPS52.pdf'
# docx_file = 'C:\PDFtoDOCX\Economic_Problems.docx' (output file will be created at this location)
#
# parse(pdf_file,docx_file)

#import parse from pdf2docx

from pdf2docx import parse

pdf_file = '<insert file name\location>'
docx_file = '<insert desired file name\location>'

# convert pdf tp docx

parse(pdf_file,docx_file)