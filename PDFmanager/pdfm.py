import PyPDF2
import sys

def run():
    try:
        if (sys.argv[1] == "merge"):
            if (len(sys.argv) < 4):
                usage()
            else:
                merge(sys.argv[2], sys.argv[3])
        elif (sys.argv[1] == "split"):
            if (len(sys.argv) < 5):
                usage()
            else:
                split(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    except Exception:
        usage()

    return

def usage():
    print("Python PDF Manager Script")
    print("Create a subsection of a PDF file by specifying start/end page number:\n\n")
    print("$ python pdfm.py split <filename> <start page> <end page>\n\n")
    print("Merge two PDF files together:\n\n")
    print("$ python pdfm.py merge <filename1> <filename2>\n\n")
    return

def merge(filename1, filename2):

    try:
        pdf1 = open(filename1, "rb")
        pdf2 = open(filename2, "rb")

        pdf1reader = PyPDF2.PdfFileReader(pdf1)
        pdf2reader = PyPDF2.PdfFileReader(pdf2) 

        pdfWriter = PyPDF2.PdfFileWriter()

        for pageNum in range(pdf1reader.numPages):
            pageObj = pdf1reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
        for pageNum in range(pdf2reader.numPages):
            pageObj = pdf2reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        combinedPdf = open("merged.pdf", "wb")
        pdfWriter.write(combinedPdf)
        combinedPdf.close()
        pdf1.close()
        pdf2.close()
    except IOError:
        print("Something was wrong")

def split(filename, start, end):
    try:
        pdf = open(filename, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdf)
        pdfWriter = PyPDF2.PdfFileWriter()

        if (end > pdfReader.numPages - 1):
            return

        for pageNum in range(end):
            if (pageNum >= start):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

        splitPdf = open("split-" + filename + ".pdf", "wb")
        pdfWriter.write(splitPdf)
        splitPdf.close()
        pdf.close()
        
    except IOError:
        print("Something was wrong")

if __name__ == "__main__":
    run()
