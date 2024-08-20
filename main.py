from PyQt5.QtWidgets import QApplication
from ui import DownloaderUI
from downloader import Downloader
import sys


class MainApp(DownloaderUI):
    def __init__(self):
        super().__init__()

        self.download_button.clicked.connect(self.download_video)

    def download_video(self):
        url = self.url_input.text()
        format = self.format_combo.currentText()
        output_folder = self.folder_input.text()
        if url and output_folder:
            self.download_list.addItem(f"Starting download: {url}")
            downloader = Downloader(url, format, output_folder, self.update_progress_bar, self.download_complete)
            downloader.start_download()

    def update_progress_bar(self, value):
        self.progress_bar.setValue(int(value))

    def download_complete(self):
        self.download_list.addItem("Download completed!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
