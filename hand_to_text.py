import numpy

import easyocr
import cv2
import matplotlib.pyplot as plt

def handwriting_to_text(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the image
    plt.imshow(image)
    plt.axis('off')
    plt.show()

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Perform text detection
    result = reader.readtext(image_path)

    # Extract and print detected text
    extracted_text = '\n'.join([text[1] for text in result])
    print("Extracted Text:")
    print(extracted_text)

    return extracted_text

# Example usage
if __name__ == "__main__":
    image_path = "Chhabi 2.jpg"  # Replace with your image file path
    text = handwriting_to_text(image_path)