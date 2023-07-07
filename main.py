import tkinter as tk

#Screen Dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400

#Sprite Dimensions
SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50

MOVE_SPEED = 1

class Sprite:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = tk.PhotoImage(file="./sprite.png")
        self.sprite = self.canvas.create_image(SCREEN_WIDTH // 2, SCREEN_HEIGHT - SPRITE_HEIGHT, image=self.image)
        self.move_right = True
        
    def move_sprite(self):
        sprite_cor = self.canvas.coords(self.sprite)
        sprite_x = sprite_cor[0]
        if self.move_right:
            sprite_x += MOVE_SPEED
            if sprite_x + SPRITE_WIDTH >= SCREEN_WIDTH:
                self.move_right = False
        else:
            sprite_x -= MOVE_SPEED
            if sprite_x <=0:
                self.move_right = True
        self.canvas.coords(self.sprite, sprite_x, sprite_cor[1])
    
def main():
    # Main Window
    window = tk.Tk()
    window.title('Virtual World')
    
    #Window Size
    canvas = tk.Canvas(window, width=SCREEN_WIDTH, height = SCREEN_HEIGHT)
    canvas.pack()
    
    sprite = Sprite(canvas)
    
    def animate():
        sprite.move_sprite()
        window.after(16, animate) #60 fps
    
    animate()
    
    window.mainloop()
    
    
if __name__ == "__main__":
    main()