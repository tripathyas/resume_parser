import logging
import os
import re
from pdffile import PdfFile


class ResumeParser():

    def __init__(self, file_path):
        logging.debug("Initializing ResumeParser")
        self.file_path = file_path
        self.file_type = self.extract_file_type()
        self.file_object = self.file_factory()
        self.text_content = self.file_object.get_content_in_text()
        print("done")

    def extract_file_type(self):
        return os.path.splitext(self.file_path)[1]

    def read_file_content(self):
        pass

    def file_factory(self):
        if self.file_type == ".pdf":
            return PdfFile(self.file_path)

    def convert_to_raw_data(self):
        pass

    def extract_required_info(self):
        pass

    def create_output_file(self, info):
        pass


if __name__ == '__main__':
    logging.basicConfig(filename='resume_parser.log',
                        level=logging.DEBUG, filemode='w')
    resumeParser = ResumeParser(
        "/home/shubhi/Downloads/Ashutosh_Tripathy_Intel_6.1Yrs_Bang.pdf")
