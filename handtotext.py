import cv2
import pytesseract
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Set Tesseract path (Windows users only)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """
    Preprocesses the image to improve OCR accuracy.

    Steps:
    - Convert to grayscale
    - Apply thresholding (adaptive or OTSU)
    - Remove noise
    """
    # Read the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply OTSU's thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Optional: Apply dilation & erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    processed_img = cv2.dilate(thresh, kernel, iterations=1)
    processed_img = cv2.erode(processed_img, kernel, iterations=1)

    return processed_img

def extract_handwritten_text(image_path):
    """
    Recognizes handwriting from an image using Tesseract OCR.
    """
    # Preprocess the image
    processed_img = preprocess_image(image_path)

    # Perform OCR using Tesseract
    extracted_text = pytesseract.image_to_string(processed_img, lang='eng')
    

    return extracted_text

def display_image(image_path):
    """
    Displays the given image using Matplotlib.
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    plt.imshow(image)
    plt.axis("off")
    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = "div.jpg"  # Replace with your handwriting image file
    display_image(image_path)
    text.txt = extract_handwritten_text(image_path)
    print("\nExtracted Text:")
    print(text.txt)
