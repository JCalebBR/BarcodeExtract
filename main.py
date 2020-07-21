from extract import Extract, OCRFailed
import keyboard


class Main:
    def __init__(self, filename=None):
        self.extract = Extract()

    def paste(self):
        try:
            self.extract.clipboardToImage()
            self.extract.imageToText()
            self.extract.textToClipboard()
        except OCRFailed:
            pass
        except AttributeError:
            pass


if __name__ == "__main__":
    main = Main()

    keyboard.add_hotkey("Ctrl+Shift+V", lambda: main.paste())

    keyboard.wait("Windows+Esc")
