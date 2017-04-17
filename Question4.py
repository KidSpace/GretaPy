# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 4

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door4.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Deaf children do not experience...as a result of their condition.\n\n')
print('a. frequent pneumonia\n')
print('b. problems balancing\n')
print('c. speech delays\n')
print('d. difficulty communicating\n')

#--Correct Answer
answer = 'a'

#--Link to learn more
url3 = "http://www.livestrong.com/article/509643-characteristics-of-hearing-impairment-and-deafness-in-children/"

#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again! Go Here For a Clue: {}'.format(url3))
        
