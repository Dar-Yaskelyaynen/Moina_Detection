import os
from sklearn.model_selection import train_test_split
import numpy as np


def move_files(file_list, file_type='images', group='train'):
    another_group = 'test' if group == 'train' else 'train'
    for file_name in file_list: 
        print(os.getcwd())
        if os.path.isfile(f'dataset\\{file_type}\\{file_name}'):
            os.replace(f'dataset\\{file_type}\\{file_name}', f'dataset\\{file_type}\\{group}\\{file_name}')
        elif os.path.isfile(f'dataset\\{file_type}\\{another_group}\\{file_name}'):
            os.replace(f'dataset\\{file_type}\\{another_group}\\{file_name}', f'dataset\\{file_type}\\{group}\\{file_name}')


def split_data():
    os.chdir('C:\\Users\\yasik\\anaconda3\\envs\\MoinaDataset\\creepy')	
    images_list = os.listdir('pictures\\')
    raw_prefix = [name.split('.')[0] for name in images_list]
    labels_list = [f'{name}.txt' for name in raw_prefix]

    X_train, X_test, Y_train, Y_test = train_test_split(images_list, labels_list)
    move_files(X_train, file_type='images', group='train')
    move_files(X_test, file_type='images', group='test')
    move_files(Y_train, file_type='labels', group='train')
    move_files(Y_test, file_type='labels', group='test')
    with open('train.txt', 'w') as out:
        for img_name in X_train:
            out.write(img_name)
            out.write('\n')

    with open('test.txt', 'w') as out:
        for img_name in X_test:
            out.write(img_name)
            out.write('\n')


if __name__ == '__main__':
    split_data()
