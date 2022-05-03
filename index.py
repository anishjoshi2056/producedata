import camelot

# PDF file to extract tables from
file1 = "realdata.pdf"
file2 = "realdata2.pdf"
# extract all the tables in the PDF file
tables1 = camelot.read_pdf(file1)
tables2 = camelot.read_pdf(file2)
# number of tables extracted
print("Total tables extracted:", tables1.n)
# export individually as CSV
tables1[0].to_csv("realdata.csv")
tables2[0].to_csv("realdata1.csv")