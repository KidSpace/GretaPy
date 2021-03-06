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
print('Deaf children cannot talk on the phone.\n\n')
print('a. True \n')
print('b. False\n')

#--Correct Answer
answer = 'b'

#--Link to learn more
url4 = "http://www.ndcs.org.uk/family_support/fostering_deaf_children/six_things_you_didnt_know_about_deaf_children/"

#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again! Go Here For a Clue: {}'.format(url4))
        

