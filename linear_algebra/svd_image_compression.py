# Re-import required libraries after kernel reset
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import resize

# Load and preprocess an example grayscale image (camera)
image = color.rgb2gray(data.astronaut())  # convert to grayscale
image = resize(image, (100, 100), anti_aliasing=True)  # resize for simplicity

# Perform SVD
U, S, VT = np.linalg.svd(image, full_matrices=False)

# Reconstruct image using top k singular values
def reconstruct_image(k):
    return U[:, :k] @ np.diag(S[:k]) @ VT[:k, :]

# Create reconstructions with different k values
ks = [5, 20, 50, 100]
reconstructed_images = [reconstruct_image(k) for k in ks]

# Plot original and reconstructed images
fig, axes = plt.subplots(1, len(ks) + 1, figsize=(15, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off')

for ax, img, k in zip(axes[1:], reconstructed_images, ks):
    ax.imshow(img, cmap='gray')
    ax.set_title(f'k = {k}')
    ax.axis('off')

plt.tight_layout()
plt.show()
