# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 7

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door7.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Current devices to help deaf people function normally do not include...?\n\n')
print('a. Cochlear implants\n')
print('b. hearing aids\n')
print('c. a variety of around the house gadgets\n')
print('d. moon rock ear transplants\n')

#--Correct Answer
answer = 'd'


#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again!)
        

