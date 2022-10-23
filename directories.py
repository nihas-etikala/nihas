from pathlib import Path

# Abosolute path:
# eg: c:\Program files\Microsoft
path = Path()
# path1 = Path('eCommerce')
# path2 = Path('emails')
# path2.mkdir()
# path1.rmdir()
# mkdir : make directory
# rmdir : remove directory
# print(path1.exists())
# print(path2.exists())
for file in path.glob('*'):
    print(file)
