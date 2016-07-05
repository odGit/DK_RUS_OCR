# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 15:07:07 2014
TODO: check for file type
TODO: check for number of arguments
TODO: create main file
@author: olgis
"""

from pyPdf import PdfFileWriter, PdfFileReader
import sys
import os
import copy


def get_file_name(any_file):
    """ MISSING DOC STRING"""
    file_name = any_file[:-4]  # stripping off .PDF

    return file_name


def dic_for_output(file_name):
    """ MISSING DOC STRING"""
    file_path = os.getcwd()  # current directory
    out_dir = file_path + "/" + file_name[:-4]  # name of dict for output
    print "Files will be saved to following directory: %s" % out_dir

#Checking if output dictory already exist, if not creats it
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    return out_dir


def pdf_info(pdf_file):
    #Checking how many pages in PDF file
    inputpdf = PdfFileReader(open(pdf_file, "rb"))
    num_pages = inputpdf.numPages
    print "File %s length is %s pages" % (pdf_file, num_pages+1)


def split_pdf(pdf_file, list_pages, coef=1.75):
    """ MISSING DOC STRING"""
    pdf_name = get_file_name(pdf_file)
    out_dir = dic_for_output(pdf_file)
    #Checking how many pages in PDF file
    inputpdf = PdfFileReader(open(pdf_file, "rb"))
    num_pages = inputpdf.numPages
    print "File %s length is %s pages" % (pdf_file, num_pages+1)
    print "Page will be splitted with %s ratio" % coef

    #Splitting page in two and saving both pages
    for i in list_pages:
        output = PdfFileWriter()
        print "Processing page %s out of %s pages" % (i, num_pages+1)
        current_page = inputpdf.getPage(i)
        current_copy = copy.copy(current_page)
# get y of Lower Left corner
        y = current_page.mediaBox.getLowerLeft_y()
# get y of Upper Right corner
        y2 = current_page.mediaBox.getUpperRight_y()
        t1 = float(current_page.mediaBox.getUpperRight_x()) / coef

        current_page.mediaBox.upperRight = (t1, y2)
        output.addPage(current_page)
        with open(os.path.join(out_dir, "%s_%s_left.pdf" % (pdf_name, i)),
                  "wb") as outputStream:
                    output.write(outputStream)

        output1 = PdfFileWriter()
        current_copy.mediaBox.lowerLeft = (t1, y)
        output1.addPage(current_copy)
        with open(os.path.join(out_dir, "%s_%s_right.pdf" % (pdf_name, i)),
                  "wb") as outputStream:
                    output1.write(outputStream)

        outputStream.close()

    print "Finish splitting the file "
    return 0


def main():
    arg_names = ['py_file', 'pdf_file', 'pages', 'coef']
    args = dict(zip(arg_names, sys.argv))

#Cheking how many pages to process
    line = args["pages"].translate(None, '[]')  # removing []
    if "-" in line:
        a = [x.strip() for x in line.split("-")]
        nk = [int(k) for k in a if k.isdigit()]
        pages = range(nk[0], nk[1])

    else:
        a = [x.strip() for x in line.split(",")]  # splitting with comma
        pages = [int(k) for k in a if k.isdigit()]

    print pages

    if "coef" in args:
        split_pdf(args["pdf_file"], pages, float(args["coef"]))
    else:
        split_pdf(args["pdf_file"], pages)


if __name__ == "__main__":
    main()
