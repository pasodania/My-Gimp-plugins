from gimpfu import *

def python_glowEffect(img, drawable,
        outer_light_color, outer_grow_radius, outer_feather_radius,
        outer_layer_opacity,
        inner_light_color, inner_shrink_radius, inner_feather_radius,
        inner_layer_opacity
        ):
    # timg.disable_undo()
    img.undo_group_start()

    pdb.gimp_selection_none(img)

    baseLayer = img.active_layer

    fg_color = pdb.gimp_context_get_foreground()
    bg_color = pdb.gimp_context_get_background()
    pdb.gimp_context_set_background(outer_light_color)
    pdb.gimp_context_set_foreground(inner_light_color)

    baseLayer.lock_alpha=True
    pdb.gimp_edit_fill(baseLayer, BACKGROUND_FILL)
    baseLayer.lock_alpha=False
    baseLayer.remove_mask(MASK_APPLY)

    outerLayer = img.active_layer.copy()
    innerLayer = img.active_layer.copy()
    img.add_layer(outerLayer)
    img.add_layer(innerLayer)

    outerLayer.resize_to_image_size()
    pdb.gimp_selection_layer_alpha(outerLayer)
    pdb.gimp_edit_clear(outerLayer)
    pdb.gimp_selection_grow(img, outer_grow_radius)
    pdb.gimp_selection_feather(img, outer_feather_radius)
    pdb.gimp_edit_fill(outerLayer, BACKGROUND_FILL)
    pdb.gimp_selection_none(img)
    pdb.gimp_layer_set_opacity(outerLayer, outer_layer_opacity)
    pdb.gimp_layer_set_mode(outerLayer, SCREEN_MODE)

    innerLayer.resize_to_image_size()
    pdb.gimp_selection_layer_alpha(innerLayer)
    pdb.gimp_edit_clear(outerLayer)
    pdb.gimp_selection_shrink(img, inner_shrink_radius)
    pdb.gimp_selection_feather(img, inner_feather_radius)
    pdb.gimp_edit_fill(innerLayer, FOREGROUND_FILL)
    pdb.gimp_selection_none(img)
    pdb.gimp_layer_set_opacity(innerLayer, inner_layer_opacity)

    pdb.gimp_context_set_foreground(fg_color)
    pdb.gimp_context_set_background(bg_color)

    img.undo_group_end()
    #img.enable_undo()

register(
        "python-fu-glowEffect",
        "Apply Glow Effect to the layer",
        "Glow Effect",
        "ycums <youcharmanums._{at}_.gmail.com>",
        "ycums",
        "2008",
        "<Image>/Layer/_Glow Effect...",
        "RGB*, GRAY*, INDEXED",
        [ 
            (PF_COLOR, "outer_light_color", 
                "Outer light color", (255, 0, 255)),
            (PF_ADJUSTMENT, "outer_grow_radius",
                "Outer grow radius (in pixel)", 
                10, (0, 1024, 1)),
            (PF_ADJUSTMENT, "outer_feather_radius",
                "Outer feather radius", 40, (0, 255, 1)),
            (PF_ADJUSTMENT, "outer_layer_opacity",
                "Outer layer opacity", 70, (0, 100, 1)),

            (PF_COLOR, "inner_light_color", 
                "Inner light color", (255, 255, 255)),
            (PF_ADJUSTMENT, "inner_shrink_radius",
                "Inner shrink radius (in pixel)", 
                1, (0, 1024, 1)),
            (PF_ADJUSTMENT, "inner_feather_radius",
                "Inner feather radius", 5, (0, 255, 1)),
            (PF_ADJUSTMENT, "inner_layer_opacity",
                "Inner layer opacity", 100, (0, 100, 1)),
            ],
        [],
        python_glowEffect)
main()
