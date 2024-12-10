import daltonlens as dalton
from daltonlens import simulate, convert
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image

'''
Simulates what a colorblind person would see when given an image.
'''
def main():
    
    # Open an image that will be converted into the three different types of colorblindness
    while True:
        try:
            image_name = input("Enter the name of the image you want to cosnvert (FULL NAME WITH FILE TYPE): ")
            if (not (".jpg" or ".png") in image_name):
                raise ValueError
            image = Image.open(image_name).convert("RGB")
            image_names = image_name.split(".")
        except ValueError:
            print("That's not a valid name! Be sure it ends with .jpg or .png.")
            continue
        except FileNotFoundError:
            print("File not found! Ensure the picture is in the same folder as this file.")
        else:
            break

    sim = simulate.Simulator_AutoSelect()
    
    print(image_names)
    image_array = np.array(image)
    simulated_arr = sim.simulate_cvd(image_array, simulate.Deficiency.PROTAN, 0.8)
    simulated_img  = Image.fromarray(simulated_arr)
    simulated_img.save(image_names[0] + "-protanopia." + image_names[1])
    simulated_img.show()
    simulated_arr = sim.simulate_cvd(image_array, simulate.Deficiency.DEUTAN, 0.8)
    simulated_img  = Image.fromarray(simulated_arr)
    simulated_img.save(image_names[0] +"-deuteranopia." + image_names[1])
    simulated_img.show()
    simulated_arr = sim.simulate_cvd(image_array, simulate.Deficiency.TRITAN, 0.8)
    simulated_img  = Image.fromarray(simulated_arr)
    simulated_img.save(image_names[0] + "-tritanopia." + image_names[1])
    simulated_img.show()

if (__name__ == "__main__"):
    main()