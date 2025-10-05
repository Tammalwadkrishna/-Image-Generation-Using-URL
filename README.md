# 🖼️ Image Generation Using URL

This project demonstrates how to **load and display images directly from a URL** using Python. It also includes an example of converting a color image to **grayscale** for visualization using popular Python libraries such as `requests`, `PIL`, and `matplotlib`.

---

## 🚀 Features
- Load an image from an external URL.
- Display the original image using Matplotlib.
- Convert the image to grayscale.
- Display the grayscale version.

---

## 🧠 Concepts Covered
- Handling HTTP requests with the `requests` library.
- Working with image data using the `PIL` (Pillow) module.
- Visualizing images using `matplotlib.pyplot`.
- Basic image conversion and manipulation.

---

## 🛠️ Requirements

Make sure the following libraries are installed:

```bash
pip install numpy pandas matplotlib pillow requests
```

---

## 📂 Project Structure

```
IMG_GENRATION_USING_URL/
│
├── IMG_GENRATION_USING_URL.py    # Main Python script
└── README.md                     # Project documentation
```

---

## 📜 Code Overview

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
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
```

---

## 🖼️ Output Preview

### 🔹 Original Image
Displays the Iron Man image from the provided URL.

### 🔹 Grayscale Image
Displays the grayscale version of the same image.

---

## 📧 Author
**Krishna Tammalwad**  
Aspiring AI/ML Engineer | Data Analyst | Lifelong Learner  
💻 [GitHub Profile](https://github.com/krishna-tammalwad)
