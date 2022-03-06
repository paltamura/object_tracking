import sys
from PIL import Image
from subprocess import Popen, PIPE
import cv2

class H264Writer():
    def __init__(self, output_file, bitrate, fps):
        br_string = str(bitrate) + "k"
        self.p = Popen([
                'ffmpeg', 
                '-hide_banner',
                '-loglevel', 'quiet',
                '-y', 
                '-f', 
                'image2pipe', 
                '-r', str(fps), 
                '-i', '-', 
                '-vcodec', 'h264', 
                '-qscale:a', '5', # 5
                '-b:a', br_string,
                '-minrate', br_string,
                '-maxrate', br_string,
                # '-crf', '26',
                output_file], stdin=PIPE)

    def __enter__(self):
            return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.p.stdin.close()
        self.p.wait()

    def add_frame(self, frame):
        im = Image.fromarray(frame)
        im.save(self.p.stdin, 'JPEG')

# if __name__ == "__main__":
#     sys.stderr.write('Inicio... \n')
#     data_path = 'data-io/'
#     input_path = data_path + 'input/input.mkv'
#     output_path = data_path + 'output/output.mkv'
#     bitrate = 3000
#     fps = 24

#     video = cv2.VideoCapture(input_path)

#     with H264Writer(output_path, bitrate, fps) as h264Writer:
#         while True:
#             exists, cv2_frame = video.read()
#             if exists:
#                 frame = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2RGB)
#                 h264Writer.add_frame(frame)
#             else:
#                 break

#     video.release()
#     sys.stderr.write('Ok! \n')   
