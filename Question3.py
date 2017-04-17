# Greta's Quiz Game
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

number = 3

#--Cool Image to show if they answer the question Right
pil_im = Image.open('door3.png', 'r')
imshow(np.asarray(pil_im))
imshow(pil_im)

#--The Question and Answer Pairs
print('Congenital hearing loss is...?\n\n')
print('a. Slight hearing loss\n')
print('b. Caused by genetic factors ALL the time\n')
print('c. Present at birth\n')
print('d. Hearing loss old people get\n')

#--Correct Answer
answer = 'c'

#--Link to learn more
url2 = "http://www.asha.org/public/hearing/Congenital-Hearing-Loss/"

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
        
