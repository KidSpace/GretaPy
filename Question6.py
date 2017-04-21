# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 6

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door6.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Sign language, lip reading, and talking are all ways deaf people participate in conversations.\n\n')
print('a. True\n')
print('b. False\n')


#--Correct Answer
answer = 'a'


#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again!')
        
