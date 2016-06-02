# -*- coding: utf-8 -*-

# Basic exporter for svg icons

import cairo
import rsvg
import os.path
from os import listdir
from os.path import isfile, join

width, height = 16, 16

SVGS_PATH = 'svg/'


def export_all():
    if not os.path.isdir('out/'):
        os.makedirs('out/')

    file_names = [f for f in listdir(SVGS_PATH) if isfile(join(SVGS_PATH, f))]

    for file_name in file_names:
        # name without extensions
        name_only = file_name.replace('.svg', '')

        #img = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        #ctx = cairo.Context(img)

        icon_from_name = name_only
        out_icon_names = [name_only] # export to a png with the same file name
        rotations = []
        transforms = []

        # special cases
        if special_icons.has_key(name_only):
            special_icon = special_icons[name_only]
            if type(special_icon) is dict:
                if special_icon.has_key('output_names'):
                    out_icon_names += special_icon['output_names']

        svg_file_path = 'svg/%s.svg' % icon_from_name

        #handle = rsvg.Handle(svg_file_path)
        #handle.render_cairo(ctx)

        for index, out_icon_name in enumerate(out_icon_names):
            os.system('inkscape -z -f {input} -d {dpi} -e{output}'.format(
                input=svg_file_path,
                dpi=90,
                output='out/%s.png' % out_icon_name
            ))


# special cases for icons that will be exported to multiple target pngs or that require transforms.
special_icons = {
    'icon_add_track': dict( output_names=['icon_add'] ),
    'icon_new': dict( output_names=['icon_file'] ),
    'icon_animation_tree_player': dict( output_names=['icon_animation_tree'] ),
    'icon_tool_rotate': dict( output_names=['icon_reload'] ),
    'icon_folder': dict( output_names=['icon_load'] ),
    'icon_file_list': dict( output_names=['icon_enum'] ),
    'icon_collision_2d': dict( output_names=['icon_collision_polygon_2d', 'icon_polygon_2d'] ),
    'icon_class_list': dict( output_names=['icon_filesystem'] ),
    'icon_color_ramp': dict( output_names=['icon_graph_color_ramp'] ),
    'icon_translation': dict( output_names=['icon_p_hash_translation'] ),
    'icon_shader': dict( output_names=['icon_shader_material', 'icon_material_shader'] ),
    'icon_canvas_item_shader_graph': dict( output_names=['icon_material_shader_graph'] ),

}


export_all()
