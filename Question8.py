# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 8

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door8.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('?\n\n')
print('a. \n')
print('b. \n')
print('c. \n')
print('d. \n')

#--Correct Answer
answer = 'c'

#--Link to learn more
url = "http://school.eb.com/levels/high/article/deafness/29631"

#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again! Go Here For a Clue: {}'.format(url))
        

