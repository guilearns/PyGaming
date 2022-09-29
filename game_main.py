import pygame, sys
import character

class GameState:

    listOfPlayers = []
    listOfNpcs = []

class Game:
    
    gameRunning = True

    windowTitle = pygame.display.set_caption("PyGaming")

    screenWidth, screenHeight = 600, 600
    screenSurface = pygame.display.set_mode((screenWidth,screenHeight))
    
    def __init__(self):
        self.gameState = GameState()
        self.keyListener = KeyListener()
        self.keyListener.functionAppender(self.acceptedKeys)
        self.addPlayer(25,25,50, 200,'Red Guy','p', 1)
        self.addNpc(25,25,50, 300,'Blue Guy','npc')
        self.addNpc(25,25,150, 300,'Blue Guy2','npc')
        self.addNpc(25,25, 250, 300,'Blue Guy3','npc')
        

    def addPlayer(self, width, height, x, y, name, type, id):
                self.gameState.listOfPlayers.append(character.PlayableCharacter(width, height, x, y, name, type, id))   


    def addNpc(self, width, height, x, y, name, type):
                self.gameState.listOfNpcs.append(character.Character(width, height, x, y, name, type))


    def acceptedKeys(self, playerInfo):
        keyName = playerInfo['keyName']
        isPessed = playerInfo['keyType'] == 'key pressed'
        keyPressedList = self.gameState.listOfPlayers[0].keysPressed
        
        print(f"The {playerInfo['playerId']} has {playerInfo['keyType']} the {playerInfo['keyName']} key.")

        if keyName == 'up':
            if isPessed:
                keyPressedList.add(playerInfo['keyName'])

            else:
                keyPressedList.discard(playerInfo['keyName'])

        if keyName == 'down':
            if isPessed:
                keyPressedList.add(playerInfo['keyName'])
            
            else:
                keyPressedList.discard(playerInfo['keyName'])

        if keyName == 'left':
            if isPessed:
                keyPressedList.add(playerInfo['keyName'])
                
            else:
                keyPressedList.discard(playerInfo['keyName'])


        if keyName == 'right':
            if isPessed:
                keyPressedList.add(playerInfo['keyName'])
                
            else:
                keyPressedList.discard(playerInfo['keyName'])

    def checkCollision(self):
        for npcSprite in self.gameState.listOfNpcs:
            self.screenSurface.blit(npcSprite.spriteSurface, (npcSprite.x, npcSprite.y))
            npcSprite.spriteRect = npcSprite.spriteSurface.get_rect(center = (npcSprite.x, npcSprite.y))
            for i in range(len(self.gameState.listOfPlayers)):
                npcSprite.colide(self.gameState.listOfPlayers[i])
  

        for playerSprite in self.gameState.listOfPlayers:
            self.screenSurface.blit(playerSprite.spriteSurface, (playerSprite.x,playerSprite.y))
            playerSprite.spriteRect = playerSprite.spriteSurface.get_rect(center = (playerSprite.x, playerSprite.y))
            for i in range(len(self.gameState.listOfNpcs)):
                playerSprite.colide(self.gameState.listOfNpcs[i])

        
        for npcSprite in self.gameState.listOfNpcs:
                for npcSprite2 in self.gameState.listOfNpcs:
                    if npcSprite2.name != npcSprite.name:
                        npcSprite.colide(npcSprite2)
                        #print(f"{npcSprite.name} x {npcSprite2.name}")
                        
    def update(self):
        while self.gameRunning == True:

            self.screenSurface.fill((0,0,0))
            
            self.keyListener.checkEvents()

            self.checkCollision()

            self.gameState.listOfPlayers[0].movePlayer()

            pygame.display.flip()


class KeyListener:

    state = {

            'FunctionList': []
        }

    def functionAppender(self, function):
        self.state['FunctionList'].append(function)
        print("Function was added to the queue")


    def functionExecuter(self, keyInfo):
            for function in self.state['FunctionList']:
                function(keyInfo)

    def checkEvents(self):

        for event in pygame.event.get():
            quitGame = event.type == pygame.QUIT
            keyDown = event.type == pygame.KEYDOWN
            keyUp = event.type == pygame.KEYUP

            if quitGame:
                pygame.quit()
                sys.exit()
            
            elif keyDown:
                keyPressed = pygame.key.name(event.key)
                keyInfo = {'playerId': 'p1', 'keyName': keyPressed, 'keyType':'key pressed'}
                self.functionExecuter(keyInfo)

            elif keyUp:
                keyReleased = pygame.key.name(event.key)
                keyInfo = {'playerId': 'p1', 'keyName': keyReleased, 'keyType':'key released'}
                self.functionExecuter(keyInfo)
      

pygame.init()
game = Game()
game.update()