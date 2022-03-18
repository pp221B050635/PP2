import os
print('Exist:', os.access('c:\\ programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\ programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\ programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\ programming library.docx', os.X_OK))