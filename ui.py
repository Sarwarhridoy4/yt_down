from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, \
    QProgressBar, QComboBox, QFileDialog
from PyQt5.QtGui import QFont, QIcon


class DownloaderUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Video Downloader")
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon("icon.png"))
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # URL input
        url_layout = QHBoxLayout()
        self.url_label = QLabel("Video URL:")
        self.url_label.setFont(QFont('Arial', 10))
        self.url_input = QLineEdit()
        self.url_input.setFont(QFont('Arial', 10))
        url_layout.addWidget(self.url_label)
        url_layout.addWidget(self.url_input)

        # Format Selection
        format_layout = QHBoxLayout()
        self.format_label = QLabel("Format:")
        self.format_label.setFont(QFont('Arial', 10))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4", "MP3", "WEBM"])
        self.format_combo.setFont(QFont('Arial', 10))
        format_layout.addWidget(self.format_label)
        format_layout.addWidget(self.format_combo)

        # Output Folder Selection
        folder_layout = QHBoxLayout()
        self.folder_label = QLabel("Output Folder:")
        self.folder_label.setFont(QFont('Arial', 10))
        self.folder_input = QLineEdit()
        self.folder_input.setFont(QFont('Arial', 10))
        self.folder_button = QPushButton("Browse")
        self.folder_button.setFont(QFont('Arial', 10))
        self.folder_button.setStyleSheet("background-color: #1e90ff; color: white;")
        self.folder_button.clicked.connect(self.select_folder)
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(self.folder_button)

        # Download Button
        self.download_button = QPushButton("Download")
        self.download_button.setFont(QFont('Arial', 12))
        self.download_button.setStyleSheet("background-color: #1e90ff; color: white; padding: 10px;")

        # Download List
        self.download_list = QListWidget()
        self.download_list.setFont(QFont('Arial', 10))

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFont(QFont('Arial', 10))
        self.progress_bar.setStyleSheet("QProgressBar::chunk { background-color: #1e90ff; }")

        layout.addLayout(url_layout)
        layout.addLayout(format_layout)
        layout.addLayout(folder_layout)
        layout.addWidget(self.download_button)
        layout.addWidget(self.download_list)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        if folder:
            self.folder_input.setText(folder)
