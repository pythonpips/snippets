    """author: pythonpips"""

    import os.path

    file_path = './example.txt'
    exists = os.path.isfile(file_path)
    print(exists)
    # outputs True
