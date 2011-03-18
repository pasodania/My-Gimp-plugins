#!/usr/bin/env python

from gimpfu import *

def python_pytest(img, layer):
    # Actual plug-in code will go here
    pdb.gimp_image_flip(img, ORIENTATION_VERTICAL)
    return


register(
    "python_fu_pytest",
    "Does something",
    "Does something terribly useful",
    "Your name",
    "Your name",
    "2009",
    "Py Test...",
    "*",
    [],
    [],
    python_pytest,
        menu="<Image>/Filters/Distorts")    

main()
