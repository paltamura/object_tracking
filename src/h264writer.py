import sys
from PIL import Image
from subprocess import Popen, PIPE
import cv2

class H264Writer():
    def __init__(
        self, 
        output_file, 
        bitrate, 
        fps,
        vcodec, 
        compression_log_level):

        br_string = str(bitrate) + "k"
        self.p = Popen([
                'ffmpeg', 
                '-hide_banner',
                '-loglevel', compression_log_level,
                '-y', 
                '-f', 
                'image2pipe', 
                '-r', str(fps), 
                '-i', '-', 
                '-vcodec', vcodec, 
                '-qscale:v', '5', 
                '-b:v', br_string,
                '-bufsize', br_string,
                output_file], stdin=PIPE)

    def __enter__(self):
            return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.p.stdin.close()
        self.p.wait()

    def add_frame(self, frame):
        im = Image.fromarray(frame)
        im.save(self.p.stdin, 'JPEG')

