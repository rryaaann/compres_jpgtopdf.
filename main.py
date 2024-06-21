import os
from tkinter import Tk, Label, Button, filedialog, messagebox, Scale, HORIZONTAL, Frame
from PIL import Image
from reportlab.pdfgen import canvas

class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Compressor")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')

        self.header_frame = Frame(self.root, bg='#4CAF50')
        self.header_frame.pack(fill='x')

        self.label = Label(self.header_frame, text="Image to PDF Compressor", font=("Helvetica", 18, 'bold'), bg='#4CAF50', fg='white')
        self.label.pack(pady=10)

        self.content_frame = Frame(self.root, bg='#f0f0f0')
        self.content_frame.pack(pady=20)

        self.upload_button = Button(self.content_frame, text="Upload Image", command=self.upload_image, font=("Helvetica", 12), bg='#008CBA', fg='white')
        self.upload_button.pack(pady=10)

        self.size_label = Label(self.content_frame, text="Select Compression Quality:", bg='#f0f0f0', font=("Helvetica", 12))
        self.size_label.pack(pady=5)

        self.quality_scale = Scale(self.content_frame, from_=10, to=100, orient=HORIZONTAL, label="Quality (10 = low, 100 = high)", bg='#f0f0f0', font=("Helvetica", 10))
        self.quality_scale.set(85)
        self.quality_scale.pack(pady=5)

        self.convert_button = Button(self.content_frame, text="Compress and Convert to PDF", command=self.compress_and_convert_to_pdf, state='disabled', font=("Helvetica", 12), bg='#4CAF50', fg='white')
        self.convert_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg *.jpeg")])
        if file_path:
            self.image_path = file_path
            self.convert_button.config(state='normal')
            messagebox.showinfo("Upload Sukses", "gambar berhasil di uplod ya gengs!")

    def compress_and_convert_to_pdf(self):
        quality = self.quality_scale.get()
        image = Image.open(self.image_path)
        
        # kompres gambar
        compressed_image_path = os.path.splitext(self.image_path)[0] + "_compressed.jpg"
        image.save(compressed_image_path, "JPEG", quality=quality)

        pdf_path = os.path.splitext(self.image_path)[0] + ".pdf"

        c = canvas.Canvas(pdf_path, pagesize=image.size)
        c.drawImage(compressed_image_path, 0, 0, *image.size)
        c.save()

        os.remove(compressed_image_path)  # bersih kan dari file kompres 

        messagebox.showinfo("kompresi sukses", f"pdf tersimpan ya gengs!\nLocation: {pdf_path}")


if __name__ == "__main__":
    root = Tk()
    app = ImageToPdfConverter(root)
    root.mainloop()
