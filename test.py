import json
import numpy as np
import cv2

import coco_formatter
import coco_visualizer

image = cv2.imread('./temp/EPSON014.jpg')
with open('./temp/instances.json', 'rb') as f:
    coco_image = json.load(f)

categories = coco_formatter.get_categories()
# print(categories)



img_anns = coco_visualizer.draw_annotations_image(
    image,
    coco_image['annotations'],
    categories
)

cv2.imwrite('./temp/test.jpg', img_anns)

with open('./temp/coco_video.json', 'rb') as f:
    coco_video = json.load(f)
coco_visualizer.draw_annotations_video(
    './temp/test_video.mp4',
    './temp/test_video-anns.mp4',
    coco_video,
    categories
)