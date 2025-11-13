"""
Desktop Pet Application
A transparent, draggable desktop pet that can display animated GIFs and static PNGs
"""

import sys
import os
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QMenu, QAction)
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QPixmap, QMovie, QCursor
import pygame


class DesktopPet(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize pygame mixer for music
        pygame.mixer.init()
        
        # State management
        self.isAnimating = True  # Start with GIF animation
        self.isAutoSwitching = True  # Auto-switch mode enabled by default
        self.isMuted = False  # Mute state
        self.dragging = False
        self.drag_position = QPoint()
        
        # Image paths (使用 resource_path 以支援 PyInstaller 打包)
        self.gif_path = self.resource_path(os.path.join("Images", "OIIAIOIIIAI.gif"))
        self.png_path = self.resource_path(os.path.join("Images", "OIIAIOIIIAI_stop.png"))
        
        # Music path (使用 resource_path 以支援 PyInstaller 打包)
        self.music_path = self.resource_path(os.path.join("Images", "oiia-oiia-sound.mp3"))
        self.music_loaded = False
        
        # Initialize UI
        self.initUI()
        
        # Setup auto-switch timer
        self.auto_switch_timer = QTimer()
        self.auto_switch_timer.timeout.connect(self.toggle_state)
        self.auto_switch_timer.setInterval(2000)  # 2 seconds
        
        # Start auto-switch mode
        if self.isAutoSwitching:
            self.auto_switch_timer.start()
    
    def resource_path(self, relative_path):
        """ 取得資源的絕對路徑 (無論是在開發環境還是打包後的 .exe 中) """
        try:
            # PyInstaller 會建立一個暫存資料夾，並將路徑存在 _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            # 如果不是在 PyInstaller 環境中 (例如直接執行 .py)，則使用目前路徑
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def initUI(self):
        """Initialize the user interface"""
        # Window properties
        self.setWindowFlags(
            Qt.FramelessWindowHint |  # No frame
            Qt.WindowStaysOnTopHint |  # Always on top
            Qt.Tool  # Don't show in taskbar
        )
        self.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background
        self.setFixedSize(200, 200)  # Fixed size 200x200
        
        # Create label for image display
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("padding: 10px;")  # 10px margin
        self.image_label.setGeometry(0, 0, 200, 200)
        
        # Load initial image (GIF animation)
        self.load_image()
        
        # Set initial position (center of screen)
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        
        self.show()
    
    def load_image(self):
        """Load and display the current image based on state"""
        if self.isAnimating:
            # Load GIF animation
            if os.path.exists(self.gif_path):
                self.movie = QMovie(self.gif_path)
                if self.movie.isValid():
                    # Scale movie to fit within label with margin
                    self.movie.setScaledSize(self.image_label.size() * 0.9)
                    self.image_label.setMovie(self.movie)
                    self.movie.start()
                    # Play music when GIF starts
                    self.play_music()
                else:
                    self.show_error("Invalid GIF file")
            else:
                self.show_error(f"GIF file not found: {self.gif_path}")
        else:
            # Load static PNG
            if os.path.exists(self.png_path):
                pixmap = QPixmap(self.png_path)
                if not pixmap.isNull():
                    # Scale pixmap to fit within label with margin, maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.image_label.size() * 0.9,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.image_label.setPixmap(scaled_pixmap)
                    # Stop music when showing PNG
                    self.stop_music()
                else:
                    self.show_error("Invalid PNG file")
            else:
                self.show_error(f"PNG file not found: {self.png_path}")
    
    def show_error(self, message):
        """Display error message in the label"""
        self.image_label.setText(f"Error:\n{message}")
        self.image_label.setStyleSheet("color: red; padding: 10px;")
    
    def play_music(self):
        """Play background music"""
        if self.isMuted:
            return  # Don't play if muted
        
        try:
            if os.path.exists(self.music_path):
                if not self.music_loaded:
                    pygame.mixer.music.load(self.music_path)
                    self.music_loaded = True
                pygame.mixer.music.play(-1)  # Loop indefinitely
            else:
                print(f"Music file not found: {self.music_path}")
        except Exception as e:
            print(f"Error playing music: {e}")
    
    def stop_music(self):
        """Stop background music"""
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            print(f"Error stopping music: {e}")
    
    def toggle_mute(self):
        """Toggle mute on/off"""
        self.isMuted = not self.isMuted
        
        if self.isMuted:
            # Mute: stop music
            self.stop_music()
        else:
            # Unmute: play music if in GIF state
            if self.isAnimating:
                self.play_music()
    
    def toggle_state(self):
        """Toggle between GIF animation and PNG static image"""
        self.isAnimating = not self.isAnimating
        self.load_image()
    
    def toggle_auto_switch(self):
        """Toggle auto-switch mode on/off"""
        self.isAutoSwitching = not self.isAutoSwitching
        
        if self.isAutoSwitching:
            self.auto_switch_timer.start()
        else:
            self.auto_switch_timer.stop()
    
    def mousePressEvent(self, event):
        """Handle mouse press events"""
        if event.button() == Qt.LeftButton:
            # Start dragging
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        elif event.button() == Qt.MiddleButton:
            # Manual state toggle
            self.toggle_state()
            event.accept()
        elif event.button() == Qt.RightButton:
            # Show context menu
            self.show_context_menu(event.globalPos())
            event.accept()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events for dragging"""
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()
    
    def show_context_menu(self, position):
        """Show right-click context menu"""
        menu = QMenu(self)
        
        # Toggle State action
        toggle_action = QAction("切換狀態", self)
        toggle_action.triggered.connect(self.toggle_state)
        menu.addAction(toggle_action)
        
        # Auto Switch Mode action (checkable)
        auto_switch_action = QAction("自動切換模式", self)
        auto_switch_action.setCheckable(True)
        auto_switch_action.setChecked(self.isAutoSwitching)
        auto_switch_action.triggered.connect(self.toggle_auto_switch)
        menu.addAction(auto_switch_action)
        
        # Mute action (checkable)
        mute_action = QAction("靜音", self)
        mute_action.setCheckable(True)
        mute_action.setChecked(self.isMuted)
        mute_action.triggered.connect(self.toggle_mute)
        menu.addAction(mute_action)
        
        menu.addSeparator()
        
        # Exit action
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close_application)
        menu.addAction(exit_action)
        
        # Show menu at cursor position
        menu.exec_(position)
    
    def close_application(self):
        """Clean up and close the application"""
        self.auto_switch_timer.stop()
        self.stop_music()
        pygame.mixer.quit()
        QApplication.quit()
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.auto_switch_timer.stop()
        self.stop_music()
        pygame.mixer.quit()
        event.accept()


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Create and show desktop pet
    pet = DesktopPet()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
