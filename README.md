# 🖱️ Mouse to Morse Code Converter

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

> Transform your mouse clicks into Morse code and watch it magically appear as text! 🎯

A Python application that converts middle mouse button clicks into Morse code and automatically types the decoded text into any active text field.

## ✨ Features

- 🖱️ **Real-time Morse Code Input**: Use middle mouse button clicks to input Morse code
- ⌨️ **Automatic Text Output**: Decoded text appears directly in any active text field
- 👀 **Visual Feedback**: Console displays dots, dashes, and decoded characters in real-time
- ⏱️ **Smart Timing**: Distinguishes between dots (short clicks) and dashes (long clicks)
- 📝 **Word Spacing**: Automatically adds spaces between words based on timing gaps
- 🌐 **Cross-platform**: Works on Windows, macOS, and Linux

## 🔧 How It Works

| Action | Result | Timing |
|--------|--------|--------|
| 🖱️ **Short click** | Dot (.) | < 0.3 seconds |
| 🖱️ **Long click** | Dash (-) | ≥ 0.3 seconds |
| ⏸️ **Short pause** | Convert to character | 1 second |
| ⏸️ **Long pause** | Add word space | 2.5 seconds |

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Administrator/root privileges (for global mouse listening)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mouse-to-morse.git
   cd mouse-to-morse
   ```

2. **Install dependencies**
   ```bash
   pip install pynput
   ```

3. **Run the application**
   ```bash
   python script.py
   ```

### Alternative: One-line install
```bash
pip install pynput && python script.py
```

## 📖 Usage

1. **Start the application**
   ```bash
   python script.py
   ```

2. **Position your cursor** in any text field (browser, notepad, etc.)

3. **Input Morse code** using middle mouse button:
   - 🔘 **Quick clicks** → dots (.)
   - 🔘 **Long clicks** → dashes (-)

4. **Watch the magic** ✨ as your Morse code converts to text automatically

5. **Exit** with `Ctrl+C`

### 🎬 Demo
```
Input:  . - .     (short-long-short clicks)
Output: R

Input:  ... --- ...     (SOS)
Output: SOS
```

## 📚 Supported Characters

The converter supports the full international Morse code alphabet:
- 🔤 **Letters**: A-Z (26 characters)
- 🔢 **Numbers**: 0-9 (10 digits)

<details>
<summary>📋 <strong>Click to view Morse Code Reference</strong></summary>

### Letters & Numbers

| Letter | Code | Letter | Code | Number | Code |
|--------|------|--------|------|--------|------|
| A | .-   | N | -.   | 1 | .---- |
| B | -... | O | ---  | 2 | ..--- |
| C | -.-. | P | .--. | 3 | ...-- |
| D | -..  | Q | --.- | 4 | ....- |
| E | .    | R | .-.  | 5 | ..... |
| F | ..-. | S | ...  | 6 | -.... |
| G | --.  | T | -    | 7 | --... |
| H | .... | U | ..-  | 8 | ---.. |
| I | ..   | V | ...- | 9 | ----. |
| J | .--- | W | .--  | 0 | ----- |
| K | -.-  | X | -..- |   |       |
| L | .-.. | Y | -.-- |   |       |
| M | --   | Z | --.. |   |       |

</details>

## ⚙️ Configuration

Customize timing settings by editing these values in `script.py`:

```python
# Timing configuration (in seconds)
self.dot_dash_threshold = 0.3  # Short vs long click threshold
self.character_gap = 1.0       # Gap between characters  
self.word_gap = 2.5            # Gap between words
```

| Setting | Default | Description |
|---------|---------|-------------|
| `dot_dash_threshold` | 0.3s | Click duration to distinguish dots from dashes |
| `character_gap` | 1.0s | Pause before converting Morse to character |
| `word_gap` | 2.5s | Pause before adding word space |

## 📋 Requirements

| Component | Version | Purpose |
|-----------|---------|---------|
| 🐍 Python | 3.6+ | Runtime environment |
| 📦 pynput | Latest | Mouse/keyboard input handling |
| 🔐 Admin rights | - | Global mouse event capture |

## 🔧 Troubleshooting

<details>
<summary><strong>Common Issues & Solutions</strong></summary>

| Problem | Solution |
|---------|----------|
| 🚫 **Permission errors** | Run as administrator (Windows) or with `sudo` (Linux/Mac) |
| 📝 **Text not appearing** | Ensure you've clicked in an active text field first |
| 📦 **Import errors** | Install pynput: `pip install pynput` |
| 🖱️ **Mouse not detected** | Check if middle mouse button is working in other apps |
| ⏱️ **Timing issues** | Adjust timing values in configuration section |

### Platform-specific notes:
- **Windows**: May require "Run as Administrator"
- **macOS**: Grant accessibility permissions in System Preferences
- **Linux**: May need `sudo` or add user to input group

</details>

## 🎯 Examples

### Basic Usage
```
Mouse Input: [short] [long] [short]
Morse Code:  .       -      .
Output:      R
```

### Complete Word
```
Mouse Input: [short-short-short] [pause] [long-long-long] [pause] [short-short-short]
Morse Code:  ...                         ---                     ...
Output:      SOS
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features  
- 🔧 Submit pull requests
- 📖 Improve documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a star! ⭐

---

<div align="center">
  <strong>Happy Morse coding! 📡</strong>
</div>