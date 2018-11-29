"""author: @pythonpips"""

import os
print(os.getcwd())
# outputs: '/Users/pythonpips' 

from pathlib import Path
print(Path.cwd())
# outputs: PosixPath('/Users/pythonpips')
