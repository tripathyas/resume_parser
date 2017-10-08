class BaseFile(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = open(self.file_path, 'rb')

if __name__ == '__main__':
    pass
    