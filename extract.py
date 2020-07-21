from PIL import ImageGrab, Image
import pytesseract
import win32clipboard


class Extract:
    def __init__(self, filename="test.png", filetype="PNG"):
        self.filename = filename
        self.filetype = filetype
        pytesseract.pytesseract.tesseract_cmd = (
            "C:\\Tesseract-OCR\\tesseract.exe"
        )
        self.im = ImageGrab
        self.result = None

    def clipboardToImage(self):
        self.im.clip = self.im.grabclipboard()
        self.im.clip.save(self.filename, self.filetype)

    def imageToText(self):
        self.result = pytesseract.image_to_string(
            Image.open(self.filename)
        )

    def textToClipboard(self):
        if self.result:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(
                win32clipboard.CF_UNICODETEXT, self.result
            )
            win32clipboard.CloseClipboard()
        else:
            raise OCRFailed


class OCRFailed(Exception):
    """Raised when OCR fails"""

    def __init__(self, *args, **kwargs):
        Exception(*args, **kwargs)
