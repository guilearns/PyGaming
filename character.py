import pygame

class Sprite:
    def __init__(self,width, height, x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.position = (x,y)
        self.spriteSurface = pygame.Surface((self.width,self.height))
        self.spriteRect = self.spriteSurface.get_rect(center = self.position)
        self.spriteSurface.fill('green')

    def colide(self,otherSprite):
        externalRect = otherSprite.spriteRect
        collisionTolerance = 5
        if self.spriteRect.colliderect(externalRect):
            if abs(externalRect.top - self.spriteRect.bottom) < collisionTolerance:
                otherSprite.y += 1
                #print("top->bottom collision")
            elif abs(externalRect.bottom - self.spriteRect.top) < collisionTolerance:
                otherSprite.y -= 1
                #print("bottom->top collision")
            elif abs(externalRect.left - self.spriteRect.right) < collisionTolerance:
                otherSprite.x += 1
                #print("left->right collsion")
            elif abs(externalRect.right - self.spriteRect.left) < collisionTolerance:
                otherSprite.x -= 1
                #print("right->left collision")

class Character(Sprite):
    def __init__(self, width, height, x, y, name, type):
        super().__init__(width, height, x, y)
        self.spriteSurface.fill('blue')
        self.name = name
        self.type = type
        
class PlayableCharacter(Character):
    def __init__(self, width, height, x, y, name,type, id):
        super().__init__(width, height, x, y, name, type)
        self.spriteSurface.fill('red')
        self.id = id
        self.type= type
        self.keysPressed = set()
        
    def movePlayer(self):
        if 'up' in self.keysPressed:
            self.y -= 0.2

        if 'down' in self.keysPressed:
           self.y += 0.2

        if 'left' in self.keysPressed:
            self.x -= 0.2

        if 'right' in self.keysPressed:
            self.x +=  0.2

