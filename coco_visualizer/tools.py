

from typing import Optional

def video_conversion(
    path_file_src: str, \
    path_file_dst: str, \
    test: Optional[int]=None
):
    
    import ffmpeg

    if test is None:
        stream = ffmpeg.input(path_file_src, v="quiet")
        stream = ffmpeg.output(stream, path_file_dst, v="quiet")
    else:
        stream = ffmpeg.input(path_file_src)
        stream = ffmpeg.output(stream, path_file_dst)
    ffmpeg.run(stream)


def set_audio(
    path_src: str, 
    path_dst: str
):
    """
    https://kp-ft.com/684
    https://stackoverflow.com/questions/46864915/python-add-audio-to-video-opencv
    """

    import os, shutil
    import moviepy.editor as mp
    import time

    root_ext_pair = os.path.splitext(path_src)
    path_dst_copy = f"{root_ext_pair[0]}-copy{root_ext_pair[1]}"
    shutil.copyfile(path_dst, path_dst_copy)
    time.sleep(0.5)

    # Extract audio from input video.                                                                     
    clip_input = mp.VideoFileClip(path_src)
    # clip_input.audio.write_audiofile(path_audio)
    # Add audio to output video.                                                                          
    clip = mp.VideoFileClip(path_dst_copy)
    clip.audio = clip_input.audio

    time.sleep(0.5)
    clip.write_videofile(path_dst)

    time.sleep(0.5)
    os.remove(path_dst_copy)