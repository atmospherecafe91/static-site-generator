import os
import sys
from pathlib import Path

from textnode import TextNode, TextType
from copy_static_file import copy_static_files
from helper_functions.generate_page import generate_page

from utils import get_project_root

ROOT_DIR = get_project_root()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    directory_path_full = os.path.join(ROOT_DIR, dir_path_content)
    
    content_list = os.listdir(directory_path_full)

    for file in content_list:

        file_path = os.path.join(directory_path_full, file)

        relative_file_path = os.path.join(
            dir_path_content, file
        )

        file_parts = "/".join(Path(relative_file_path).parts[1:])


        file_join = os.path.join(ROOT_DIR, dest_dir_path, file_parts)

        dest_file = os.path.splitext(file_join)[0] + '.html'


        if os.path.isfile(file_path):

            generate_page(file_path, f"{ROOT_DIR}/template.html", f"{dest_file}", basepath)
        
        else:
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, dest_dir_path, basepath)


def main():

    basepath = '/'

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static_files()
    generate_pages_recursive("content", "template.html", "docs", basepath)
        
        



    

if __name__ == "__main__":
    main()
