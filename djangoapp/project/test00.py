from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web'

print(f'BASE_DIR={BASE_DIR}')
print(f'DATA_DIR={DATA_DIR}')
