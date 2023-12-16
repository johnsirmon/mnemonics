import streamlit as st
import os
import re

# Function to extract command and prompt from file names
def extract_details(file_name):
    file_name_regex = r"(git_[a-z]+)_(.*).png"
    match = re.match(file_name_regex, file_name)
    if match:
        command, prompt = match.groups()
        return command.replace('_', ' ').title(), prompt.replace('_', ' ').capitalize()
    return None, None

# Function to load images and descriptions
def load_images_and_descriptions(images_folder):
    images = []
    for file_name in sorted(os.listdir(images_folder)):
        if file_name.endswith(".png"):
            command, prompt = extract_details(file_name)
            if command and prompt:
                images.append((command, prompt, os.path.join(images_folder, file_name)))
    return images

# Streamlit app layout
def display_app(images_folder):
    st.title("Git Command Visual Mnemonics")

    images = load_images_and_descriptions(images_folder)
    
    for command, prompt, image_path in images:
        st.header(f"Git Command: {command}")
        st.image(image_path, caption=prompt)

# Assuming the images folder is located at 'Images' relative to the script
images_folder_path = "Images"

# Display the app
display_app(images_folder_path)
