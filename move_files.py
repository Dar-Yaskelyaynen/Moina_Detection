import os
import re

os.chdir('C:\\Users\\yasik\\anaconda3\\envs\\MoinaDataset\\creepy')

pattern_img = r'[\d_\w]*.jpg$'
pattern_txt = r'[\d_\w]*.txt$'
pattern_group = r'(train|valid)'

for dirpath, dirnames, filenames in os.walk('Raw_data'):
  for fn in filenames:
    img_name = re.search(pattern_img, fn)
    file_name = re.search(pattern_txt, fn)
    group = re.search(pattern_group, dirpath).group()

    if img_name:
      img_name = img_name.group()
      base_destination = f'MoinaDataset/labels/{group}/{img_name}'
      os.rename(f'{dirpath}/{img_name}', base_destination)
    if file_name:
      file_name = file_name.group()
      base_destination = f'MoinaDetectionDataset/labels/{group}/{file_name}'
      os.rename(f'{dirpath}/{file_name}', base_destination)
