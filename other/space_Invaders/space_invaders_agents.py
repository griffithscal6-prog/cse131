import tkinter as tk
import random

WIDTH, HEIGHT = 600, 700


class ProjectileAgent:
    def __init__(self, x, y, speed, enemy=False):
        self.x, self.y, self.speed, self.enemy = x, y, speed, enemy

    def update(self):
        self.y += self.speed

    def hits(self, target, width, height):
        return abs(self.x - target.x) < width and abs(self.y - target.y) < height

    def draw(self, canvas):
        color = "#ff6464" if self.enemy else "#65f4ff"
        canvas.create_rectangle(self.x - 3, self.y - 9, self.x + 3, self.y + 9,
                                fill=color, outline="", tags="game")


class PlayerAgent:
    SPRITE = (
        "000010000",
        "000111000",
        "001111100",
        "011111110",
        "111111111",
        "110101011",
        "100000001",
    )

    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT - 55
        self.cooldown = 0
        self.lives = 3

    def act(self, keys):
        if "left" in keys or "a" in keys:
            self.x -= 6
        if "right" in keys or "d" in keys:
            self.x += 6
        self.x = max(25, min(WIDTH - 25, self.x))

        self.cooldown = max(0, self.cooldown - 1)
        if "space" in keys and self.cooldown == 0:
            self.cooldown = 13
            return ProjectileAgent(self.x, self.y - 22, -11)
        return None

    def draw(self, canvas):
        pixel = 6
        for row, line in enumerate(self.SPRITE):
            for col, cell in enumerate(line):
                if cell == "1":
                    x, y = self.x - 27 + col * pixel, self.y - 21 + row * pixel
                    canvas.create_rectangle(x, y, x + pixel, y + pixel,
                                            fill="#69e88b", outline="",
                                            tags="game")
        canvas.create_rectangle(self.x - 3, self.y - 9, self.x + 3, self.y - 3,
                                fill="#65f4ff", outline="", tags="game")
        for x in (self.x - 15, self.x + 9):
            canvas.create_rectangle(x, self.y + 21, x + 6, self.y + 27,
                                    fill="#ffad42", outline="", tags="game")


class InvaderAgent:
    SPRITE = (
        "00100100",
        "00011000",
        "00111100",
        "01101110",
        "11111111",
        "10100101",
        "00100100",
        "01000010",
    )

    def __init__(self, x, y):
        self.x, self.y = x, y

    def act(self, dx, drop):
        self.x += dx
        self.y += drop

    def shoot(self):
        return ProjectileAgent(self.x, self.y + 15, 5, enemy=True)

    def draw(self, canvas):
        pixel = 4
        for row, line in enumerate(self.SPRITE):
            for col, cell in enumerate(line):
                if cell == "1":
                    x, y = self.x - 16 + col * pixel, self.y - 16 + row * pixel
                    canvas.create_rectangle(x, y, x + pixel, y + pixel,
                                            fill="#9cff57", outline="",
                                            tags="game")


class ShieldAgent:
    SHAPE = (
        "00111111111100",
        "01111111111110",
        "11111111111111",
        "11111111111111",
        "11111111111111",
        "11111111111111",
        "11110000001111",
        "11100000000111",
    )

    def __init__(self, x, y, scale):
        self.x, self.y, self.scale = x, y, scale
        self.cell = 4 * scale
        self.blocks = {(col, row) for row, line in enumerate(self.SHAPE)
                       for col, cell in enumerate(line) if cell == "1"}

    def absorb(self, bullet):
        for col, row in self.blocks:
            left = self.x + col * self.cell
            top = self.y + row * self.cell
            if (bullet.x + 3 >= left and bullet.x - 3 <= left + self.cell
                    and bullet.y + 9 >= top and bullet.y - 9 <= top + self.cell):
                # Remove a small patch around the impact to leave a crater.
                crater = {(col + dx, row + dy)
                          for dx in (-1, 0, 1) for dy in (-1, 0, 1)}
                self.blocks.difference_update(crater)
                return True
        return False

    def shrink(self):
        center_x = self.x + 7 * self.cell
        center_y = self.y + 4 * self.cell
        self.cell *= 0.995
        self.scale *= 0.995
        self.x = center_x - 7 * self.cell
        self.y = center_y - 4 * self.cell

    def draw(self, canvas):
        for col, row in self.blocks:
            left = self.x + col * self.cell
            top = self.y + row * self.cell
            canvas.create_rectangle(left, top, left + self.cell, top + self.cell,
                                    fill="#52e878", outline="", tags="game")


