import os

def format_title(title):
    return title.replace('_', ' ').replace('-', ' ')

reserved_folder = ['./docs/img', './docs/zan', './docs/rating']

# SVG back arrow (inline HTML) to include above links
BACK_BUTTON_HTML = '''
<a href="../" style="display:inline-block;margin-bottom:16px;">
  <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="none" stroke="#555" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <line x1="19" y1="12" x2="5" y2="12"/>
    <polyline points="12 19 5 12 12 5"/>
  </svg>
</a>

\n\n
'''

if __name__ == '__main__':
    for root, folders, files in os.walk('./docs'):
        folders.sort()
        files.sort()
        content = ''

        if '_files' not in root:
            for folder in folders:
                full_path = os.path.join(root, folder)
                if full_path not in reserved_folder and '_files' not in folder:
                    content += f'[{format_title(folder)}]({folder})\n\n'

            for file in files:
                if (file.endswith('.mkd') or file.endswith('.markdown')) and file != 'index.mkd':
                    name = format_title(file.rsplit('.', 1)[0])
                    content += f'[{name}]({file})\n\n'
                elif file.endswith('.html') and file != 'index.html':
                    name = format_title(file.rsplit('.', 1)[0])
                    content += f'[{name}]({file})\n\n'

            if content:
                folder_title = format_title(root.rsplit('/', 1)[-1])
                title_block = f'title:{folder_title}\n\n\n\n'

                # Add back button only if not in the root folder
                if root != './docs':
                    content = title_block + BACK_BUTTON_HTML + content
                else:
                    try:
                        with open('./docs/home.txt') as f:
                            content += f.read()
                    except FileNotFoundError:
                        content += "\n\n_Welcome page content not found._"

                # Write the index.mkd file
                with open(os.path.join(root, 'index.mkd'), 'w') as f:
                    f.write(content)
