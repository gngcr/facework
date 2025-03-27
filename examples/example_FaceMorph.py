# Example usage for FaceMorph

from facework import FaceMorph
import cv2
import time
import sys
import numpy as np

# Optional: Print full NumPy arrays if needed for debugging
np.set_printoptions(threshold=sys.maxsize)

# --- Load the Two Face Images ---

# It's recommended that img_1 is high quality and taken from a frontal angle

# Image 1
path_1 = r'examples/AAA000healthy_james_blu_LE.jpg'
img_1 = cv2.imread(path_1)

# Image 2
path_2 = r'examples/AAA000healthy_jessi_gray_LE.jpg'
img_2 = cv2.imread(path_2)

# --- Generate Morphing Frames ---

# Initialize FaceMorph with the two images
FM = FaceMorph(img_1, img_2)

start = time.time()

# Create 5 morphing frames (equally spaced transition between faces)
# Optionally save the output frames in a folder (must exist)
frames = FM.make_frames(5, out_name=r'examples/examples/frames')

# Show each frame using internal show method
for frame in frames:
    FM.FC.show(frame)

end = time.time()
print("Elapsed time (frames only):", end - start, "seconds")

# --- Generate Morphing Video ---

start = time.time()

# Re-initialize FaceMorph if needed
FM = FaceMorph(img_1, img_2)

# Create a morphing video
# Parameters:
# - output folder must exist (e.g. 'examples/examples/morph_video')
# - fps: frames per second
# - seconds: total duration of the video
# - with_reverse=True: also creates a reversed version (from face 2 to face 1)

FM.make_morph_video(
    r'examples/examples/morph_video',
    with_reverse=True,
    fps=10,
    seconds=10
)

end = time.time()
print("Elapsed time (video generation):", end - start, "seconds")

# --- Notes on Codecs ---

# By default, the codec used is 'mpeg4', which avoids licensing issues. Being an older codec mpeg4 migth not be compatible with all video players.

# You *can* specify other codecs supported by FFmpeg. For example:
# FM.make_morph_video(codec='libx264') which is the de-facto standard today for mp4 videos.

# ⚠️ IMPORTANT: The use of 'libx264' codec (common for MP4 videos) is covered under the GPLv2+ license.
# It may not be legally compatible with all software, especially in commercial contexts.
# This project does not use or take responsibility for 'libx264' usage.

