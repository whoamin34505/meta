from exif import Image
from datetime import datetime

def update_exif_datetime(image_path, output_path):
    with open(image_path, "rb") as file:
        img = Image(file)
    
    if not img.has_exif:
        print("The photo does not contain EXIF data. Creating new ones.")
        img.has_exif = True
    
    now = datetime.now()
    formatted_date = now.strftime("%Y:%m:%d %H:%M:%S")
    
    img.datetime_original = formatted_date
    img.datetime_digitized = formatted_date
    img.datetime = formatted_date
    
    with open(output_path, "wb") as new_file:
        new_file.write(img.get_file())

input_image = "D:/DCIM/182___01/IMG_3227.JPG"
output_image = "D:/DCIM/182___01/IMG_3227_updated.JPG"

update_exif_datetime(input_image, output_image)
print("The date and time in EXIF have been updated!")