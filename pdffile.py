from basefile import BaseFile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import logging
import StringIO
import re


class PdfFile(BaseFile):
    def __init__(self, file_path):
        super(PdfFile, self).__init__(file_path)

    def get_content_in_text(self):
        logging.debug('Converting pdf to txt: ' + str(self.file_path))
        # Setup pdf reader
        rsrcmgr = PDFResourceManager()
        retstr = io.BytesIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        # Iterate through pages

        for page in PDFPage.get_pages(self.file_content, pagenos, maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)
        self.file_content.close()
        device.close()

        # Get full string from PDF
        full_string = retstr.getvalue()
        retstr.close()

        # Normalize a bit, removing line breaks
        full_string = full_string.replace("\r", "\n")
        full_string = full_string.replace("\n", " ")

        # Remove awkward LaTeX bullet characters
        full_string = re.sub(r"\(cid:\d{0,2}\)", " ", full_string)
        full_string = full_string.decode("utf-8")
        return full_string.encode('ascii', errors='ignore')


if __name__ == '__main__':
    pass
