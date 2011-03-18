#!/usr/bin/env python
# Author: Chris Mohler
# Copyright 2009 Chris Mohler
# License: GPL v3
# Version 0.3
# GIMP plugin to export layers as PNGs

from gimpfu import *
import os

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)


def export_layers(img, drw, path, flatten=False):
	dupe = img.duplicate()
	for layer in dupe.layers:
		layer.visible = 0
	for layer in dupe.layers:
		layer.visible = 1
		name = layer.name + ".png"
		fullpath = os.path.join(path, name);
		tmp = dupe.duplicate()
		if (flatten):
			tmp.flatten()
		pdb.file_png_save(tmp, tmp.layers[0], fullpath, name, 0, 9, 1, 1, 1, 1, 1)
		dupe.remove_layer(layer)

	    
register(
    proc_name=("python-fu-export-layers"),
    blurb=("Export Layers as PNG"),
    help=("Export all layers as individual PNG files."),
    author=("Chris Mohler"),
    copyright=("Chris Mohler"),
    date=("2009"),
    label=("as _PNG"),
    imagetypes=("*"),
    params=[
	(PF_IMAGE, "img", "Image", None),
	(PF_DRAWABLE, "drw", "Drawable", None),
	(PF_DIRNAME, "path", "Save PNGs here", os.getcwd()),
	(PF_BOOL, "flatten", "Flatten Images?", False),
	   ],
    results=[],
    function=(export_layers), 
    menu=("<Image>/File/E_xport Layers"), 
    domain=("gimp20-python", gimp.locale_directory)
    )

main()
