import os

def rename_images(directory_path, prefix):
    file_extension = ".jpg"
    file_list = sorted([f for f in os.listdir(directory_path) if f.endswith(file_extension)])
    num_images = len(file_list)
    num_digits = len(str(num_images))
    
    for index, filename in enumerate(file_list, start=1):
        new_filename = f"{prefix}_{index:04d}{file_extension}"
        old_filepath = os.path.join(directory_path, filename)
        new_filepath = os.path.join(directory_path, new_filename)

        os.rename(old_filepath, new_filepath)
        print(f"Renamed {filename} to {new_filename}")

def main():
    directory_path = "Nerissa"  # Replace with the directory containing the images
    prefix = "Nerissa"  # Replace with the desired prefix for the filenames
    rename_images(directory_path, prefix)

if __name__ == "__main__":
    main()
