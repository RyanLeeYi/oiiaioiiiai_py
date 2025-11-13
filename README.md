# Desktop Pet Application / 桌面寵物應用程式

[English](#english) | [中文](#中文)

---

## English

A cute, transparent desktop pet that lives on your screen! This Python application creates a draggable, always-on-top window that displays animated GIF with background music.

### Features

- **Transparent Window**: Only the pet image is visible, no borders or background
- **Always On Top**: Pet stays visible above all other windows
- **Draggable**: Click and drag your pet anywhere on the screen
- **Animated & Static States**: Switch between animated GIF and static PNG images
- **Background Music**: Plays music when showing GIF animation
- **Mute Option**: Toggle sound on/off via context menu
- **Auto-Switch Mode**: Automatically alternates between states every 3 seconds (enabled by default)
- **Manual Controls**: Use middle-click or context menu to toggle states
- **PyInstaller Ready**: Can be packaged into standalone executable

### Requirements

- Python 3.6 or higher
- PyQt5
- pygame

### Installation

1. Install Python if you haven't already: https://www.python.org/downloads/

2. Install required packages:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install PyQt5 pygame
```

### Setup

Place your files in the `Images/` folder:
- `OIIAIOIIIAI.gif` - Animated GIF (for active state)
- `OIIAIOIIIAI_stop.png` - Static PNG (for idle state)
- `music.mp3` - Background music (supports MP3, OGG, WAV)

Recommended image size: 180x180 pixels or smaller

### Usage

Run the application:
```bash
python oiiaioiiiai.py
```

Or build standalone executable:
```bash
pyinstaller oiiaioiiiai.spec
```
The executable will be in `dist/oiiaioiiiai.exe`

### Controls

| Action | Description |
|--------|-------------|
| **Left Click + Drag** | Move the pet around your screen |
| **Middle Click** | Manually toggle between animated and static states |
| **Right Click** | Open context menu |

### Context Menu Options

- **切換狀態 (Toggle State)**: Manually switch between GIF and PNG
- **自動切換模式 (Auto Switch Mode)**: Enable/disable automatic switching
- **靜音 (Mute)**: Toggle music on/off
- **退出 (Exit)**: Close the application

### Music Behavior

- Music plays automatically when GIF animation is displayed
- Music stops when switching to static PNG
- Music loops indefinitely while GIF is showing
- Can be muted via context menu (mute state persists across toggles)

### File Structure

```
project_root/
├── oiiaioiiiai.py           # Main application file
├── oiiaioiiiai.spec         # PyInstaller spec file
├── requirements.txt         # Python dependencies
├── Images/                  # Resource folder
│   ├── OIIAIOIIIAI.gif     # Animated pet image
│   ├── OIIAIOIIIAI_stop.png # Static pet image
│   ├── music.mp3           # Background music
│   └── README.txt          # Image folder instructions
└── README.md               # This file
```

### Troubleshooting

**Music not playing:**
- Ensure `music.mp3` exists in `Images/` folder
- Check mute is not enabled (right-click → uncheck Mute)
- Verify file format is supported (MP3, OGG, WAV)

**Images not showing:**
- Ensure image files exist in `Images/` folder
- Check that files are valid and not corrupted

---

## 中文

一個可愛的透明桌面寵物，陪伴您在螢幕上！此 Python 應用程式創建一個可拖曳、永遠置頂的視窗，顯示動畫 GIF 並播放背景音樂。

### 功能特色

- **透明視窗**：只顯示寵物圖片，無邊框或背景
- **永遠置頂**：寵物始終顯示在所有視窗之上
- **可拖曳**：點擊並拖曳寵物到螢幕任意位置
- **動畫與靜態切換**：在 GIF 動畫和 PNG 靜態圖片之間切換
- **背景音樂**：顯示 GIF 動畫時播放音樂
- **靜音選項**：透過右鍵選單切換音效開關
- **自動切換模式**：每 3 秒自動在狀態間切換（預設啟用）
- **手動控制**：使用中鍵或右鍵選單切換狀態
- **支援打包**：可使用 PyInstaller 打包成獨立執行檔

### 系統需求

- Python 3.6 或更高版本
- PyQt5
- pygame

### 安裝

1. 如果尚未安裝 Python，請先安裝：https://www.python.org/downloads/

2. 安裝所需套件：
```bash
pip install -r requirements.txt
```

或手動安裝：
```bash
pip install PyQt5 pygame
```

### 設定

將以下檔案放入 `Images/` 資料夾：
- `OIIAIOIIIAI.gif` - 動畫 GIF（活躍狀態）
- `OIIAIOIIIAI_stop.png` - 靜態 PNG（閒置狀態）
- `music.mp3` - 背景音樂（支援 MP3、OGG、WAV 格式）

建議圖片大小：180x180 像素或更小

### 使用方式

執行應用程式：
```bash
python oiiaioiiiai.py
```

或打包成執行檔：
```bash
pyinstaller oiiaioiiiai.spec
```
執行檔將位於 `dist/oiiaioiiiai.exe`

### 操作控制

| 動作 | 說明 |
|-----|------|
| **左鍵拖曳** | 移動寵物到螢幕任意位置 |
| **中鍵點擊** | 手動切換動畫和靜態狀態 |
| **右鍵點擊** | 開啟右鍵選單 |

### 右鍵選單選項

- **切換狀態**：手動在 GIF 和 PNG 之間切換
- **自動切換模式**：啟用/停用自動切換功能
- **靜音**：切換音樂開關
- **退出**：關閉應用程式

### 音樂行為

- 顯示 GIF 動畫時自動播放音樂
- 切換到靜態 PNG 時停止音樂
- GIF 顯示期間音樂會無限循環播放
- 可透過右鍵選單靜音（靜音狀態在切換時保持）

### 檔案結構

```
專案根目錄/
├── oiiaioiiiai.py           # 主程式檔案
├── oiiaioiiiai.spec         # PyInstaller 設定檔
├── requirements.txt         # Python 相依套件
├── Images/                  # 資源資料夾
│   ├── OIIAIOIIIAI.gif     # 動畫寵物圖片
│   ├── OIIAIOIIIAI_stop.png # 靜態寵物圖片
│   ├── music.mp3           # 背景音樂
│   └── README.txt          # 資料夾說明
└── README.md               # 本說明檔
```

### 疑難排解

**音樂無法播放：**
- 確認 `music.mp3` 檔案存在於 `Images/` 資料夾中
- 檢查是否已啟用靜音（右鍵 → 取消勾選「靜音」）
- 確認檔案格式受支援（MP3、OGG、WAV）

**圖片無法顯示：**
- 確認圖片檔案存在於 `Images/` 資料夾中
- 檢查檔案是否有效且未損壞

---

**Enjoy your new desktop companion! / 享受您的新桌面夥伴！🐱🐶🐦**
