# Replicating Colorblindness on Photos

## Overview

This assignment focuses on replicating how a colorblind person would envision a certain image based on their colorblindness. The goals include browsing through a python library, understanding what the library does, and assessing how someone with colorblindness has trouble with envisioning certain images.

## Objectives

1.  **Browsing a Python Library and Obtaining Information**

    - Browse through the source code of a Python Library and obtain information from the code to be used in the assignment.

2. **Understanding how to use functions and classes from a Library**

    - Use the knowledge gained from browsing the library to replicate what is asked for in the assignment.

3. **Colorblindness Analysis**

    - Assess the pictures generated, and draw ideas for the differences in how someone with colorblindness views the world differently.


## Introduction

Colorblindness is a visual difference, where certain people may see a certain color a different way, or don't even see a certain color at all. These can lead to many challenges for someone with colorblindness. For instance, they may not be able to distinguish grass from gravel, or even a large animal in a forest.

This assignment aims to show people how certain color deficiencies actually look like, using a picture of an Ishihara color deficiency image to show the true differences of these color deficiencies. Then, we want people to understand how hard it may be for someone with these deficiencies to operate in life, whether that be through their job or just life in general.

## Instructions

### Part 1: Understanding `daltonlens`
This assignment will be using `daltonlens` as its main source of replicating this colorblindness. It's actually really helpful! As this library will actually simulate the colorblindness for us, we barely need to write any code!

Thus, you should absolutely understand what `daltonlens` actually entails, before just using it.

1. To start, you most likely don't have `daltonlens` even installed for python. So, in your console, type
 
    - `pip install daltonlens`

    to download daltonlens to be able to use on your computer. If it worked, the `from daltonlens import simulate` should no longer be underlined or greyed out! If not, ask your professor for assistance.

2. Next, click this link:
    - https://github.com/DaltonLens/DaltonLens-Python/tree/master

        This will take you to the source code of `daltonlens` that we will be using in this assignment. There's a lot of folders and files! However, we only really care about one.

3. Click on the `daltonlens` folder on the github page.

    - You'll see a lot of different python files! You can browse through all these files if you want, but for now, we only want to focus on one, as it is the file we will be using for this assignment. 

4. Find which python file we will be using for this assignment, and open it.
    - #### HINT: take a look at the import lines at the top of `colorblindness.py`!

5. Look through this file.
    - Now, there's a LOT of information on this file. However, there are only a few things you should focus on for now.

    - Firstly, find the class `Deficiency` in the file. It should be close to the top.
        - Take a look at these different deficiencies. They will be important for later!

    - Next, take a look at the `Simulator` class, which should also be at the top.
        - Focus on its method `simulate_cvd` as we will be using it in this assignment! Obviously, you won't understand it entirely, but take a look at it, and understand what it is doing. Be sure to also look at its parameters, and what their data types are!

    - Lastly, glance over the rest of the `Simulator` classes. Mainly, glance over `Simulator_AutoSelect` class. 

### Part 2: Get an image that will be used to simulate colorblindness
Now, go back to `colorblindness.py`. There's only one function, `main()`! That's alright. We don't really need many functions! However, you will need to know how to get a photo as input from a user.

1. Get input from a user, which is the name of the photo that will be converted. Be sure to account for error cases!

    IMPORTANT TIPS:
    -  Make sure that if the user inputs an incorrect name, or an incorrect format, account for the error, but don't end the program!
        -  Use `try` and `except` to account for these errors.
            - If the name doesn't end in `.jpg` or `.png`, be sure to raise a `ValueError` and account for that.
            - If the file is not found, be sure to account for that error as well!
            - Try different inputs and see what errors pop up, and account for them!
    - IMPORTANT: Be sure to tell the user to type `photos/` at the beginning of their name! Since `photos` is the folder where the photos will be at, if you tell them to input `photos/` before the actual name, your generated photos will also be saved in the `photos` folder!

2. Use `Image` imported from `PIL` to open the image from the user input.
    IMPORTANT TIPS:
    - Use the function `Image.open()` to open the file associated with the name obtained from the user input.
    - BE SURE TO USE THE FUNCTION `convert("RGB")` on the object that the image is associated with! If you don't use this function, then the `daltonlens` code will produce errors!

### Part 3: Initialize a `Simulator` object and convert the image
This is a short section, don't worry!
1. Initialize a `Simulator` object, and convert the image to an image array.
    IMPORTANT TIPS:
    - In order to actually initialize the simulator object, be sure to type `simulate.[CHOSEN SIMULATOR]` so you're accessing `simulate` from `daltonlens`. If it worked, the text shouldn't be greyed out!
        - Think back to the Simulators you looked at. Which type of simulator class would be the best for simulating the three different types of color deficiencies?
    - For converting the image, use `np.array()` to convert it into an array, so the next part can go by swimmingly.

### Part 4: Simulate the color deficiencies

Now for the fun part, actually simulating and generating the image!

1. From your simulator object, use `simulate_cvd()` with the appropriate parameters to generate an image of a color deficiency.
    IMPORTANT TIPS:
    - Look back at `simulate_cvd()` and its parameters! How exactly can you get a `Deficiency` object from `simulate.py`?
        - HINT: Use `simulate.Deficiency.[NAME]` to get a `Deficiency` object for the parameter!
    - The generated object from `simulate_cvd()` is actually an array! So you will need to generate an `Image` object from that array. How could you go about doing that? What method from `Image` could you use? HINT: It has `array` in its name!
    - Be sure to save the image using the method `.save([IMG NAME])` on your new `Image` object.
        - Be sure to save the image with a new name, or at least something that indicates which type of color deficiency it simulated! If you save it with the same name as before, it will overwrite the other image!

2. Repeat Step 1, but for the other two color deficiencies.

3. To test your code, use the base image, `ishihara.jpg` located in photos. Then, take a look at your generated photos!

4. Compare your images with the images that have `ACTUAL` in their name. Are they similar?

5. Grab an additional image from the internet, or wherever, of an object that you commonly see, and use your code to simulate color deficiency on that photo. See the differences of what they see versus what you see!

### Congratulations! You finished it!

## Questions and Conclusions
In a .txt file, answer these questions. A few sentences will be enough:

1. Take a look through `daltonlens` and `simulate.py` again. Notice that the top of `simulate.py` has an import from `convert.py`. Find where these are used. Why would they need to import this? Take a look through the rest of the files if you're stuck.

2. Think about how much code `simulate.py` has, and how much code is in `daltonlens` itself. With ample time, do you think you could create an algorithm that replicates these effects? Maybe make it simpler? Why or why not?

3. Take a look at your generated images again. Think about what they see, and think about your own life. If you had one of these color deficiencies, how different would your life be? Would an object you owned look completely different than what it was like before?

4. Do you think it is important to put resources into visuals to be able to compensate for colorblindness? Why or why not?


## Resources
- Python libraries: `daltonlens`, `PIL`, `numpy`