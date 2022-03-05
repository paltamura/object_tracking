from PIL import Image
from subprocess import Popen, PIPE
import cv2

def main():
    # Config
    data_path = 'data-io/'
    input_path = data_path + 'input/input.mkv'
    output_path = data_path + 'output/output.mkv'
    
    br_int = 3000
    fps = 24
    video = cv2.VideoCapture(input_path)

    br_string = str(br_int) + "k"

    p = Popen(['ffmpeg', 
               '-y', 
               '-f', 
               'image2pipe', 
               '-vcodec', 'mjpeg', 
               '-r', str(fps), 
               '-i', '-', 
               '-vcodec', 'h264', 
               '-qscale', '5', 
               '-b', br_string,
               '-minrate', br_string,
               '-maxrate', br_string,
               output_path], stdin=PIPE)


    while True:
        exists, frame = video.read()
        if exists:
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