import time
import threading
from pynput import mouse, keyboard
from pynput.keyboard import Controller as KeyboardController
import sys

class MouseToMorseConverter:
    def __init__(self):
        # Morse Code Dictionary
        self.morse_to_char = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9', '-----': '0'
        }
        
        # Timing configuration (in seconds)
        self.dot_dash_threshold = 0.3  # Short click = dot, long click = dash
        self.character_gap = 1.0       # Gap between characters
        self.word_gap = 2.5            # Gap between words
        
        # State variables
        self.current_morse = ''
        self.last_click_time = 0
        self.click_start_time = 0
        self.is_clicking = False
        
        # Keyboard controller for text input
        self.keyboard_controller = KeyboardController()
        
        # Timer for character conversion
        self.conversion_timer = None
        self.running = True
        
        print("🎯 Mouse to Morse Code Converter Started!")
        print("📝 Instructions:")
        print("   • Quick middle mouse clicks = dots (.)")
        print("   • Long middle mouse clicks = dashes (-)")
        print("   • Text will appear in any active text field")
        print("   • Press Ctrl+C to exit")
        print("⚡ Ready for input...\n")

    def on_scroll_click_down(self):
        """Handle mouse scroll button press down"""
        if not self.is_clicking:
            self.is_clicking = True
            self.click_start_time = time.time()

    def on_scroll_click_up(self):
        """Handle mouse scroll button release"""
        if self.is_clicking:
            self.is_clicking = False
            click_duration = time.time() - self.click_start_time
            
            # Determine dot or dash based on click duration
            if click_duration < self.dot_dash_threshold:
                self.current_morse += '.'
                print('.', end='', flush=True)
            else:
                self.current_morse += '-'
                print('-', end='', flush=True)
            
            self.last_click_time = time.time()
            self.reset_conversion_timer()

    def on_click(self, x, y, button, pressed):
        """Global mouse click event handler"""
        if button == mouse.Button.middle:  # Middle mouse button only
            if pressed:
                self.on_scroll_click_down()
            else:
                self.on_scroll_click_up()

    def on_key_press(self, key):
        """Handle keyboard events for exit condition"""
        try:
            # Exit on Ctrl+C
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                return True
        except AttributeError:
            if hasattr(key, 'char') and key.char == 'c':
                # Check if Ctrl is being held
                return True

    def reset_conversion_timer(self):
        """Reset the timer for character conversion"""
        if self.conversion_timer:
            self.conversion_timer.cancel()
        
        self.conversion_timer = threading.Timer(self.character_gap, self.process_morse)
        self.conversion_timer.start()

    def process_morse(self):
        """Convert accumulated Morse code to character and insert"""
        if self.current_morse:
            current_time = time.time()
            
            # Add word space for longer gaps
            if current_time - self.last_click_time > self.word_gap:
                self.insert_text(' ')
                print(' [SPACE]', end='')
            
            # Convert Morse to character
            character = self.morse_to_char.get(self.current_morse, '')
            if character:
                self.insert_text(character)
                print(f' → {character}')
            else:
                print(f' → [?] (Unknown: {self.current_morse})')
            
            # Reset for next character
            self.current_morse = ''

    def insert_text(self, text):
        """Insert text into currently active text field"""
        try:
            # Small delay to ensure text field is ready
            time.sleep(0.01)
            self.keyboard_controller.type(text)
        except Exception as e:
            print(f"\n❌ Error inserting text: {e}")

    def start_listening(self):
        """Start the global mouse and keyboard listeners"""
        try:
            print("🔊 Listening for mouse scroll button clicks...")
            print("💡 Click in any text field and use middle mouse button\n")
            
            # Start mouse listener
            mouse_listener = mouse.Listener(on_click=self.on_click)
            mouse_listener.start()
            
            # Keep the program running
            try:
                while self.running:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("\n\n🛑 Converter stopped by user (Ctrl+C)")
                self.running = False
                
        except Exception as e:
            print(f"❌ Error starting listeners: {e}")
        finally:
            if self.conversion_timer:
                self.conversion_timer.cancel()
            print("✅ Cleanup complete")

def main():
    """Main function to start the converter"""
    try:
        converter = MouseToMorseConverter()
        converter.start_listening()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Failed to start converter: {e}")
        print("\n📦 Make sure you have installed the required package:")
        print("   pip install pynput")
        print("\n🔧 Run as administrator if you encounter permission issues")

if __name__ == "__main__":
    main()
NoneIGGA