#!/usr/bin/env python3
# Copyright (c) Kevin-Tofu, koheitech001@gmail.com

import os
from typing import Optional, Union
import numpy as np
import cv2
# import set_audio
# from tools import set_audio
from coco_visualizer import tools


def create_converter_id2name(
    categories: list[dict]
):
    ret = dict()
    for cat in categories:
        ret[cat['id']] = cat['name']
    return ret


def draw_annotations_image(
    image: np.ndarray,
    annotations: list[dict],
    categories: Optional[Union[list[dict], dict]]=None
) -> np.ndarray:

    if categories is None:
        converter = lambda a : 'object'
    elif isinstance(categories,  list):
        converter = create_converter_id2name(categories)
    elif isinstance(categories,  dict):
        converter = categories

    img_ret = np.copy(image)
    # draw annotations on the image
    for ann in annotations:
        bbox = ann['bbox']
        category_id = ann['category_id']
        category_name = converter[ann['category_id']]
        score = ann['score'] if 'score' in ann.keys() else ''

        cv2.rectangle(img_ret, (int(bbox[0]), int(bbox[1])), (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), (0, 255, 0), 2)
        cv2.putText(img_ret, f"{category_name} - {score}", (int(bbox[0]), int(bbox[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return img_ret


def draw_annotations_video(
    fpath: str, 
    fpath_dst: str,
    coco: dict,
    categories: Optional[Union[list[dict], dict]]=None
):
    if categories is None:
        converter = lambda a : 'object'
    elif isinstance(categories,  list):
        converter = create_converter_id2name(categories)
    elif isinstance(categories,  dict):
        converter = categories
    
    cap = cv2.VideoCapture(fpath)
    k = cap.isOpened()
    if k == False:
        cap.open(fpath)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fpath_ex = os.path.splitext(fpath_dst)[-1]
    if fpath_ex == ".mp4" or fpath_ex == ".MP4":
        fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter(fpath_dst, fmt, fps, (width, height))


    imgid = 0
    while(1):

        ret, image = cap.read()
        if ret == False:
            break
        
        # coco['images'][imgid]
        anns = [c for c in coco['annotations'] if c['image_id'] == imgid]
        image_visualize = draw_annotations_image(
            image, 
            anns, 
            converter
        )
        # image_visualize = cv2.cvtColor(image_visualize, cv2.COLOR_RGB2BGR)
        writer.write(image_visualize)
        imgid += 1

    cap.release()
    writer.release()

    tools.set_audio(fpath, fpath_dst)