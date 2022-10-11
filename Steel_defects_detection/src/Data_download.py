import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

data_paths = ['data/raw', 'data/interim', 'data/processed']

for path in data_paths:
    if not os.path.exists(path):
        print(f'Creating directory \'{path}\' ...')
        os.makedirs(path)

    else:
        print(f'Directory \'{path}\' exists')

if not os.path.exists('data/raw/defects-class-and-location.zip'):
    print('Downloading dataset...')
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset='zhangyunsheng/defects-class-and-location', path=data_paths[0])

else:
    print('Dataset has already been downloaded')


if os.path.exists('data/raw/images') and os.path.exists('data/raw/label'):
    print('Dataset has already been unpacked')

else:
    print('Unpacking dataset')
    with zipfile.ZipFile('data/raw/defects-class-and-location.zip', 'r') as zip_file:
        zip_file.extractall('data/raw/')
    print('Dataset unpacked')





