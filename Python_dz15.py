import os, sys
from collections import namedtuple
import logging




logging.basicConfig(filename='logs.log', filemode='a+', encoding='utf-8',  level=logging.DEBUG)
logging.info('Программа запущена')
print('Введите путь до директории на ПК')
def Target_info(target_path):
    obj_info = namedtuple('obj_info',['file_name', 'extension', 'parent_name'])
    if os.path.exists(target_path):
        with open("files_info.txt", "w",encoding='utf-8',) as file:
            for item in os.listdir(target_path):
                obj = item.split('.')
                obj_path = os.path.abspath(f'{target_path}//{item}')
                if len(obj) == 1:
                    temp_obj = obj_info(obj[0],'folder', obj_path)
                    file.writelines(f'{temp_obj.file_name} {temp_obj.extension} {temp_obj.parent_name}'+'\n')
                    logging.info(f'{temp_obj.file_name} {temp_obj.extension} {temp_obj.parent_name}')
                else:
                    temp_obj = obj_info(obj[0],obj[1], obj_path)
                    file.writelines(f'{temp_obj.file_name} {temp_obj.extension} {temp_obj.parent_name}'+'\n')
                    logging.info(f'{temp_obj.file_name} {temp_obj.extension} {temp_obj.parent_name}')
            print('Файл с информацией создан, программа завершена')
            
    else: 
        print('Неправильный путь')
        logging.warning('Неправильный путь')
Target_info(input())
logging.info('Программа завершена')   