class GameAgent:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                                bg="#080d24", highlightthickness=0)
        self.canvas.pack()
        self.canvas.focus_set()
        self.keys = set()
        root.bind("<KeyPress>", self.key_down)
        root.bind("<KeyRelease>", self.key_up)
        self.reset()
        self.draw_stars()
        self.tick()

    def reset(self):
        self.player = PlayerAgent()
        self.invaders = [InvaderAgent(65 + col * 62, 75 + row * 48)
                         for row in range(4) for col in range(8)]
        self.bullets = []
        self.direction, self.speed = 1, 1.5
        self.score, self.wave = 0, 1
        self.shields = []
        self.make_shields()
        self.game_over = False
        self.won = False
        self.keys.clear()

    def make_shields(self):
        count = self.wave // 5
        scale = 0.995 ** (self.wave - 1)
        for shield in self.shields:
            shield.shrink()
        self.shields.extend(ShieldAgent(0, HEIGHT - 155, scale)
                            for _ in range(count - len(self.shields)))
        if count:
            width = 14 * 4 * scale
            gap = (WIDTH - count * width) / (count + 1)
            for i, shield in enumerate(self.shields):
                shield.x = gap + i * (width + gap)
                shield.y = HEIGHT - 155

    def draw_stars(self):
        for _ in range(75):
            x, y = random.randint(2, WIDTH - 2), random.randint(2, HEIGHT - 2)
            r = random.choice((1, 1, 2))
            self.canvas.create_oval(x, y, x + r, y + r, fill="#536080",
                                    outline="", tags="background")

    def key_down(self, event):
        key = event.keysym.lower() if event.keysym != "space" else "space"
        self.keys.add(key)
        if self.game_over and key == "r":
            self.reset()

    def key_up(self, event):
        key = event.keysym.lower() if event.keysym != "space" else "space"
        self.keys.discard(key)

    def update(self):
        if self.game_over:
            return

        shot = self.player.act(self.keys)
        if shot:
            self.bullets.append(shot)

        dx, drop = self.direction * self.speed, 0
        if any(alien.x + dx < 20 or alien.x + dx > WIDTH - 20
               for alien in self.invaders):
            self.direction *= -1
            dx, drop = self.direction * self.speed, 18
        for alien in self.invaders:
            alien.act(dx, drop)

        # The invader group occasionally chooses one member to fire.
        if self.invaders and random.random() < 0.025:
            self.bullets.append(random.choice(self.invaders).shoot())

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.y < 0 or bullet.y > HEIGHT:
                self.bullets.remove(bullet)
                continue

            if any(shield.absorb(bullet) for shield in self.shields):
                self.bullets.remove(bullet)
                continue

            if bullet.enemy:
                if bullet.hits(self.player, 23, 22):
                    self.bullets.remove(bullet)
                    self.player.lives -= 1
                    if self.player.lives <= 0:
                        self.game_over = True
            else:
                hit = next((a for a in self.invaders
                            if bullet.hits(a, 18, 15)), None)
                if hit:
                    self.invaders.remove(hit)
                    self.bullets.remove(bullet)
                    self.score += 10

        if any(a.y > self.player.y - 30 for a in self.invaders):
            self.game_over = True
        if not self.game_over and not self.invaders:
            self.wave += 1
            self.speed *= 1.10
            self.make_shields()
            self.invaders = [InvaderAgent(65 + col * 62, 65 + row * 48)
                             for row in range(4) for col in range(8)]
            self.bullets = [b for b in self.bullets if not b.enemy]

    def draw(self):
        self.canvas.delete("game")
        self.player.draw(self.canvas)
        for alien in self.invaders:
            alien.draw(self.canvas)
        for shield in self.shields:
            shield.draw(self.canvas)
        for bullet in self.bullets:
            bullet.draw(self.canvas)

        self.canvas.create_text(12, 15, anchor="w", fill="white",
                                font=("Arial", 14, "bold"),
                                text=f"Score: {self.score}    Lives: {self.player.lives}    Wave: {self.wave}",
                                tags="game")
        self.canvas.create_text(WIDTH // 2, HEIGHT - 15, fill="#aab6d3",
                                font=("Arial", 10),
                                text="Move: A/D or ←/→     Shoot: SPACE", tags="game")

        if self.game_over:
            message = "YOU WIN!" if self.won else "GAME OVER"
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, fill="white",
                                    font=("Arial", 34, "bold"), text=message, tags="game")
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 45, fill="white",
                                    font=("Arial", 16), text="Press R to restart", tags="game")

    def tick(self):
        self.update()
        self.draw()
        self.root.after(20, self.tick)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Space Invaders - Agent Game")
    window.resizable(False, False)
    GameAgent(window)
    window.mainloop()
