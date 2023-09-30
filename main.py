import pygame
import pandas as pd
import math

pygame.init()

data = pd.read_csv("data_normalized.csv")

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
offset = 500
scale = 4


# Run until the user asks to quit
running = True

x = 0
y = 0
theta = 0
x_translate = 500
y_translate = 500

delx = 0
dely = 0
t = 0
delt = 0


d1 = 0
d2 = 0
d3 = 0 
d4 = 0


color1 = (52, 192, 235)


font = pygame.font.SysFont(None, 24)


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    


    for index, row in data.iterrows():
        screen.fill((222, 222, 222))
        x1_object = x + ((row['FirstObjectDistance_X']* math.cos(theta)) - (row['FirstObjectDistance_Y'] * math.sin(theta)))
        y1_object = y + ((row['FirstObjectDistance_X']* math.sin(theta)) - (row['FirstObjectDistance_Y'] * math.cos(theta)))
        d1 = math.sqrt((row['FirstObjectDistance_X']**2) + (row['FirstObjectDistance_Y']**2))
        x2_object = x + ((row['SecondObjectDistance_X']* math.cos(theta)) - (row['SecondObjectDistance_Y'] * math.sin(theta)))
        y2_object = y + ((row['SecondObjectDistance_X']* math.sin(theta)) - (row['SecondObjectDistance_Y'] * math.cos(theta)))
        d2 = math.sqrt((row['SecondObjectDistance_X']**2) + (row['SecondObjectDistance_Y']**2))
        x3_object = x + ((row['ThirdObjectDistance_X']* math.cos(theta)) - (row['ThirdObjectDistance_Y'] * math.sin(theta)))
        y3_object = y + ((row['ThirdObjectDistance_X']* math.sin(theta)) - (row['ThirdObjectDistance_Y'] * math.cos(theta)))
        d3 = math.sqrt((row['ThirdObjectDistance_X']**2) + (row['ThirdObjectDistance_Y']**2))
        x4_object = x + ((row['FourthObjectDistance_X']* math.cos(theta)) - (row['FourthObjectDistance_Y'] * math.sin(theta)))
        y4_object = y + ((row['FourthObjectDistance_X']* math.sin(theta)) - (row['FourthObjectDistance_Y'] * math.cos(theta)))
        d4 = math.sqrt((row['FourthObjectDistance_X']**2) + (row['FourthObjectDistance_Y']**2))
        pygame.draw.circle(screen, (0, 0, 255), ((x*scale) + offset, (y*scale) + offset), 10)
        pygame.draw.circle(screen, color1, (x1_object*scale +offset, y1_object*scale + offset), 5)
        pygame.draw.circle(screen, color1, (x2_object*scale +offset, y2_object*scale + offset), 5)
        pygame.draw.circle(screen, color1, (x3_object*scale +offset, y3_object*scale + offset), 5)
        pygame.draw.circle(screen, color1, (x4_object*scale +offset, y4_object*scale + offset), 5)

        img1 = font.render(f'Object 1: {d1}', True, (0, 0, 0))
        screen.blit(img1, (20, 20))
        img2 = font.render(f'Object 2: {d2}', True, (0, 0, 0))
        screen.blit(img2, (20, 40))
        img3 = font.render(f'Object 3: {d3}', True, (0, 0, 0))
        screen.blit(img3, (20, 60))
        img4 = font.render(f'Object 4: {d4}', True, (0, 0, 0))
        screen.blit(img4, (20, 80))
        

        if (index < (len(data) - 1)):
            delt = data.iloc[index + 1]['Timestamp'] - row['Timestamp']
        delx = row['VehicleSpeed'] * delt * math.cos(theta)
        dely = row['VehicleSpeed'] * delt * math.sin(theta)
        x = x + delx
        y = y + dely
        theta = theta + row['YawRate']*delt
        pygame.time.delay(50)
        pygame.display.flip()
    screen.fill((255, 255, 255))
    x = 0
    y = 0
    theta = 0
    # Draw a solid blue circle in the center

    # Flip the display
    

# Done! Time to quit.
pygame.quit()