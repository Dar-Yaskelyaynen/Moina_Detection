import cv2
import numpy as np
import json
import os
from matplotlib import pyplot as plt


json_list = {}
with open('image_annotation.json', 'r') as inp:
    json_list = json.load(inp)

for dirpath, dirnames, filenames in os.walk('videos/'):
    for json_dict in json_list:
        fn = json_dict['file_upload'].split('-')
        fn = '-'.join(fn[1:]).replace('.jpg', '').replace('png', '')
        annotation_list = json_dict['annotations'][0]['result']
        with open(f'labels/{fn}.txt', 'w') as outp:
            for annotation in annotation_list:
                x_shape = annotation['original_width']
                y_shape = annotation['original_height']
                d = annotation['value']
                outp.write(f"{0} {d['x']*0.01} {d['y']*0.01} {d['width']*0.01} {d['height']*0.01}\n")
