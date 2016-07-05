# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 15:27:33 2014

@author: olgis

PDF to PNG with GhostScript
"""

import subprocess
import os
import traceback
import sys
import glob

# Absolute path to Ghostscript executable here or
# command name if Ghostscript is in your PATH.
GHOSTSCRIPTCMD = "gs"


def main():
    pdf_path = sys.argv[1]
    pdf_list = glob.glob(pdf_path + "/*.pdf")
    #pdf_list[0]
    for item in xrange(len(pdf_list)):

        gs_pdf_to_png(pdf_list[item], "600")


def gs_pdf_to_png(pdffilepath, resolution):
    if not os.path.isfile(pdffilepath):
        print "'%s' is not a file. Skip." % pdffilepath

    pdfname, ext = os.path.splitext(pdffilepath)


    try:
        # For other commandline options see
        # http://ghostscript.com/doc/current/Use.htm#Options
        arglist = [GHOSTSCRIPTCMD,
                   "-dSAFER",
                   "-dBATCH",
                   "-dNOPAUSE",
                   "-sOutputFile=%s.png" % pdfname,
                   "-sDEVICE=pnggray",
                   "-dTextAlphaBits=4"
                   "-r%s" % resolution,
                   pdffilepath]
        print "Running command:\n%s" % ' '.join(arglist)
        subprocess.Popen(args=arglist, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    except OSError:
        sys.exit("Error executing Ghostscript ('%s'). Is it in your PATH?"
                 % GHOSTSCRIPTCMD)
    except:
        print "Error while running Ghostscript subprocess. Traceback:"
        print "Traceback:\n%s" % traceback.format_exc()

#    stdout, stderr = sp.communicate()
#    print "Ghostscript stdout:\n'%s'" % stdout
#    if stderr:
#        print "Ghostscript stderr:\n'%s'" % stderr

if __name__ == "__main__":
    main()
