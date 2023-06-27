import os
import shutil

def normalize(name):
    trans_dict = {
        'А': 'Ah', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye',
        'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L',
        'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh'
    }
    
    normalized_name = ''
    for char in name:
        if char.upper() in trans_dict:
            normalized_name += trans_dict[char.upper()]
        else:
            normalized_name += char
    return normalized_name

def sort_folder(path):
   
    os.makedirs(os.path.join(path, 'images'), exist_ok=True)
    os.makedirs(os.path.join(path, 'documents'), exist_ok=True)
    os.makedirs(os.path.join(path, 'audio'), exist_ok=True)
    os.makedirs(os.path.join(path, 'video'), exist_ok=True)
    os.makedirs(os.path.join(path, 'archives'), exist_ok=True)

    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path) and item not in ['images', 'documents', 'audio', 'video', 'archives']:
            sort_folder(item_path)
            continue

        
        extension = item.split('.')[-1].upper()

        
        if extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
            shutil.move(item_path, os.path.join(path, 'images', normalize(item)))
        elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
            shutil.move(item_path, os.path.join(path, 'video', normalize(item)))
        elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
            shutil.move(item_path, os.path.join(path, 'documents', normalize(item)))
        elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
            shutil.move(item)