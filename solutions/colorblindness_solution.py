from daltonlens import simulate
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

'''
Simulates what a colorblind person would see when given an image.
'''
def main():
    
    # Open an image that will be converted into the three different types of colorblindness
    while True:
        try:
            image_name = input("Enter the name of the image you want to convert (FULL NAME WITH FILE TYPE) " +
                               "(Be sure to add 'photos/' at the beginnning of the name): ")
            if (not (".jpg" or ".png") in image_name):
                raise ValueError
            image = Image.open(+ image_name).convert("RGB")
            image_names = image_name.split(".")
        except ValueError:
            print("That's not a valid name! Be sure it ends with .jpg or .png.")
            continue
        except FileNotFoundError:
            print("File not found! Ensure the picture is in the 'photos' folder.")
        else:
            break

    
    sim = simulate.Simulator_AutoSelect()
    image_array = np.array(image)
    # Simulate protanopia
    simulated_arr = sim.simulate_cvd(image_array, simulate.Deficiency.PROTAN, 0.8)
    simulated_img  = Image.fromarray(simulated_arr)
    simulated_img.save(image_names[0] + "-protanopia." + image_names[1])
    simulated_img.show()
    # Simulate deuteranopia
    simulated_arr = sim.simulate_cvd(image_array, simulate.Deficiency.DEUTAN, 0.8)
    simulated_img  = Image.fromarray(simulated_arr)
    simulated_img.save(image_names[0] +"-deuteranopia." + image_names[1])
    simulated_img.show()
    # Simulate tritanopia
    simulated_arr = sim.simulate_cvd(image_array, simulate.Deficiency.TRITAN, 0.8)
    simulated_img  = Image.fromarray(simulated_arr)
    simulated_img.save(image_names[0] + "-tritanopia." + image_names[1])
    simulated_img.show()

if (__name__ == "__main__"):
    main()
