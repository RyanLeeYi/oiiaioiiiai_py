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
        
        # State management (Group 1 or Group 2, each with GIF/PNG state)
        self.current_group = 1  # Start with group 1 (1 or 2)
        self.is_gif_state = True  # True = GIF, False = PNG
        self.isAutoSwitching = True  # Auto-switch mode enabled by default
        self.isMuted = False  # Mute state
        self.dragging = False
        self.drag_position = QPoint()
        
        # Scale settings
        self.scale_factor = 1.0  # Default scale (1.0 = 100%)
        self.base_size = 200  # Base window size
        
        # Group 1 paths (使用 resource_path 以支援 PyInstaller 打包)
        self.group1_gif_path = self.resource_path(os.path.join("Images", "OIIAIOIIIAI.gif"))
        self.group1_png_path = self.resource_path(os.path.join("Images", "OIIAIOIIIAI_stop.png"))
        self.group1_music_path = self.resource_path(os.path.join("Images", "oiia-oiia-sound.mp3"))
        
        # Group 2 paths (使用 resource_path 以支援 PyInstaller 打包)
        self.group2_gif_path = self.resource_path(os.path.join("Images", "borzoi-siren.gif"))
        self.group2_png_path = self.resource_path(os.path.join("Images", "borzoi-siren_stop.png"))
        self.group2_music_path = self.resource_path(os.path.join("Images", "borzoi-siren-sound.mp3"))
        
        # Music state
        self.music_loaded_group1 = False
        self.music_loaded_group2 = False
        self.current_music_group = None
        
        # Auto-switch intervals for each group and state (in milliseconds)
        # Group 1 timings
        self.group1_gif_duration = 2000   # 2 seconds for group 1 GIF
        self.group1_png_duration = 1000   # 1 second for group 1 PNG
        
        # Group 2 timings
        self.group2_gif_duration = 5500   # 5 seconds for group 2 GIF
        self.group2_png_duration = 1500   # 1.5 seconds for group 2 PNG
        
        # Initialize UI
        self.initUI()
        
        # Setup auto-switch timer
        self.auto_switch_timer = QTimer()
        self.auto_switch_timer.timeout.connect(self.toggle_state)
        self.update_timer_interval()  # Set initial interval based on current group
        
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
    
    def update_window_size(self):
        """Update window and label size based on scale factor"""
        new_size = int(self.base_size * self.scale_factor)
        self.setFixedSize(new_size, new_size)
        self.image_label.setGeometry(0, 0, new_size, new_size)
        # Reload image to fit new size
        self.load_image()

    def initUI(self):
        """Initialize the user interface"""
        # Window properties
        self.setWindowFlags(
            Qt.FramelessWindowHint |  # No frame
            Qt.WindowStaysOnTopHint |  # Always on top
            Qt.Tool  # Don't show in taskbar
        )
        self.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background
        
        # Create label for image display
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("padding: 10px;")  # 10px margin
        
        # Set initial size
        self.update_window_size()
        
        # Load initial image (GIF animation)
        self.load_image()
        
        # Set initial position (center of screen)
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        
        self.show()
    
    def load_image(self):
        """Load and display the current image based on group and state"""
        if self.current_group == 1:
            if self.is_gif_state:
                self._load_gif(self.group1_gif_path, self.group1_music_path, 1, "Group 1 GIF")
            else:
                self._load_png(self.group1_png_path, "Group 1 PNG")
        else:  # group 2
            if self.is_gif_state:
                self._load_gif(self.group2_gif_path, self.group2_music_path, 2, "Group 2 GIF")
            else:
                self._load_png(self.group2_png_path, "Group 2 PNG")
    
    def _load_gif(self, gif_path, music_path, group_num, gif_name):
        """Helper method to load and display a GIF with its music"""
        if os.path.exists(gif_path):
            self.movie = QMovie(gif_path)
            if self.movie.isValid():
                # Scale movie to fit within label with margin
                self.movie.setScaledSize(self.image_label.size() * 0.9)
                self.image_label.setMovie(self.movie)
                self.movie.start()
                # Play music for this group
                self.play_music(music_path, group_num)
            else:
                self.show_error(f"Invalid {gif_name} file")
        else:
            self.show_error(f"{gif_name} not found: {gif_path}")
    
    def _load_png(self, png_path, png_name):
        """Helper method to load and display PNG"""
        if os.path.exists(png_path):
            pixmap = QPixmap(png_path)
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
                self.show_error(f"Invalid {png_name} file")
        else:
            self.show_error(f"{png_name} not found: {png_path}")
    
    def show_error(self, message):
        """Display error message in the label"""
        self.image_label.setText(f"Error:\n{message}")
        self.image_label.setStyleSheet("color: red; padding: 10px;")
    
    def play_music(self, music_path, group_num):
        """Play background music for specific group"""
        if self.isMuted:
            return  # Don't play if muted
        
        try:
            if os.path.exists(music_path):
                # Only reload if switching to different group's music
                if self.current_music_group != group_num:
                    pygame.mixer.music.load(music_path)
                    self.current_music_group = group_num
                    if group_num == 1:
                        self.music_loaded_group1 = True
                    else:
                        self.music_loaded_group2 = True
                pygame.mixer.music.play(-1)  # Loop indefinitely
            else:
                print(f"Music file not found: {music_path}")
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
            if self.is_gif_state:
                music_path = self.group1_music_path if self.current_group == 1 else self.group2_music_path
                self.play_music(music_path, self.current_group)
    
    def update_timer_interval(self):
        """Update auto-switch timer interval based on current group and state"""
        if self.current_group == 1:
            interval = self.group1_gif_duration if self.is_gif_state else self.group1_png_duration
        else:
            interval = self.group2_gif_duration if self.is_gif_state else self.group2_png_duration
        self.auto_switch_timer.setInterval(interval)
    
    def toggle_state(self):
        """Toggle between GIF and PNG within current group"""
        self.is_gif_state = not self.is_gif_state
        self.load_image()
        # Update timer interval for the new state
        if self.isAutoSwitching:
            self.update_timer_interval()
    
    def set_group(self, group_num, is_gif=True):
        """Set specific group and state"""
        self.current_group = group_num
        self.is_gif_state = is_gif
        self.update_timer_interval()  # Update timer interval for new group
        self.load_image()
    
    def zoom_in(self):
        """Increase size by 25%"""
        if self.scale_factor < 3.0:  # Max 300%
            self.scale_factor += 0.25
            self.update_window_size()
    
    def zoom_out(self):
        """Decrease size by 25%"""
        if self.scale_factor > 0.5:  # Min 50%
            self.scale_factor -= 0.25
            self.update_window_size()
    
    def reset_zoom(self):
        """Reset to original size (100%)"""
        self.scale_factor = 1.0
        self.update_window_size()
    
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
        
        # Toggle State action (within current group)
        toggle_action = QAction("切換狀態 (GIF ↔ PNG)", self)
        toggle_action.triggered.connect(self.toggle_state)
        menu.addAction(toggle_action)
        
        menu.addSeparator()
        
        # Group 1 selection
        group1_menu = menu.addMenu("oiiaoiiiai")
        group1_gif_action = QAction("顯示 oiiaoiiiai GIF", self)
        group1_gif_action.triggered.connect(lambda: self.set_group(1, True))
        group1_menu.addAction(group1_gif_action)
        
        group1_png_action = QAction("顯示 oiiaoiiiai PNG", self)
        group1_png_action.triggered.connect(lambda: self.set_group(1, False))
        group1_menu.addAction(group1_png_action)
        
        # Group 2 selection
        group2_menu = menu.addMenu("Siren Dog")
        group2_gif_action = QAction("顯示 Siren Dog GIF ", self)
        group2_gif_action.triggered.connect(lambda: self.set_group(2, True))
        group2_menu.addAction(group2_gif_action)
        
        group2_png_action = QAction("顯示 Siren Dog PNG", self)
        group2_png_action.triggered.connect(lambda: self.set_group(2, False))
        group2_menu.addAction(group2_png_action)
        
        menu.addSeparator()
        
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
        
        # Zoom options
        zoom_in_action = QAction(f"放大 (+25%) [目前: {int(self.scale_factor * 100)}%]", self)
        zoom_in_action.triggered.connect(self.zoom_in)
        menu.addAction(zoom_in_action)
        
        zoom_out_action = QAction("縮小 (-25%)", self)
        zoom_out_action.triggered.connect(self.zoom_out)
        menu.addAction(zoom_out_action)
        
        reset_zoom_action = QAction("重設大小 (100%)", self)
        reset_zoom_action.triggered.connect(self.reset_zoom)
        menu.addAction(reset_zoom_action)
        
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
