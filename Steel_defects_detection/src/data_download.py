import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

data_paths = [Path('../data/raw'), Path('../data/interim'), Path('../data/processed')]

for dir in data_paths:
    if not dir.exists:
        print(f'Creating directory \'{dir}\'...')
        dir.mkdir()

    else:
        print(f'Directory \'{dir}\' exists')

if not os.path.exists('data/raw/defects-class-and-location.zip'):
    print('Downloading dataset...')
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset='zhangyunsheng/defects-class-and-location', path=data_paths[0])

else:
    print('Dataset has already been downloaded')


if Path('data/raw/images').exists() and Path('data/raw/label').exists():
    print('Dataset has already been unpacked')

else:
    print('Unpacking dataset...')
    with zipfile.ZipFile('data/raw/defects-class-and-location.zip', 'r') as zip_file:
        zip_file.extractall('data/raw/')
    print('Dataset unpacked')





