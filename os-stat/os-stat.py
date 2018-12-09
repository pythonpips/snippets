"""author: @pythonpips"""

import os

os.stat('example.txt')
"""
outputs: os.stat_result(
    st_mode=33188, 
    st_ino=17043304, 
    st_dev=16777220, 
    st_nlink=1, 
    st_uid=501, 
    st_gid=20, 
    st_size=0, 
    st_atime=1544260359, 
    st_mtime=1544260359, 
    st_ctime=1544260359
)
"""