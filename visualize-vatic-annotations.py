import sys
import os
import json
import Tkinter as tk
import tkFont


if len(sys.argv) == 2:
    vatic_annotation_file = sys.argv[1]
    vatic_video_frames_dir = sys.argv[2]
else:
    vatic_annotation_file = '/home/rajeevv/data/vatic-data/shelf_video_20_mar/dummy_shelf_at_ripl_3.json'
    vatic_video_frames_dir = '/home/rajeevv/data/vatic-data/shelf_video_20_mar/shelf_video_1080_landscape/0/'

vatic_annotation_json_data = json.load(open(vatic_annotation_file))

video_frames = {}
for walk_tuple in os.walk(vatic_video_frames_dir):
    path,list_of_dir,list_of_files = walk_tuple
    for video_frame in list_of_files:
        video_frames[video_frame.split(".")[0]]=path+os.path.sep+video_frame



