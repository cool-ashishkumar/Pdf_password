import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter


def upload_image_and_encrypt():
    # Select an image file using a file dialog
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )

    if image_path:
        # print(f"Image selected: {image_path}")

        # Open the image using Pillow
        image = Image.open(image_path)

        # Convert the image to RGB mode if not already
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Save the image as a PDF
        pdf_path = "photo.pdf"
        image.save(pdf_path, "PDF")
        print(f"Image successfully converted to PDF: {pdf_path}")

        # Ask the user for a password
        password = input("Enter a password for the encrypted PDF: ").strip()

        # Encrypt the generated PDF
        encrypt_pdf(pdf_path, password)
    else:
        print("No image selected")


def encrypt_pdf(input_pdf, password):
    # Read the PDF file
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Add pages from the reader to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Set encryption
    writer.encrypt(password)

    # Save the encrypted PDF
    encrypted_pdf_path = input("What do you want to write name of your pdf: ")
    with open(encrypted_pdf_path, "wb") as encrypted_file:
        writer.write(encrypted_file)

    print(f"PDF successfully encrypted with password: {encrypted_pdf_path}")


upload_image_and_encrypt()
