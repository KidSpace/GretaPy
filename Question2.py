# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 2

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door2.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('The two main types of deafness are...?\n\n')
print('a. old deafness and young deafness\n')
print('b. conduction deafness and nerve deafness\n')
print('c. happy deafness and sad deafness \n')
print('d. genetic deafness and non genetic deafness\n')

#--Correct Answer
answer = 'b'

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
        
