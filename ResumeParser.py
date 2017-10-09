import logging
import os
import re
from pdffile import PdfFile
import sys
import pandas as pd
from ParamRegexMap import ParamRegexMap as prmap
import glob


class ResumeParser():

    def __init__(self, file_path):
        logging.debug("Initializing ResumeParser")
        self.file_path = file_path
        self.file_type = self.extract_file_type()
        self.file_object = self.file_factory()
        # self.text_content = self.file_object.get_content_in_text()

    def extract_file_type(self):
        return os.path.splitext(self.file_path)[1]

    def read_file_content(self):
        pass

    def file_factory(self):
        if self.file_type == ".pdf":
            return PdfFile()

    def convert_to_raw_data(self):
        pass

    def extract_required_info(self):
        file_list = glob.glob(self.file_path)
        logging.info('Iterating through file_list: ' + str(file_list))

        resume_summary_df = pd.DataFrame()
        resume_summary_df["file_path"] = file_list

        resume_summary_df["raw_text"] = resume_summary_df["file_path"].apply(
            self.file_object.get_content_in_text)
        resume_summary_df["num_words"] = resume_summary_df["raw_text"].apply(
            lambda x: len(x.split()))

        resume_summary_df["email"] = resume_summary_df["raw_text"].apply(
            prmap.check_email)
        resume_summary_df["phone_number"] = resume_summary_df["raw_text"].apply(
            prmap.check_phone_number)

        return resume_summary_df

    def create_json_file(self, info):
        # Output to json
        filter_df = info[prmap.param_list].iloc[0]
        filter_df.to_json("./data/output/resume_data.json")


if __name__ == '__main__':
    logging.basicConfig(filename='resume_parser.log',
                        level=logging.INFO, filemode='w')
    resumeParser = ResumeParser(
        "./data/input/Brendan_Herger_Resume.pdf")
    resume_df = resumeParser.extract_required_info()
    resumeParser.create_json_file(resume_df)

    logging.info('End Main')
    print("successfully completed")
    input()