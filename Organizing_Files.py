import shutil, os, re
from pathlib import Path

path = Path.home()

dates = ["asdfoienwef12-30-2004", "adsfowefnweon05-15-1999", "asdfoaf"]

date_pattern = re.compile(r"""
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.X | re.M)

#TODO: Loop over the files in the working directory
mo_list = []
for s in dates:
    mo = date_pattern.search(s)
    if mo:
        mo_list.append(mo)

print(mo_list)

#TODO: Skip files without a date.

#TODO: Get the different parts of the filename.

#TODO: Form the European-style filename.

#TODO: Get the full, absolute file paths.

#TODO: Rename the files.