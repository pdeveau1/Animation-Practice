import pygame

#create a class for a sprite sheet
class SpriteSheet:
  def __init__(self, img_path):
    #load image
    self.sprite_sheet = pygame.image.load(img_path)

  #create function that gets specific sprite and creates a new image
  def get_image(self,x,y,width,height):
    #create a blank image
    image = pygame.Surface([width,height])
    #add image from sprite sheet onto image
    image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
    #making the background transparent
    image.set_colorkey(image.get_at((0,0))
    #returns image we created
    return image
