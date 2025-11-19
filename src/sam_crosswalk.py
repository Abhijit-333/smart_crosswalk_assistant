import torch
import cv2
import numpy as np
from segment_anything import sam_model_registry, SamPredictor

# Load SAM model
sam_checkpoint = "models/sam_vit_b_01ec64.pth"
model_type = "vit_b"

device = "cuda" if torch.cuda.is_available() else "cpu"
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
predictor = SamPredictor(sam)

# Load your crosswalk image
image_path = "data/test_crosswalk_1.jpeg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
predictor.set_image(image_rgb)

# Option 1: Predict all regions automatically
masks, scores, logits = predictor.predict(
    point_coords=None,
    point_labels=None,
    multimask_output=True,
)

# Pick the best mask
best_mask = masks[np.argmax(scores)]

# Overlay mask on original image
overlay = image.copy()
overlay[best_mask] = (0, 255, 0)  # highlight in green
result = cv2.addWeighted(image, 0.5, overlay, 0.5, 0)

cv2.imshow("SAM Crosswalk Segmentation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
