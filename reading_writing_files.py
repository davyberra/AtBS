from pathlib import Path
import os

# print(str(Path('spam', 'bacon', 'eggs')))

home_folder = Path('C:/Users/Davy')
sub_folder = Path('spam')

# print(home_folder / sub_folder)

# print(Path.cwd())
#
# print(Path.home())

Path(r'C:\Users\Davy\butts').mkdir()