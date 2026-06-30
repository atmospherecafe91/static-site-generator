import os

from utils import get_project_root
import shutil

ROOT_DIR = get_project_root()

def copy_static_files():

    dest_path  = os.path.join(ROOT_DIR, 'docs')
    copy_path = os.path.join(ROOT_DIR, 'static')
    
    
    try:
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
        else:
            shutil.rmtree(dest_path)
            os.mkdir(dest_path)
        

    except Exception as e:
        print('[*] - File already exists', e)
    
    
    files = os.listdir(copy_path)

    if files:
        copy_recursive_fn(copy_path, dest_path, files)



def copy_recursive_fn(src: str, dest: str, files: list[str]):
    for file in files:
        try:
            path = os.path.join(src, file)

            if os.path.isfile(path):
                shutil.copy(path, dest)
                print(f'[*] File Copied - {path}')
            else:
                content = os.listdir(path)
                destination_path = os.path.join(dest, file)
                source_path = os.path.join(src, file)

                if not os.path.exists(destination_path):
                        os.mkdir(destination_path)

                if content:             
                    copy_recursive_fn(source_path, destination_path, content)
        except Exception as e:
            print('[Error] - Couldn\'t copy file to destination', e )
        

