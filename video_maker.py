
import subprocess
from pathlib import Path

Path("output").mkdir(exist_ok=True)

command = [
    "ffmpeg", "-y",
    "-f", "lavfi",
    "-i", "color=c=0x087E76:s=720x1280:r=30:d=25",
    "-f", "lavfi",
    "-i", "anullsrc=r=44100:cl=stereo",
    "-vf",
    "drawtext=text='PARADISEPARS':"
    "fontcolor=white:fontsize=65:"
    "x=(w-text_w)/2:y=(h-text_h)/2",
    "-t", "25",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    "output/paradisepars_test.mp4"
]

subprocess.run(command, check=True)
print("Video created successfully!")
