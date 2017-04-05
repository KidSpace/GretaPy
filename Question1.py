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
print('A. Being dead\n')
print('B. Not being able to hear at all\n')
print('C. Slight hearing impairment\n')
print('D. Either not being able to hear at all OR having slight hearing impairment\n')

#--Correct Answer
answer = 'D'

#--Link to learn more
url = "http://www.specialeducationguide.com/disability-profiles/hearing-impairments/"

#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('A, B, C, or D?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again! Go Here For a Clue: {}'.format(url))
        
