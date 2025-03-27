# Example usage for FaceCrop

import cv2
import matplotlib.pyplot as plt
from facework import FaceCrop

# Initialize the FaceCrop class
proc = FaceCrop()

# --- Load Image ---
# Option 1: Provide the image path directly
image_path = r"examples/AAA000healthy_james_blu_LE.jpg"

# Option 2: Load the image using OpenCV
image = cv2.imread(image_path)

# Display the original image using FaceCrop's internal viewer
proc.show(image)

# Load the image into the class (must be a list, even for one image)
proc.load_images(images=[image])

# --- Landmark & Silhouette Info ---

# Facial landmarks detected by MediaPipe
print("Landmark list (raw):", proc.image_landmark_list)

# Normalized landmarks (scaled to image size)
print("Normalized landmarks:", proc.nomralized_landmarks)

# Silhouette points of the face
print("Silhouette points:", proc.image_silhouette_list)

# --- Step 1: Center Faces ---

# Focus the image on the face area
focused_faces = proc.center_faces()

# Display the centered faces
for face in focused_faces:
    proc.show(face)

# Optionally, use focused_faces as new input
# proc.load_images(images=focused_faces)

# --- Step 2: Generate Face Masks ---

# Generate cropping masks (returns list of PIL images)
# and optionally save the masks to a folder (folder must exist)
masks = proc.generate_mask(r'examples/examples/final_mask')

# Display the masks
for mask in masks:
    mask.show()




# --- Step 3: Crop Faces ---

# Crop faces using the generated masks
cropped_faces = proc.crop_face()

# Display cropped results
for face in cropped_faces:
    face.show()

# Alternatively: apply a specific mask to all images
# (load mask with PIL before using)
cropped_faces = proc.crop_face(masks[0])

# Display results from the custom mask
for face in cropped_faces:
    face.show()
