import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO  # Used to hold image data in memory

def load_image_from_url(url):
    response = requests.get(url)  # Fixed typo here
    return Image.open(BytesIO(response.content))

iron_man_url = "https://tse1.mm.bing.net/th/id/OIP.LQZpQ_gRrC6l0LusvOGUwgHaJW?rs=1&pid=ImgDetMain&o=7&rm=3"

iron_man = load_image_from_url(iron_man_url)

# Display the original image
plt.figure(figsize=(10, 10))
plt.imshow(iron_man)
plt.title("Iron Man")
plt.axis("off")
plt.show()

# Grayscale image
iron_man_gray = iron_man.convert("L")

# Display the grayscale image
plt.figure(figsize=(10, 6))
plt.imshow(iron_man_gray, cmap="gray")
plt.title("Iron Man - Grayscale")
plt.axis("off")
plt.show()

