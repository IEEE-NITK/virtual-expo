import gdown
import os
import shutil
from datetime import datetime
import docx
import csv


meet_links_sheet = "https://docs.google.com/spreadsheets/d/1RbG9kE-ns88ksDqndV1xK5NQKGVPM-FtaA-I5ryDuu8/export?gid=1475908830&format=csv"

# Download the meet links sheet
# gdown.download(meet_links_sheet, "meet_links.csv", quiet=False)



# CODE TO REMOVE FOLDER AND ALL ITS CONTENTS: 

# if os.path.exists("Project Expo"):
#     # remove the folder and all its contents
#     shutil.rmtree("Project Expo")

# CODE TO DOWNLOAD FOLDER FROM GOOGLE DRIVE:

# envision_2023_reports = "https://drive.google.com/drive/u/1/folders/1z8Zt3ndLTTtYNyGlMyxB9L86GvQboiD5"
# gdown.download_folder(envision_2023_reports, quiet=False, use_cookies=False)

successful_projects = []

sig_order = ['C', 'D', 'P']

sig_image_folder = {
    'C': 'compsoc',
    'D': 'diode',
    'P': 'piston',
    'I': 'intersig'
}

for folder in os.listdir("Project Expo"):
    if folder == '_Sample_Project_Code_':
        continue
    sig = folder[0]
    flag = 0
    # Check if images folder exists in Project Expo/{folder}
    if os.path.exists(f"Project Expo/{folder}/images"):
        flag = 1
    elif os.path.exists(f"Project Expo/{folder}/Images"):
        flag = 2
    else:
        flag = 0

    date = ""
    new_md_title = ""
    # Find the .md file in the folder
    for file in os.listdir(f"Project Expo/{folder}"):
        if file.endswith(".md") or file.endswith(".MD") or file.endswith(".Md") or file.endswith(".mD") or file.endswith(".docx"):
            # If the file is a docx file
            if file.endswith(".docx"):
                doc = docx.Document(f"Project Expo/{folder}/{file}")
                lines = []
                for para in doc.paragraphs:
                    lines.append(para.text)
            # If the file is a md file
            else:
                f = open(f"Project Expo/{folder}/{file}", "r")
                # Read the file line by line
                try:
                    lines = f.readlines()
                except:
                    # If the file is a docx file (with .md extension)
                    try:
                        doc = docx.Document(f"Project Expo/{folder}/{file}")
                        lines = []
                        for para in doc.paragraphs:
                            lines.append(para.text)
                    except:
                        print(f"Error in reading {file} file.")
                        print("Project : ", folder)
                        print("File : ", file)
                        print("\n\n")
                        continue
                
                print(f"Project : {folder}")
                print(f"Successfully read {file} file.")
                successful_projects.append(folder)
                print("\n\n")

                for i, line in enumerate(lines):
                    date = datetime.today().strftime('%Y-%m-%d')
                    if line.startswith("title:"):
                        # Todays date in YYYY-MM-DD format
                        # Split at the first : and get the text after it
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
                        elif flag == 2:
                            # copy the thumbnail image to ../img/thumbnails folder
                            try:
                                shutil.copy(f"Project Expo/{folder}/Images/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                            except:
                                try: 
                                    shutil.copy(f"Project Expo/{folder}/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                                except:
                                    print(f"No thumbnail image found for {folder} project.")
                        else:
                            # copy the thumbnail image to ../img/thumbnails folder
                            try:
                                shutil.copy(f"Project Expo/{folder}/{image_name}", f"../assets/img/thumbnails/{final_image_name}")
                            except:
                                print(f"No thumbnail image found for {folder} project.")

                        # Update the thumbnail line
                        lines[i] = f"thumbnail: {final_image_name}\n"

                    
                    # if a line has ![ :
                    if '![' in line:
                        # Extract only ![ and ]( and ) from the line
                        image_section = line.split("!")[1].split(")")[0]

                        old_image_name = image_section.split("(")[-1].split(")")[0]
                        # Get the image name
                        image_name = image_section.split("(")[-1].split(")")[0]
                        # If the image name is a link
                        if image_name.startswith("http"):
                            continue
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
                                    print("\n\n")
                        
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
                                print("\n\n")
            
            # Open csv file
            with open("meet_links.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row)
                    if row['Project Code'] == folder:
                        # insert gmeet link on the 2nd line
                        lines.insert(1, f"""gmeet: "{row['GMeet Link']}"\n""")
                    
            # Write the updated lines to the .md file
            with open(f"Project Expo/{folder}/{new_md_title}.md", "w") as f:
                f.writelines(lines)

           # Delete file
            os.remove(f"Project Expo/{folder}/{file}")

            # Copy the .md file to the '../_posts' folder
            shutil.copy(f"Project Expo/{folder}/{new_md_title}.md", f"../_posts/{date}-{new_md_title}.md")

print("\n\nDone")
successful_projects = sorted(successful_projects)
print("Successful projects: ", successful_projects)

# Delete Project Expo folder
shutil.rmtree("Project Expo")