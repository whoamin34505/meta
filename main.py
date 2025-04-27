from exif import Image
from datetime import datetime
from tkinter import filedialog
import os

def update_exif_datetime(image_path, output_path):
    with open(image_path, "rb") as file:
        img = Image(file)
                  
    now = datetime.now()
    formatted_date = now.strftime("%Y:%m:%d %H:%M:%S")
            
    img.datetime_original = formatted_date
    img.datetime_digitized = formatted_date
    img.datetime = formatted_date
  
    with open(output_path, "wb") as new_file:
        new_file.write(img.get_file())

def main():
    print("Select a folder with photos.")
    os.system("PAUSE")

    dir_path = filedialog.askdirectory()
    if not dir_path:
        print("No folder selected. Exiting.")
        return
    
    dir_path = os.path.normpath(dir_path).replace("\\", "/")
    
    output_dir = os.path.join(dir_path, "new")
    os.makedirs(output_dir, exist_ok=True)

    file_paths = []
    for file in os.scandir(dir_path):
        if file.is_file() and not file.name.startswith("."):
            input_path = os.path.join(dir_path, file.name).replace("\\", "/")
            file_paths.append(input_path)
    
    success_count = 0
    for input_path in file_paths:
        name, ext = os.path.splitext(os.path.basename(input_path))
        output_path = os.path.join(output_dir, f"{name}_updated{ext}").replace("\\", "/")
        
        print(f"\nProcess: {os.path.basename(input_path)}")
        update_exif_datetime(input_path, output_path)
        print(f"Successfully saved to: {os.path.basename(output_path)}")
        success_count += 1


    print(f"\nComplete! Successfully for {success_count} files.")

if __name__ == "__main__":
    main()