# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 10

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door10.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Deaf kids are...?\n\n')
print('a. dumb, stupid, hopeless\n')
print('b. unique, amazing, adaptable, creative, intelligent, kind, special \n')
print('c. weird, ugly, awkward\n')
print('d. unfortunate, unlucky, pathetic\n')

#--Correct Answer
answer = 'b'

#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again! You really should have gotten this one right!)
        
