# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import pandas as pd

# Set up a square array which will represent the field available to the predator and prey
array_size = 400
prey_array_R = np.zeros((array_size, array_size))
pred_array_G = np.zeros((array_size, array_size))
land_array_B = np.zeros((array_size, array_size))


# Create a placeholder RGB array from the prey and predator arrays
rgbArray = np.zeros((array_size, array_size, 3), dtype='uint8')
rgbArray[..., 0] = prey_array_R * 255
rgbArray[..., 1] = pred_array_G * 255
rgbArray[..., 2] = land_array_B * 255

# Convert the array to an image
img = Image.fromarray(rgbArray)

# Save the image to a file
img.save('Array_files/rgbArray_img.jpeg')

# --------------------------------------------------------------------------------------------

### PARAMETERS ###

# PREY #
# Set up a data frame to store prey parameters for multiple prey
# Each row will represent a different prey individual (prey1, prey2, etc.)
# Each column will represent a different parameter (e.g. speed, decay rate, energy, etc.)
prey_df = pd.DataFrame(columns=['speed', 'decay'])
# Add a row to the data frame for prey1

prey_speed = 1
prey_decay = 0.99

# Set up a random starting position (x,y) in the array for the prey
# random number between 1 and array_size
x = np.random.randint(1, array_size )
y = np.random.randint(1, array_size)
x, y = (x, y)

# PREDATOR #
pred_speed = 1
pred_decay = 0.99

# Set up a random starting position (x,y) in the array for the prey
# random number between 1 and array_size
a = np.random.randint(1, array_size )
b = np.random.randint(1, array_size)
a, b = (a, b)

#--------------------------------------------------------------------------------------------

## SIMULATION LOOP ##

# Set up a loop to move the walker in a random direction
for i in range(10000):

    ## PREY ##
    # halve the brightness of the prey array to show a trail of where the prey has been
    prey_array_R = prey_array_R*prey_decay

    direction = np.random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up':
        x, y = (x, y+prey_speed)
    elif direction == 'down':
        x, y = (x, y-prey_speed)
    elif direction == 'left':
        x, y = (x-prey_speed, y)
    elif direction == 'right':
        x, y = (x+prey_speed, y)

    # If the prey reaches the edge of the array on either side, it will turn around and move in the opposite direction
    if x > array_size-1:
        x = x - prey_speed
    elif x < 1:
        x = x + prey_speed
    elif y > array_size-1:
        y = y - prey_speed
    elif y < 1:
        y = y + prey_speed
    
    # Change the cell value of the prey's current position to 1
    prey_array_R[x, y] = 1

    ## PREDATOR ##
    # Halve the brightness of the predator array to show a trail of where the prey has been
    pred_array_G = pred_array_G*pred_decay

    direction = np.random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up':
        a, b = (a, b+pred_speed)
    elif direction == 'down':
        a, b = (a, b-pred_speed)
    elif direction == 'left':
        a, b = (a-pred_speed, b)
    elif direction == 'right':
        a, b = (a+pred_speed, b)

    # If the predator reaches the edge of the array on either side, it will turn around and move in the opposite direction
    if a > array_size-1:
        a = a - pred_speed
    elif a < 1:
        a = a + pred_speed
    elif b > array_size-1:
        b = b - pred_speed
    elif b < 1:
        b = b + pred_speed
    
    # Change the cell value of the predator's current position to 1
    pred_array_G[a, b] = 1

    #--------------------------------------------------------------------------------------------

    # Add new prey & predator array to the RGB array
    rgbArray = np.zeros((array_size, array_size, 3), dtype='uint8')
    rgbArray[..., 0] = np.round(prey_array_R * 255, 0)
    rgbArray[..., 1] = np.round(pred_array_G * 255, 0)
    rgbArray[..., 2] = land_array_B * 255

    # Convert the array to an image
    img = Image.fromarray(rgbArray)

    # Save the image to a file
    img.save('Array_files/rgbArray_img.jpeg')

    # Read the image back in with cv2
    rgbArray_img = cv2.imread("Array_files/rgbArray_img.jpeg", cv2.IMREAD_COLOR)
    
    # Display the modified image
    cv2.imshow("EvolGame", rgbArray_img)
 
    # Wait 0.1 s before displaying the next image
    key = cv2.waitKey(10)

    # Press 'Esc' to exit the loop
    if key == 27:
        break

# Close the window
cv2.destroyAllWindows()
