# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 1

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door1.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Deafness is...?\n\n')
print('a. Being dead\n')
print('b. Not being able to hear at all\n')
print('c. Slight hearing impairment\n')
print('d. Either not being able to hear at all OR having slight hearing impairment\n')

#--Correct Answer
answer = 'd'

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
        
