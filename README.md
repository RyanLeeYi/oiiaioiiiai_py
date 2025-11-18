# Desktop OIIAIOIIIAI Spinning Cat Application / 桌面旋轉貓咪應用程式 51121!!

<img width="300" height="400" alt="OIIAIOIIIAI_stop" src="https://github.com/user-attachments/assets/73b92e7c-f213-4585-b766-783d56ba4977" />

[English](#english) | [中文](#中文)

---

## English

A cute, transparent desktop pet that lives on your screen! This Python application creates a draggable, always-on-top window that displays animated GIF with background music.

### Features

- **Transparent Window**: Only the pet image is visible, no borders or background
- **Always On Top**: Pet stays visible above all other windows
- **Draggable**: Click and drag your pet anywhere on the screen
- **Two Independent Groups**: Each group has its own GIF, PNG, background music, and auto-switch timings
  - Group 1: GIF1 (2s) + PNG1 (1s) + Music1
  - Group 2: GIF2 (3s) + PNG2 (1.5s) + Music2
- **Flexible Switching**: Toggle between GIF/PNG within each group, or switch between groups
- **Group-Specific Music**: Different background music for each group's GIF animation
- **Independent Timings**: Each state (GIF/PNG) in each group has its own display duration
  - Customizable durations for GIF and PNG separately in each group
- **Mute Option**: Toggle sound on/off via context menu
- **Zoom Controls**: Resize the pet from 50% to 300% of original size
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

**Group 1:**
- `OIIAIOIIIAI.gif` - Group 1 animated GIF
- `OIIAIOIIIAI_stop.png` - Group 1 static PNG
- `oiia-oiia-sound.mp3` - Group 1 background music

**Group 2:**
- `OIIAIOIIIAI2.gif` - Group 2 animated GIF
- `OIIAIOIIIAI2_stop.png` - Group 2 static PNG
- `oiia-oiia-sound2.mp3` - Group 2 background music

Supported music formats: MP3, OGG, WAV

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

### Customizing Display Timings

You can customize how long each state displays by editing the timing variables in `oiiaioiiiai.py`:

```python
# Group 1 timings (in milliseconds)
self.group1_gif_duration = 2000   # 2 seconds for group 1 GIF
self.group1_png_duration = 1000   # 1 second for group 1 PNG

# Group 2 timings (in milliseconds)
self.group2_gif_duration = 3000   # 3 seconds for group 2 GIF
self.group2_png_duration = 1500   # 1.5 seconds for group 2 PNG
```

For example, to make Group 1 GIF display for 5 seconds, change:
```python
self.group1_gif_duration = 5000
```

### Controls

| Action | Description |
|--------|-------------|
| **Left Click + Drag** | Move the pet around your screen |
| **Middle Click** | Toggle between GIF and PNG within current group |
| **Right Click** | Open context menu |

### Context Menu Options

- **切換狀態 (Toggle State)**: Toggle between GIF and PNG within current group
- **組 1 (Group 1)**:
  - **顯示 GIF 1**: Display Group 1 animated GIF (with Music 1)
  - **顯示 PNG 1**: Display Group 1 static PNG
- **組 2 (Group 2)**:
  - **顯示 GIF 2**: Display Group 2 animated GIF (with Music 2)
  - **顯示 PNG 2**: Display Group 2 static PNG
- **自動切換模式 (Auto Switch Mode)**: Enable/disable automatic switching (toggles GIF/PNG within current group)
- **靜音 (Mute)**: Toggle music on/off
- **放大 (Zoom In)**: Increase size by 25% (up to 300%)
- **縮小 (Zoom Out)**: Decrease size by 25% (down to 50%)
- **重設大小 (Reset Zoom)**: Reset to original size (100%)
- **退出 (Exit)**: Close the application

### Music Behavior

- Each group has its own unique background music
- Music plays automatically when displaying a group's GIF animation
- Music stops when switching to PNG (within the same group)
- When switching between groups, the appropriate music loads and plays
- Music loops indefinitely while GIF is showing
- Can be muted via context menu (mute state persists across toggles)

### File Structure

```
project_root/
├── oiiaioiiiai.py           # Main application file
├── oiiaioiiiai.spec         # PyInstaller spec file
├── requirements.txt         # Python dependencies
├── Images/                  # Resource folder
│   ├── OIIAIOIIIAI.gif     # Group 1 animated GIF
│   ├── OIIAIOIIIAI_stop.png # Group 1 static PNG
│   ├── oiia-oiia-sound.mp3 # Group 1 background music
│   ├── OIIAIOIIIAI2.gif    # Group 2 animated GIF
│   ├── OIIAIOIIIAI2_stop.png # Group 2 static PNG
│   ├── oiia-oiia-sound2.mp3 # Group 2 background music
│   └── README.txt          # Image folder instructions
└── README.md               # This file
```

### Troubleshooting

**Music not playing:**
- Ensure `oiia-oiia-sound.mp3` exists in `Images/` folder
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
- **兩個獨立組別**：每組都有各自的 GIF、PNG、背景音樂和顯示時間
  - 組 1：GIF1 (2秒) + PNG1 (1秒) + 音樂1
  - 組 2：GIF2 (3秒) + PNG2 (1.5秒) + 音樂2
- **靈活切換**：可在各組內切換 GIF/PNG，或在組之間切換
- **分組專屬音樂**：每組的 GIF 動畫播放不同的背景音樂
- **獨立計時**：每組的每個狀態（GIF/PNG）都有各自的顯示時間
  - 可分別自訂每組的 GIF 和 PNG 顯示時長
- **靜音選項**：透過右鍵選單切換音效開關
- **縮放控制**：可將寵物大小調整為原始大小的 50% 至 300%
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

**組 1：**
- `OIIAIOIIIAI.gif` - 組 1 動畫 GIF
- `OIIAIOIIIAI_stop.png` - 組 1 靜態 PNG
- `oiia-oiia-sound.mp3` - 組 1 背景音樂

**組 2：**
- `OIIAIOIIIAI2.gif` - 組 2 動畫 GIF
- `OIIAIOIIIAI2_stop.png` - 組 2 靜態 PNG
- `oiia-oiia-sound2.mp3` - 組 2 背景音樂

支援的音樂格式：MP3、OGG、WAV

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

### 自訂顯示時間

您可以透過編輯 `oiiaioiiiai.py` 中的時間變數來自訂每個狀態的顯示時長：

```python
# 組 1 時間設定（以毫秒為單位）
self.group1_gif_duration = 2000   # 組 1 GIF 顯示 2 秒
self.group1_png_duration = 1000   # 組 1 PNG 顯示 1 秒

# 組 2 時間設定（以毫秒為單位）
self.group2_gif_duration = 3000   # 組 2 GIF 顯示 3 秒
self.group2_png_duration = 1500   # 組 2 PNG 顯示 1.5 秒
```

例如，要讓組 1 的 GIF 顯示 5 秒，修改為：
```python
self.group1_gif_duration = 5000
```

### 操作控制

| 動作 | 說明 |
|-----|------|
| **左鍵拖曳** | 移動寵物到螢幕任意位置 |
| **中鍵點擊** | 在當前組內切換 GIF 和 PNG |
| **右鍵點擊** | 開啟右鍵選單 |

### 右鍵選單選項

- **切換狀態**：在當前組內切換 GIF 和 PNG
- **組 1**：
  - **顯示 GIF 1**：顯示組 1 動畫 GIF（搭配音樂1）
  - **顯示 PNG 1**：顯示組 1 靜態 PNG
- **組 2**：
  - **顯示 GIF 2**：顯示組 2 動畫 GIF（搭配音樂2）
  - **顯示 PNG 2**：顯示組 2 靜態 PNG
- **自動切換模式**：啟用/停用自動切換（在當前組內切換 GIF/PNG）
- **靜音**：切換音樂開關
- **放大**：每次增加 25% 大小（最大 300%）
- **縮小**：每次減少 25% 大小（最小 50%）
- **重設大小**：恢復為原始大小（100%）
- **退出**：關閉應用程式

### 音樂行為

- 每組都有各自獨特的背景音樂
- 顯示組別的 GIF 動畫時自動播放該組音樂
- 在同一組內切換到 PNG 時停止音樂
- 在組之間切換時，會載入並播放對應的音樂
- GIF 顯示期間音樂會無限循環播放
- 可透過右鍵選單靜音（靜音狀態在切換時保持）

### 檔案結構

```
專案根目錄/
├── oiiaioiiiai.py           # 主程式檔案
├── oiiaioiiiai.spec         # PyInstaller 設定檔
├── requirements.txt         # Python 相依套件
├── Images/                  # 資源資料夾
│   ├── OIIAIOIIIAI.gif     # 組 1 動畫 GIF
│   ├── OIIAIOIIIAI_stop.png # 組 1 靜態 PNG
│   ├── oiia-oiia-sound.mp3 # 組 1 背景音樂
│   ├── OIIAIOIIIAI2.gif    # 組 2 動畫 GIF
│   ├── OIIAIOIIIAI2_stop.png # 組 2 靜態 PNG
│   ├── oiia-oiia-sound2.mp3 # 組 2 背景音樂
│   └── README.txt          # 資料夾說明
└── README.md               # 本說明檔
```

### 疑難排解

**音樂無法播放：**
- 確認 `oiia-oiia-sound.mp3` 檔案存在於 `Images/` 資料夾中
- 檢查是否已啟用靜音（右鍵 → 取消勾選「靜音」）
- 確認檔案格式受支援（MP3、OGG、WAV）

**圖片無法顯示：**
- 確認圖片檔案存在於 `Images/` 資料夾中
- 檢查檔案是否有效且未損壞

---

**Enjoy your new desktop companion! / 享受您的新桌面夥伴！🐱🐶🐦**
