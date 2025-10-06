#!/usr/bin/env python3
"""
Silent Piece - A quiet forest walking game
A peaceful game where you walk through the forest and encounter surprises.
"""

import random
import time
import sys


class ForestGame:
    def __init__(self):
        self.player_position = 0
        self.forest_length = 20
        self.game_running = True
        self.surprises = [
            "Anda menemukan burung cantik di pohon! 🐦",
            "Suara angin sepoi-sepoi menenangkan... 🍃",
            "Anda menemukan bunga liar yang indah! 🌸",
            "Tupai berlari melewati jalur Anda! 🐿️",
            "Anda mendengar suara sungai di kejauhan... 💧",
            "Kupu-kupu berwarna-warni terbang di sekitar Anda! 🦋",
            "Anda menemukan batu yang unik! 🪨",
            "Cahaya matahari menembus dedaunan dengan indah... ☀️",
            "Anda menemukan jamur yang tumbuh di pohon tua! 🍄",
            "Burung hantu terlihat bertengger di pohon tinggi! 🦉"
        ]
    
    def print_slow(self, text, delay=0.03):
        """Print text with a slow typing effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def display_forest(self):
        """Display the current forest view"""
        print("\n" + "=" * 50)
        forest = ["🌲"] * self.forest_length
        forest[self.player_position] = "🚶"
        print(" ".join(forest))
        print("=" * 50)
        print(f"Posisi: {self.player_position + 1}/{self.forest_length}")
    
    def check_surprise(self):
        """Randomly trigger a surprise event"""
        if random.random() < 0.4:  # 40% chance of surprise
            surprise = random.choice(self.surprises)
            print("\n✨ Kejutan! ✨")
            self.print_slow(surprise)
            time.sleep(1)
    
    def walk(self):
        """Move forward in the forest"""
        if self.player_position < self.forest_length - 1:
            self.player_position += 1
            print("\nAnda berjalan maju...")
            time.sleep(0.5)
            self.check_surprise()
        else:
            print("\n🎉 Selamat! Anda telah mencapai akhir hutan!")
            self.game_running = False
    
    def rest(self):
        """Take a rest"""
        print("\nAnda beristirahat sejenak...")
        self.print_slow("Anda mendengarkan suara alam di sekitar...")
        time.sleep(1)
        self.check_surprise()
    
    def look_around(self):
        """Look around the current position"""
        print("\nAnda melihat sekeliling...")
        descriptions = [
            "Pohon-pohon tinggi mengelilingi Anda.",
            "Dedaunan bergoyang lembut tertiup angin.",
            "Cahaya redup menembus celah pepohonan.",
            "Jalur tanah tertutup daun-daun kering.",
            "Suasana tenang dan damai."
        ]
        self.print_slow(random.choice(descriptions))
        time.sleep(0.5)
        self.check_surprise()
    
    def show_menu(self):
        """Display the game menu"""
        print("\n--- Apa yang ingin Anda lakukan? ---")
        print("1. Berjalan maju")
        print("2. Istirahat")
        print("3. Lihat sekeliling")
        print("4. Keluar dari hutan")
        print("-----------------------------------")
    
    def start(self):
        """Start the game"""
        print("\n" + "=" * 50)
        self.print_slow("🌲 Selamat datang di Silent Piece 🌲", 0.05)
        self.print_slow("Game tenang di hutan yang penuh kejutan", 0.05)
        print("=" * 50)
        time.sleep(1)
        
        print("\nAnda berdiri di pinggir hutan yang tenang...")
        self.print_slow("Mari berjalan-jalan dan menikmati keindahan alam.")
        time.sleep(1)
        
        while self.game_running:
            self.display_forest()
            self.show_menu()
            
            try:
                choice = input("\nPilih aksi (1-4): ").strip()
                
                if choice == "1":
                    self.walk()
                elif choice == "2":
                    self.rest()
                elif choice == "3":
                    self.look_around()
                elif choice == "4":
                    print("\nAnda meninggalkan hutan...")
                    self.print_slow("Terima kasih telah bermain Silent Piece! 👋")
                    self.game_running = False
                else:
                    print("\nPilihan tidak valid. Silakan pilih 1-4.")
            
            except KeyboardInterrupt:
                print("\n\nAnda meninggalkan hutan...")
                self.print_slow("Terima kasih telah bermain Silent Piece! 👋")
                self.game_running = False
                break
        
        print("\n" + "=" * 50)


def main():
    """Main entry point"""
    game = ForestGame()
    game.start()


if __name__ == "__main__":
    main()
