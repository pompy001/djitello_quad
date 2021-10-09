import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyname):
    ans = False
    for eve in pygame.event.get():pass

    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame , 'K_{}'.format(keyname))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey("LEFT"):
        print("The Left Key Pressed")
    if getKey("RIGHT"):
        print("The Righ Key Is Pressed")
    

if __name__ =="__main__":
    init()
    while True:
        main()

