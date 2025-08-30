# Mouse to Morse Code Converter

A Python application that converts middle mouse button clicks into Morse code and automatically types the decoded text into any active text field.

## Features

- **Real-time Morse Code Input**: Use middle mouse button clicks to input Morse code
- **Automatic Text Output**: Decoded text appears directly in any active text field
- **Visual Feedback**: Console displays dots, dashes, and decoded characters in real-time
- **Smart Timing**: Distinguishes between dots (short clicks) and dashes (long clicks)
- **Word Spacing**: Automatically adds spaces between words based on timing gaps

## How It Works

- **Short middle mouse clicks** (< 0.3 seconds) = **Dots (.)**
- **Long middle mouse clicks** (≥ 0.3 seconds) = **Dashes (-)**
- **Character gaps**: 1 second pause converts accumulated Morse to a character
- **Word gaps**: 2.5 second pause adds a space between words

## Installation

1. Install the required dependency:
```bash
pip install pynput
```

2. Run the script:
```bash
python script.py
```

## Usage

1. Start the application by running the script
2. Click in any text field where you want the decoded text to appear
3. Use middle mouse button clicks to input Morse code:
   - Quick clicks for dots
   - Hold longer for dashes
4. Watch as your Morse code gets automatically converted to text
5. Press `Ctrl+C` to exit

## Supported Characters

The converter supports the full international Morse code alphabet:

- **Letters**: A-Z
- **Numbers**: 0-9

### Morse Code Reference

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

## Configuration

You can modify timing settings in the script:

```python
self.dot_dash_threshold = 0.3  # Short vs long click threshold
self.character_gap = 1.0       # Gap between characters
self.word_gap = 2.5            # Gap between words
```

## Requirements

- Python 3.6+
- `pynput` library
- Administrator/root privileges may be required for global mouse listening

## Troubleshooting

- **Permission errors**: Run as administrator (Windows) or with sudo (Linux/Mac)
- **Text not appearing**: Make sure you've clicked in an active text field
- **Import errors**: Install pynput with `pip install pynput`

## Example

Input sequence: Short click, long click, short click (. - .)
Output: "R"

## License

This project is open source and available under standard terms.