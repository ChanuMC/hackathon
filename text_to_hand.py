import PIL
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import matplotlib.pyplot as plt
#import textract
#text = textract.process("SE ASS-1.docx")

def text_to_handwriting(text, output_path="handwriting.png", font_path="CedarvilleCursive-Regular.ttf", font_size=40):
    """
    Converts text into a handwritten-style image.

    Parameters:
    text (str): The text to be converted.
    output_path (str): File path to save the output image.
    font_path (str): Path to the handwriting-style TTF font file.
    font_size (int): Font size for the handwriting.
    """
    try:
        # Create a blank white image
        img = Image.new("RGB", (1500, 3000), "white")
        draw = ImageDraw.Draw(img)

        # Load the custom handwriting font
        font = ImageFont.truetype(font_path, font_size)

        # Write the text onto the image
        draw.text((50, 100), text, font=font, fill="black")

        # Save the image
        img.save(output_path)
        print(f"Handwritten text saved as {output_path}")

        # Display the image using Matplotlib
        img_cv = cv2.imread(output_path)
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

        plt.imshow(img_rgb)
        plt.axis("off")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    #f = open('SE ASS-1.docx', 'r')
    textInput = "Name : Chanaksh Choudhari\nRoll No:42\nBranch : 4th Sem AI\nSection : A\nSubject : Software Engineering\nTAE-1\nQ1. Explain Waterfall Model( Uses, architecture, advantages , disadvantages).\nANS:\nThe waterfall model is a linear and sequential software development model where each \nphase must be completed before moving to the next. It follows a top-down approach and is one of the\n earliest SDLC (Software Development Life Cycle) Models.\n1. Uses of the Waterfall Model :\nThe Waterfall Model is best suited for:\n*Small or well-defined projects with clear requirements.\n*projects with fixed scope and minimal expected changes.\n*Government and defense projects,where documentation is critical.\n*Healthcare , banking and embedded systems, where predictability is important.\n*Education and research projects , where phases are well- structured.\n\n2. Architecture of the Waterfall Model :\nThe Waterfall Model consists of six sequential phases:\nA ) Requirement gathering & Analysis - Understanding and documenting client needs.\nB ) System Design - Defining software arhitecture , components and database design.\nC ) Implementation ( coding ) - Writing code based on design specifications.\nD ) Testing - Checking for errors, bugs and functionality validation.\nE ) Deployment - Releasing the software to users.\nF ) Maintenance - Fixing bugs and providing updates after deployment.\n3. Advantages :\n* SImple and easy to understand\n*Clear Documentation\n* Better planning\n* Easy to manage\n4. Disadvantages :\n* Rigid and Inflexible\n* High Risk\n* Slow Delivery\n* Not Suitable for complex projects\n\nQ2. Explain Software Development Life Cycle ( S DL C )\nANS:\nS D L C (  Software Development Life Cycle ) is a structures process used to develop high-quality software systematically . It defines stages activities and deliverables required to build, test and deploy software efficiency.\n\nS D L C  consists of six main phases :\n1 ) Planning : \n* Define project scope, objectives , budget ad schedule.\n* Conduct feasibility studies.\n2 ) requirement Analysis : \n* Gather and document functional and non-functional requirements.\n* Identify system users and stakeholders . \n3 ) Design :\n* Create software architecture , database structure and U I design.\n* Define high - level design ( H L D ) and low - level design ( L L D ).\n4) Implementation (Coding): \n* Developers write code using programming languages.\n* Follow coding sytandards and best practices\n5 ) Testing :\n* Identify and fix bugs through unit testing integration testing, system testing and user acceptance testing ( U A T ).\n6 ) Deplayment and Maintenance : \n* Release software to users ( production environment )\n* Provide updates , bug fixes and enhancements .\n"
    text_to_handwriting(textInput, "output_handwritingword.png", "CedarvilleCursive-Regular.ttf", 30)
