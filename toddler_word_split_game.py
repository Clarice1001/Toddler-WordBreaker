import random
import subprocess
import tkinter as tk
from tkinter import font

WORDS = [
    {"word": "watermelon", "parts": ["wa", "ter", "me", "lon"]},
    {"word": "rainbow", "parts": ["rain", "bow"]},
    {"word": "cupcake", "parts": ["cup", "cake"]},
    {"word": "sunflower", "parts": ["sun", "flow", "er"]},
    {"word": "penguin", "parts": ["pen", "guin"]},
    {"word": "butterfly", "parts": ["but", "ter", "fly"]},
    {"word": "elephant", "parts": ["el", "e", "phant"]},
    {"word": "tomato", "parts": ["to", "ma", "to"]},
    {"word": "computer", "parts": ["com", "pu", "ter"]},
    {"word": "dinosaur", "parts": ["di", "no", "saur"]},
    {"word": "pineapple", "parts": ["pine", "ap", "ple"]},
    {"word": "chocolate", "parts": ["choc", "o", "late"]},
    {"word": "umbrella", "parts": ["um", "brell", "a"]},
    {"word": "strawberry", "parts": ["straw", "ber", "ry"]},
    {"word": "telephone", "parts": ["tel", "e", "phone"]},
    {"word": "kangaroo", "parts": ["kan", "ga", "roo"]},
    {"word": "avocado", "parts": ["a", "vo", "ca", "do"]},
    {"word": "banana", "parts": ["ba", "na", "na"]},
    {"word": "hippopotamus", "parts": ["hip", "po", "pot", "a", "mus"]},
    {"word": "alligator", "parts": ["al", "li", "ga", "tor"]},
    {"word": "caterpillar", "parts": ["cat", "er", "pil", "lar"]},
    {"word": "motorcycle", "parts": ["mo", "tor", "cy", "cle"]},
    {"word": "octopus", "parts": ["oc", "to", "pus"]},
    {"word": "giraffe", "parts": ["gi", "raffe"]},
    {"word": "notebook", "parts": ["note", "book"]},
    {"word": "jellybean", "parts": ["jel", "ly", "bean"]},
    {"word": "sandwich", "parts": ["sand", "wich"]},
    {"word": "playground", "parts": ["play", "ground"]},
    {"word": "birthday", "parts": ["birth", "day"]},
    {"word": "sunshine", "parts": ["sun", "shine"]},
    {"word": "balloon", "parts": ["bal", "loon"]},
    {"word": "mountain", "parts": ["moun", "tain"]},
    {"word": "painting", "parts": ["paint", "ing"]},
    {"word": "cookie", "parts": ["coo", "kie"]},
    {"word": "glasses", "parts": ["glass", "es"]},
    {"word": "policeman", "parts": ["po", "li", "ce", "man"]},
    {"word": "hospital", "parts": ["hos", "pi", "tal"]},
    {"word": "adventure", "parts": ["ad", "ven", "ture"]},
    {"word": "icecream", "parts": ["ice", "cream"]},
    {"word": "firefly", "parts": ["fire", "fly"]},
    {"word": "beehive", "parts": ["bee", "hive"]},
    {"word": "seaside", "parts": ["sea", "side"]},
    {"word": "dragonfly", "parts": ["drag", "on", "fly"]},
    {"word": "blueberry", "parts": ["blue", "ber", "ry"]},
    {"word": "pancake", "parts": ["pan", "cake"]},
    {"word": "mailbox", "parts": ["mail", "box"]},
    {"word": "treasure", "parts": ["trea", "sure"]},
    {"word": "snowflake", "parts": ["snow", "flake"]},
    {"word": "keyboard", "parts": ["key", "board"]},
    {"word": "popcorn", "parts": ["pop", "corn"]},
    {"word": "dolphin", "parts": ["dol", "phin"]},
    {"word": "toothbrush", "parts": ["tooth", "brush"]},
    {"word": "ladybug", "parts": ["la", "dy", "bug"]},
    {"word": "firetruck", "parts": ["fire", "truck"]},
    {"word": "schoolbus", "parts": ["school", "bus"]},
    {"word": "skateboard", "parts": ["skate", "board"]},
    {"word": "spaceship", "parts": ["space", "ship"]},
    {"word": "headphone", "parts": ["head", "phone"]},
    {"word": "wallpaper", "parts": ["wall", "pa", "per"]},
    {"word": "baseball", "parts": ["base", "ball"]},
    {"word": "football", "parts": ["foot", "ball"]},
    {"word": "jellyfish", "parts": ["jel", "ly", "fish"]},
    {"word": "backpack", "parts": ["back", "pack"]},
    {"word": "raincoat", "parts": ["rain", "coat"]},
    {"word": "sandcastle", "parts": ["sand", "ca", "stle"]},
    {"word": "cupboard", "parts": ["cup", "board"]},
    {"word": "goldfish", "parts": ["gold", "fish"]},
    {"word": "moonlight", "parts": ["moon", "light"]},
    {"word": "rainstorm", "parts": ["rain", "storm"]},
    {"word": "playtime", "parts": ["play", "time"]},
    {"word": "giftbox", "parts": ["gift", "box"]},
    {"word": "snowman", "parts": ["snow", "man"]},
    {"word": "hotdog", "parts": ["hot", "dog"]},
    {"word": "cowboy", "parts": ["cow", "boy"]},
    {"word": "seahorse", "parts": ["sea", "horse"]},
    {"word": "puzzle", "parts": ["puz", "zle"]},
    {"word": "cookies", "parts": ["coo", "kies"]},
    {"word": "sunglasses", "parts": ["sun", "glass", "es"]},
    {"word": "armchair", "parts": ["arm", "chair"]},
    {"word": "honeybee", "parts": ["hon", "ey", "bee"]},
    {"word": "peacock", "parts": ["pea", "cock"]},
    {"word": "fireplace", "parts": ["fire", "place"]},
    {"word": "buttercup", "parts": ["but", "ter", "cup"]},
    {"word": "moonbeam", "parts": ["moon", "beam"]},
    {"word": "starlight", "parts": ["star", "light"]},
    {"word": "rainforest", "parts": ["rain", "forest"]},
    {"word": "honeycomb", "parts": ["hon", "ey", "comb"]},
    {"word": "ballroom", "parts": ["ball", "room"]},
    {"word": "storybook", "parts": ["sto", "ry", "book"]},
    {"word": "whisper", "parts": ["whi", "sper"]},
    {"word": "daisy", "parts": ["dai", "sy"]},
    {"word": "planet", "parts": ["plan", "et"]},
    {"word": "pajamas", "parts": ["pa", "ja", "mas"]},
    {"word": "marshmallow", "parts": ["marsh", "mal", "low"]},
    {"word": "seashell", "parts": ["sea", "shell"]},
    {"word": "riverbank", "parts": ["ri", "ver", "bank"]},
    {"word": "hammock", "parts": ["ham", "mock"]},
    {"word": "carousel", "parts": ["car", "ou", "sel"]},
    {"word": "fireman", "parts": ["fire", "man"]},
    {"word": "lighthouse", "parts": ["light", "house"]},
]


class WordSplitGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Toddler Word Splitter")
        self.root.geometry("740x520")
        self.root.resizable(False, False)

        self.header_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.large_font = font.Font(family="Helvetica", size=18)
        self.button_font = font.Font(family="Helvetica", size=16)

        self.word_index = 0
        self.chosen_parts = []
        self.part_buttons = []
        self.selected_buttons = []
        self.sound_enabled = True
        self.speech_process = None
        self.bg_colors = [
            "#FDEBD0",
            "#D6EAF8",
            "#D5F5E3",
            "#FADBD8",
            "#E8DAEF",
            "#FCF3CF",
            "#D1F2EB",
            "#F9E79F",
        ]

        self.create_widgets()
        self.load_word()
        self.speak("Hello! Let's learn to split words together. Tap the pieces in the right order.")

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root,
            text="Break the word into smaller sounds",
            font=self.header_font,
            fg="#2F4F4F",
            wraplength=720,
            justify="center",
        )
        self.title_label.pack(pady=(20, 10))

        self.word_label = tk.Label(self.root, text="", font=self.large_font, fg="#004d99")
        self.word_label.pack(pady=(0, 8))

        self.instruction_label = tk.Label(
            self.root,
            text="Tap the parts in the right order.",
            font=self.large_font,
            fg="#555555",
        )
        self.instruction_label.pack(pady=(0, 12))

        self.answer_label = tk.Label(
            self.root,
            text="Answer:",
            font=self.large_font,
            fg="#333333",
            wraplength=720,
            justify="center",
        )
        self.answer_label.pack(pady=(0, 8))

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=(0, 12))

        self.message_label = tk.Label(self.root, text="", font=self.large_font, fg="#006600")
        self.message_label.pack(pady=(0, 12))

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=(0, 12))

        self.reset_button = tk.Button(
            self.controls_frame,
            text="Reset",
            font=self.button_font,
            width=10,
            command=self.reset_selection,
            bg="#FFD700",
        )
        self.reset_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(
            self.controls_frame,
            text="Next Word",
            font=self.button_font,
            width=12,
            command=self.next_word,
            bg="#D3D3D3",
            state="disabled",
        )
        self.next_button.grid(row=0, column=1, padx=10)

        self.repeat_button = tk.Button(
            self.controls_frame,
            text="Repeat Prompt",
            font=self.button_font,
            width=12,
            command=self.repeat_word,
            bg="#FFA07A",
        )
        self.repeat_button.grid(row=0, column=2, padx=10)

        self.say_button = tk.Button(
            self.controls_frame,
            text="Say Word",
            font=self.button_font,
            width=9,
            command=self.say_word,
            bg="#FFDAB9",
        )
        self.say_button.grid(row=0, column=3, padx=8)

        self.sound_canvas = tk.Canvas(
            self.controls_frame,
            width=70,
            height=34,
            bg=self.controls_frame.cget("bg"),
            highlightthickness=0,
        )
        self.sound_canvas.grid(row=0, column=4, padx=8)
        self.sound_canvas.bind("<Button-1>", lambda event: self.toggle_speech())
        self.sound_disabled = False
        self._draw_sound_switch()

        self.help_label = tk.Label(
            self.root,
            text="If sound does not work, install pyttsx3 and restart the game.",
            font=font.Font(family="Helvetica", size=12),
            fg="#666666",
            wraplength=720,
            justify="center",
        )
        self.help_label.pack(pady=(0, 8))

    def can_speak(self):
        try:
            import pyttsx3
            return True
        except Exception:
            return False

    def disable_audio(self):
        self.sound_enabled = False
        self.sound_disabled = True
        self._draw_sound_switch()
        self.stop_speech()

    def stop_speech(self):
        if self.speech_process is not None:
            try:
                self.speech_process.terminate()
                self.speech_process.wait(timeout=1)
            except Exception:
                pass
            self.speech_process = None

    def speak(self, text):
        if not self.sound_enabled:
            return
        self.stop_speech()
        try:
            safe_text = text.replace("'", "''")
            cmd = [
                "powershell",
                "-NoProfile",
                "-Command",
                f"Add-Type -AssemblyName System.Speech; $s = New-Object System.Speech.Synthesis.SpeechSynthesizer; $s.Speak('{safe_text}')",
            ]
            self.speech_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            try:
                import pyttsx3
                engine = pyttsx3.init()
                voices = engine.getProperty("voices")
                if voices:
                    engine.setProperty("voice", voices[0].id)
                engine.say(text)
                engine.runAndWait()
                engine.stop()
            except Exception:
                self.disable_audio()

    def toggle_speech(self):
        if self.sound_disabled:
            return
        self.sound_enabled = not self.sound_enabled
        self._draw_sound_switch()
        if self.sound_enabled:
            self.speak("Sound is on. Tap the pieces in the right order.")

    def _draw_sound_switch(self):
        self.sound_canvas.delete("all")
        if self.sound_disabled:
            track_color = "#D3D3D3"
            knob_x = 8
        elif self.sound_enabled:
            track_color = "#4CAF50"
            knob_x = 38
        else:
            track_color = "#F44336"
            knob_x = 8

        self.sound_canvas.create_oval(4, 8, 24, 28, fill=track_color, outline=track_color)
        self.sound_canvas.create_oval(46, 8, 66, 28, fill=track_color, outline=track_color)
        self.sound_canvas.create_rectangle(14, 8, 56, 28, fill=track_color, outline=track_color)
        self.sound_canvas.create_oval(knob_x, 6, knob_x + 24, 30, fill="white", outline="#BBBBBB")

    def repeat_word(self):
        displayed_word = self.current_word["word"].title()
        self.speak(f"The word is {displayed_word}. Tap its parts in the right order.")

    def say_word(self):
        displayed_word = self.current_word["word"].title()
        self.speak(displayed_word)

    def load_word(self):
        self.current_word = WORDS[self.word_index]
        self.target_parts = list(self.current_word["parts"])
        self.chosen_parts = []
        self.message_label.config(text="", fg="#006600")
        self.update_next_button_state(False)

        displayed_word = self.current_word["word"].title()
        self.word_label.config(text=displayed_word)
        self.update_answer_label()

        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        self.buttons_frame.update_idletasks()

        parts = list(self.target_parts)
        random.shuffle(parts)

        self.part_buttons = []
        self.selected_buttons = []
        for index, part in enumerate(parts):
            btn = tk.Button(
                self.buttons_frame,
                text=part,
                font=self.button_font,
                width=10,
                height=2,
                bg="#ADD8E6",
            )
            btn.config(command=self.make_choice_command(part, btn))
            btn.grid(row=index // 4, column=index % 4, padx=8, pady=8)
            self.part_buttons.append(btn)

        bg_color = self.bg_colors[self.word_index % len(self.bg_colors)]
        self.root.config(bg=bg_color)
        self.title_label.config(bg=bg_color)
        self.word_label.config(bg=bg_color)
        self.instruction_label.config(bg=bg_color)
        self.answer_label.config(bg=bg_color)
        self.buttons_frame.config(bg=bg_color)
        self.message_label.config(bg=bg_color)
        self.controls_frame.config(bg=bg_color)
        self.help_label.config(bg=bg_color)
        self.root.update_idletasks()
        self.speak(f"The word is {displayed_word}. Tap its parts in the right order.")

    def update_answer_label(self):
        answer_text = " ".join(self.chosen_parts)
        if answer_text == "":
            answer_text = "Tap pieces here"
        self.answer_label.config(text=f"Answer: {answer_text}")

    def make_choice_command(self, part, button):
        return lambda: self.choose_part(part, button)

    def choose_part(self, part, button):
        if button in self.selected_buttons:
            return
        self.selected_buttons.append(button)
        self.chosen_parts.append(part)
        self.update_answer_label()
        self.update_button_states()

        if len(self.chosen_parts) == len(self.target_parts):
            self.check_answer()

    def update_button_states(self):
        for btn in self.part_buttons:
            if btn in self.selected_buttons:
                btn.config(state="disabled", bg="#D3D3D3")
            else:
                btn.config(state="normal", bg="#ADD8E6")

    def update_next_button_state(self, enabled):
        if enabled:
            self.next_button.config(state="normal", bg="#90EE90")
        else:
            self.next_button.config(state="disabled", bg="#D3D3D3")

    def check_answer(self):
        if self.chosen_parts == self.target_parts:
            self.message_label.config(text="Great job! You split it perfectly.", fg="#006600")
            self.speak("Great job! You split it perfectly.")
            self.update_next_button_state(True)
        else:
            self.message_label.config(text="Oops, try again. Use Reset and try the right order.", fg="#CC0000")
            self.speak("Oops, try again. Reset and try the right order.")
            self.update_next_button_state(False)

    def reset_selection(self):
        self.chosen_parts = []
        self.selected_buttons = []
        self.update_answer_label()
        self.message_label.config(text="", fg="#006600")
        self.update_button_states()
        self.update_next_button_state(False)

    def next_word(self):
        self.stop_speech()
        self.word_index = (self.word_index + 1) % len(WORDS)
        self.load_word()


if __name__ == "__main__":
    root = tk.Tk()
    game = WordSplitGame(root)
    root.mainloop()
