import os
import shutil
from datetime import datetime
import docx

successful_projects = []
date = datetime.today().strftime('%Y-%m-%d')


sig_image_folder = {
    'C': 'compsoc',
    'D': 'diode',
    'P': 'piston',
    'I': 'intersig'
}


def read_md_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

            return lines
    except Exception as e:
        print(f"Error in reading {file_path}: {e}")
        return None
    
def read_docx_file(file_path):
    try:
        doc = docx.Document(file_path)
        lines = []
        for para in doc.paragraphs:
            lines.append(para.text + "\n")
        
        return lines
    except Exception as e:
        print(f"Error in reading {file_path}: {e}")
        return None

def write_md_file(file_path, lines):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Error in writing to {file_path}: {e}")

def process_image_line(sig, folder, lines, flag, i, new_md_title, file):
    # Extract the image section from the line
    line = lines[i]
    image_section = line.split("!")[1].split(")")[0]
    # Get the old image name
    old_image_name = image_section.split("(")[-1].split(")")[0]

    image_name = image_section.split("(")[-1].split(")")[0]
    # If the image name is a link
    if image_name.startswith("http"):
        return
    # Split at / if it exists
    if "/" in image_name:
        image_name = image_name.split("/")[-1]
    
    # Get the image extension
    image_extension = image_name.split(".")[-1].strip()
    # Get the image path
    if flag == 1:
        image_path = f"Project Expo/{folder}/images/{image_name}"
    elif flag == 2:
        image_path = f"Project Expo/{folder}/Images/{image_name}"
    else:
        image_path = f"Project Expo/{folder}/{image_name}"

    image_name_with_hyphen = image_name
    # If image has a space in its name
    if " " in image_name:
        # Replace space with hyphen
        image_name_with_hyphen = image_name.replace(" ", "-")
        # Rename the image
        try: 
            if flag == 1:
                image_path = f"Project Expo/{folder}/images/{image_name}"
                os.rename(image_path, f"Project Expo/{folder}/images/{image_name_with_hyphen}")
                image_path = f"Project Expo/{folder}/images/{image_name_with_hyphen}"
            elif flag == 2:
                image_path = f"Project Expo/{folder}/Images/{image_name}"
                os.rename(image_path, f"Project Expo/{folder}/Images/{image_name_with_hyphen}")
                image_path = f"Project Expo/{folder}/Images/{image_name_with_hyphen}"
            else:
                image_path = f"Project Expo/{folder}/{image_name}"
                os.rename(image_path, f"Project Expo/{folder}/{image_name_with_hyphen}")
                image_path = f"Project Expo/{folder}/{image_name_with_hyphen}"
        except:
            try:
                just_image_name = image_name.split(".")[0]
                if image_extension == "png":
                    try: 
                        image_path.replace(image_name, f"{just_image_name}.jpg")
                        if flag == 1:
                            os.rename(image_path, f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpg")
                            image_path = f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpg"
                        elif flag == 2:
                            os.rename(image_path, f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpg")
                            image_path = f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpg"
                        else:
                            os.rename(image_path, f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpg")
                            image_path = f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpg"
                    except:
                        image_path.replace(image_name, f"{just_image_name}.jpeg")
                        if flag == 1:
                            os.rename(image_path, f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpeg")
                            image_path = f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpeg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpeg"
                        elif flag == 2:
                            os.rename(image_path, f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpeg")
                            image_path = f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpeg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpeg"
                        else:
                            os.rename(image_path, f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpeg")
                            image_path = f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpeg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpeg"
                elif image_extension == "jpg":
                    try: 
                        image_path.replace(image_name, f"{just_image_name}.png")
                        if flag == 1:
                            os.rename(image_path, f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.png")
                            image_path = f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.png"
                            image_name = f"{just_image_name.replace(' ', '-')}.png"
                        elif flag == 2:
                            os.rename(image_path, f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.png")
                            image_path = f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.png"
                            image_name = f"{just_image_name.replace(' ', '-')}.png"
                        else:
                            os.rename(image_path, f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.png")
                            image_path = f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.png"
                            image_name = f"{just_image_name.replace(' ', '-')}.png"
                    except:
                        image_path.replace(image_name, f"{just_image_name}.jpeg")
                        if flag == 1:
                            os.rename(image_path, f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpeg")
                            image_path = f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpeg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpeg"
                        elif flag == 2:
                            os.rename(image_path, f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpeg")
                            image_path = f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpeg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpeg"
                        else:
                            os.rename(image_path, f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpeg")
                            image_path = f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpeg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpeg"
                elif image_extension == "jpeg":
                    try:
                        image_path.replace(image_name, f"{just_image_name}.png")
                        if flag == 1:
                            os.rename(image_path, f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.png")
                            image_path = f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.png"
                            image_name = f"{just_image_name.replace(' ', '-')}.png"
                        elif flag == 2:
                            os.rename(image_path, f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.png")
                            image_path = f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.png"
                            image_name = f"{just_image_name.replace(' ', '-')}.png"
                        else:
                            os.rename(image_path, f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.png")
                            image_path = f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.png"
                            image_name = f"{just_image_name.replace(' ', '-')}.png"
                    except:
                        image_path.replace(image_name, f"{just_image_name}.jpg")
                        if flag == 1:
                            os.rename(image_path, f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpg")
                            image_path = f"Project Expo/{folder}/images/{just_image_name.replace(' ', '-')}.jpg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpg"
                        elif flag == 2:
                            os.rename(image_path, f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpg")
                            image_path = f"Project Expo/{folder}/Images/{just_image_name.replace(' ', '-')}.jpg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpg"
                        else:
                            os.rename(image_path, f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpg")
                            image_path = f"Project Expo/{folder}/{just_image_name.replace(' ', '-')}.jpg"
                            image_name = f"{just_image_name.replace(' ', '-')}.jpg"
            except:
                print(f"Error in renaming {image_name} file.")
                print("Project : ", folder)
                print("File : ", file)
                print("Image Path : ", image_path)
                print("Image Name : ", image_name)
                print("Image extension : ", image_extension)
                print("\n")
    
    # Update the image name within ()
    final_image_link = f"/virtual-expo/assets/img/envision/{sig_image_folder[sig]}/{new_md_title}/{image_name.replace(' ', '-')}"

    lines[i] = lines[i].replace(old_image_name, final_image_link)

    # Moving the images to the the corresponding folder in the assets folder
    if not os.path.exists(f"../assets/img/envision/{sig_image_folder[sig]}/{new_md_title}"):
        os.makedirs(f"../assets/img/envision/{sig_image_folder[sig]}/{new_md_title}")
    if not os.path.exists(f"../assets/img/envision/{sig_image_folder[sig]}/{new_md_title}/{image_name}"):
        try:
            shutil.copy(image_path, f"../assets/img/envision/{sig_image_folder[sig]}/{new_md_title}/{image_name}")
        except:
            print(f"Image {image_name} not found in {image_path} folder.")
            print("Project : ", folder)
            print("Image : ", image_name)
            print("Removing the image line from the file ...")
            lines.pop(i)
            print("Image line removed successfully.")
            print("\n")

def process_md_file(folder, file, flag):
    
    file_path = os.path.join("Project Expo", folder, file)
    if file.lower().endswith(".md"):
        lines = read_md_file(file_path)
    elif file.lower().endswith(".docx"):
        lines = read_docx_file(file_path)
    else:
        print(f"Error: {file} is not a .md or .docx file.")
        return
    if lines is None:
        return

    sig = folder[0]

    print(f"Project: {folder}")
    print(f"Successfully read {file} file.")
    successful_projects.append(folder)

    # remove beginning lines that are white spaces
    while lines[0] == "\n":
        lines.pop(0)
    
    # remove ending lines that are white spaces
    while lines[-1] == "\n":
        lines.pop(-1)

    is_thumbnail_present = False
    for i, line in enumerate(lines):
        # remove \ from the lines[i]
        line = line.replace("\\", "")
        lines[i] = line
        # Process the lines of the file
        if line.startswith("title:"):
            new_md_title = line.split(":", 1)[1].strip()
            # extract text between quotes
            try:
                new_md_title = new_md_title.split('"')[1]
            except:
                try:
                    new_md_title = new_md_title.split("'")[1]
                except:
                    pass
            # replace spaces with hyphens
            new_md_title = new_md_title.replace(" ", "-")
            # replace all uppercase letters with lowercase letters
            new_md_title = new_md_title.lower()
            # replace all special characters with hyphens
            new_md_title = new_md_title.replace("!", "-")
            new_md_title = new_md_title.replace("@", "-")
            new_md_title = new_md_title.replace("#", "-")
            new_md_title = new_md_title.replace("$", "-")
            new_md_title = new_md_title.replace("%", "-")
            new_md_title = new_md_title.replace("^", "-")
            new_md_title = new_md_title.replace(":", "-")

        if line.startswith("categories:"):
            # Update the categories line
            lines[i] = "categories: envision\n"
        
        if line.startswith("year:"):
            # Update the year line
            lines[i] = "year: 2023\n"

        if line.startswith("thumbnail:"):
            is_thumbnail_present = True
            # extract the image name
            image_name = line.split(":", 1)[1].strip()
            # extract text between quotes
            try:
                image_name = image_name.split('"')[1]
            except:
                try:
                    image_name = image_name.split("'")[1]
                except:
                    pass
            # if / is present in the image name
            if "/" in image_name:
                # extract the image name
                image_name = image_name.split("/")[-1]

            final_image_name = f"{date}-{new_md_title}-{image_name}"

            if flag == 1:
                # copy the thumbnail image to ../img/thumbnails folder
                try:
                    shutil.copy(f"Project Expo/{folder}/images/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                except:
                    try: 
                        shutil.copy(f"Project Expo/{folder}/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                    except:
                        print(f"No thumbnail image found for {folder} project.")
                        # Update the thumbnail line to placeholder-image.jpg
                        lines[i] = f"thumbnail: placeholder-image.jpg\n"
                        continue
            elif flag == 2:
                # copy the thumbnail image to ../img/thumbnails folder
                try:
                    shutil.copy(f"Project Expo/{folder}/Images/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                except:
                    try: 
                        shutil.copy(f"Project Expo/{folder}/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                    except:
                        print(f"No thumbnail image found for {folder} project.")
                        # Update the thumbnail line to placeholder-image.jpg
                        lines[i] = f"thumbnail: placeholder-image.jpg\n"
                        continue
            else:
                # copy the thumbnail image to ../img/thumbnails folder
                try:
                    shutil.copy(f"Project Expo/{folder}/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                except:
                    print(f"No thumbnail image found for {folder} project.")
                    # Update the thumbnail line to placeholder-image.jpg
                    lines[i] = f"thumbnail: placeholder-image.jpg\n"
                    continue

            # Update the thumbnail line
            lines[i] = f"thumbnail: {final_image_name}\n"
        
        if '![' in line:
            process_image_line(sig, folder, lines, flag, i, new_md_title, file)
    
    if not is_thumbnail_present:
        print(f"No thumbnail image found for {folder} project.")
        # Update the thumbnail line to placeholder-image.jpg
        lines.insert(5, f"thumbnail: placeholder-image.jpg\n")

    temp_md_file_path = os.path.join("temp", f"{date}-{new_md_title}.md")
    write_md_file(temp_md_file_path, lines)

def main():
    # Delete the temp folder if it exists
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    # Create the temp folder
    os.makedirs("temp")

    for folder in os.listdir("Project Expo"):
        if folder == '_Sample_Project_Code_':
            continue
        sig = folder[0]
        flag = 0

        # Check if images folder exists in Project Expo/{folder}
        if os.path.exists(os.path.join("Project Expo", folder, "images")):
            flag = 1
        elif os.path.exists(os.path.join("Project Expo", folder, "Images")):
            flag = 2
        else:
            flag = 0

        # Find the .md file in the folder
        for file in os.listdir(os.path.join("Project Expo", folder)):
            if file.lower().endswith(".md") or file.lower().endswith(".docx"):
                process_md_file(folder, file, flag)
                print("\n\n")
                break

if __name__ == "__main__":
    main()

