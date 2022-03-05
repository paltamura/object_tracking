# import packages
from PIL import Image
from subprocess import Popen, PIPE
# from imutils.video import VideoStream
# from imutils.object_detection import non_max_suppression
# from imutils import paths
import cv2
import numpy as np
# import imutils

def main():
    # Config
    data_path = 'data-io/'
    input_path = data_path + 'input/input.mkv'
    output_path = data_path + 'output/output.mkv'

    # ffmpeg setup
    # p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'h264', '-qscale', '5', '-r', '24', output_path], stdin=PIPE)
    p = Popen(['ffmpeg', 
               '-y', 
               '-f', 
               'image2pipe', 
               '-vcodec', 'mjpeg', 
               '-r', '24', 
               '-i', '-', 
               '-vcodec', 'h264', 
               '-qscale', '5', 
               '-r', '24',
               '-b', '3000k',
               '-minrate', '3000k',
               '-maxrate', '3000k',
               output_path], stdin=PIPE)

    video = cv2.VideoCapture(input_path)

    while True:
        ret, frame = video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            im.save(p.stdin, 'JPEG')
        else:
            break

    p.stdin.close()
    p.wait()
    video.release()
    
if __name__ == "__main__":
    main()