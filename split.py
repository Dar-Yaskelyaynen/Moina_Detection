"""Для уставновки модулей  pip install module_name"""

import cv2
import numpy as np
import json
import os
from matplotlib import pyplot as plt

"""json с разметкой переменуем в annotation.json"""

json_list = {}
with open('annotation.json', 'r') as inp:
    json_list = json.load(inp)

"""Предполагается, что все видосы находятся в папке videos/

Лейблы в папке labels \
Изображения в images теперь в другой папке pictures \
"""

count = 0

for dirpath, dirnames, filenames in os.walk('videos/'):
    for json_dict in json_list:
        fn = json_dict['file_upload'].split('-')
        sequence = json_dict['annotations'][0]['result'][0]['value']['sequence']
        print(sequence)
        current_idx = 0
        fn = '-'.join(fn[1:])

        cap = cv2.VideoCapture(f'{dirpath}/{fn}')

        # count fps
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if (cap.isOpened() == False):
            print("Error opening video stream or file")
        else:
            # Read until video is completed
            current_frame_idx = 0
            while(cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()

                if current_frame_idx == sequence[current_idx]['frame']:
                    d = sequence[current_idx]
                    # we have only single class, so label is always 0
                    y_shape, x_shape, _= frame.shape
                    with open(f'labels/{count}.txt', 'w') as outp:
                        outp.write(f"{0} {d['x']*x_shape*0.01} {d['y']*y_shape*0.01} {d['width']*x_shape*0.01} {d['height']*y_shape*0.01}")
                    # self.check
                    # x = int(d['x']*0.01 * x_shape)
                    # y = int(d['y']*0.01 * y_shape)
                    # w = int(d['width']*0.01 * x_shape)
                    # h = int(d['height']*0.01 * y_shape)
                    # cv2.rectangle(frame, (x, y, w, h), (255, 0, 0), 10)
                    # plt.imshow(frame)

                    # write image
                    cv2.imwrite(f'pictures/{count}.jpg', frame)
                    current_idx += 1
                    if len(sequence) == current_idx:
                        break
                    count += 1

                current_frame_idx += 1

