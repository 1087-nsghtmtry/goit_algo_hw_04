import pathlib
from cats_handler import get_cats_info

current_path = pathlib.Path(__file__).parent
cats_info = get_cats_info(current_path)
print(cats_info)

