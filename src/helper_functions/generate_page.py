from helper_functions.markdown_to_html_node import markdown_to_html_node

import os


def extract_title(markdown: str):
    if not markdown.strip().startswith('#'):
        raise Exception('No valid header was found!')

    title = markdown.strip().split('\n')[0].lstrip('#').strip()

    return title

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page {from_path} to {dest_path} using {template_path}')

    if not os.path.isfile(from_path):
        raise Exception('[Error] -  File does not exist in specifed path', from_path)
    
    if not os.path.isfile(template_path):
        raise Exception('Template path does not exist')
    
    text_content = ''
    template_content = ''

    with open(from_path) as f:
        text_content += f.read() 

    with open(template_path) as f:
        template_content += f.read()

    html_text = markdown_to_html_node(text_content).to_html()

    title = extract_title(text_content)

    template_content = template_content.replace("{{ Content }}", html_text)
    template_content = template_content.replace('{{ Title }}', title)

    dirname = os.path.dirname(dest_path)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(dest_path, 'w') as f:
        f.write(template_content)
    
    
    
