import os

def format_title(title):
    return title.replace('_', ' ').replace('-', ' ')

reserved_folder = ['./docs/img', './docs/zan', './docs/rating']

if __name__ == '__main__':
    for root, folders, files in os.walk('./docs'):
        folders.sort()
        files.sort()
        content = ''

        if '_files' not in root:
            for folder in folders:
                if os.path.join(root, folder) not in reserved_folder and '_files' not in folder:
                    content += f'[{format_title(folder)}]({folder})\n\n'

            for file in files:
                if (file.endswith('.mkd') or file.endswith('.markdown')) and file != 'index.mkd':
                    name = format_title(file.rsplit('.', 1)[0])
                    content += f'[{name}]({file})\n\n'

                elif file.endswith('.html') and file != 'index.html':
                    name = format_title(file.rsplit('.', 1)[0])
                    content += f'[{name}]({file})\n\n'

            if content:
                title = f'title:{root.rsplit("/", 1)[-1]}\n\n\n\n'
                back = '<a href="../"><img src="/img/back.png" style="width:32px;height:32px;"></a><br><br>\n\n\n\n'

                if root != './docs':
                    content = title + back + content
                else:
                    with open('./docs/home.txt') as f:
                        content += f.read()

                with open(os.path.join(root, 'index.mkd'), 'w') as f:
                    f.write(content)
