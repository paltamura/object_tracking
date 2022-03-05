from PIL import Image
from subprocess import Popen, PIPE

# Config
data_path = 'data-io/'
input_path = data_path + 'input/input.mkv'
output_path = data_path + 'output/output.mkv'

fps, duration = 24, 100
p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'mpeg4', '-qscale', '5', '-r', '24', input_path], stdin=PIPE)
for i in range(fps * duration):
    im = Image.new("RGB", (300, 300), (i, 1, 1))
    im.save(p.stdin, 'JPEG')
p.stdin.close()
p.wait()