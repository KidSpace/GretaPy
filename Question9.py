
# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 9

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door9.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Deaf children can...?\n\n')
print('Hint: Vibrations are heard AND felt...) 
print('a. not enjoy listening to music or make music.\n')
print('b. enjoy listening to music, but not make music.\n')
print('c. enjoy listening to music AND make music\n')
print('d. not enjoy listening to music but make music\n')
#--Correct Answer
answer = 'c'

#--Link to learn more
url5 = ""

#--Boolean
understand_deafness=False

#--While loop
while not understand_deafness:        
    guess = input('a, b, c, or d?\n\n\n')
    
    if guess == answer:
        print('Correct! Great Job! You Just Passed Through Door # {}!'.format(number))
        understand_deafness=True
    else:
        print('\nSorry, Try Again! Go Here For a Clue: {}'.format(url5))
        
