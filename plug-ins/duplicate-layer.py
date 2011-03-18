#!/usr/bin/env python

from gimpfu import *

def python_duplicate_layer(img, layer):
  copy_layer = layer.copy()
  img.add_layer(copy_layer, -1)
  gimp.displays_flush()

register(
  "python-fu-duplicate-layer",
  "summary",
  "description",
  "name",
  "copyright",
  "date",
  "<Image>/Layer/Test/Duplicate Layer2",
  "RGB*",
  [],
  [],
  python_duplicate_layer)

main()
