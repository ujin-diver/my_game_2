import random
import time

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(self.player)
        print(self.computer)
        print()

        round_num = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"--- Раунд {round_num} ---")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден!")
                break

            time.sleep(1)

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден!")
                break

            print(self.player)
            print(self.computer)
            print()
            time.sleep(1)
            round_num += 1

        winner = self.player.name if self.player.is_alive() else self.computer.name
        print(f"🎉 Победитель: {winner}!")

# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
