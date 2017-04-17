# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 5
picture = 'door5.png'

#--Cool Image to show if they answer the question Right
pil_im = Image.open('{}'.format(picture), 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('If deaf students do not get proper educational intervention, they have often only achieved... skills upon graduating highschool.\n\n')
print('a. first or second grade\n')
print('b. third or fourth grade\n')
print('c. tenth or twelfth grade\n')
print('d. graduate school\n')
#--Correct Answer
answer = 'b'

#--Link to learn more
url4  = "http://www.asha.org/public/hearing/disorders/effects.htm"

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
        
