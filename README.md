# Ship-simulator
# Introduction
This is a report about the simulator that I did during my internship at ENSTA. The aim of the simulator is to get easily a lot of data in order to build a model to predict the pitch and the roll of a ship.

# Sources
In this section I am going to indicate the main tutorials I have followed to achieve the simulator. Besides the sites I am going to indicate I have consulted a huge amount of forums.\\
As Zhi (the precedent internship) recommended I have followed this youtube tutorials to create the trajectory and make the ship follow the sea's movement: \url{https://www.youtube.com/watch?v=sfi7HW8qHAo}.\\

And for rendering the sea, after trying very hard to define the propierties for the rendering with a python script and not finding any information about how to do that, I took the next tutorial: \url{https://blenderartists.org/t/fast-ocean-blender-add-on-for-ocean-foam-and-auto-collisions/688073/44} 
# Algorithm for the simulator
Due to the impossibility of putting into a python script the render part, it is mandatory do use a blender file with the propierties of the render already set. The macro opens this blender file, modifies the physical parameters of the ocean, introduces the boat and the camera and takes the data (frames and pith and roll).\\

As i said before, the trajectory of the boat is a circle. The first thing the algorithm does is to create a plane and subdivide it twice. After that it makes the plane follow the circle but with the condition that the vertex of the subdivision should be together and setting the velocity of the plane. After that it creates a cube and it links it to the plane computing the middle between the vertex named before and the center of the cube.\\
After that it creates a camera and links it in a constant size from the cube to make. The link is also for the angles of the camera with respect to the cube but the pitch and the roll of the camera are disabled so it will be stabilized no matter the pitch and the roll of the ship

# Parameter that are not in the script
There are some parameter that are not in the script but can be easily change in order to have more and different data
## Change the sky
Changing the sky will not change only the sky, it will change also how the light affect the water and how it is reflected. It is very easy to change. Just open blender and go to the 'world' option in the Properties (normaly at the right part of the screen) and go to surface. There will be an image .jpg or .png selected, go to the folder draw and select the new one. Take into account that you will need a 360 degrees sky image, not just a photo.
## Link again the camera and the boat
To link the camera and the boat go to the camera's properties and to the constrains options (chain drawing) and select 'X' and 'Y' in 'Rotation'.
## Changing the characteristics of the boat
We have thought about changing the characteristics of the boat in a future. As it is explained before, the boat is linked to a plane so if we want to simulate a bigger boat where the area of the influence between the sea and the boat is bigger we will just have to do the plane bigger. With this, somehow we will simulate the inertia of the boat that is not taked into account in the simulator (there is no any physical model in the simulation)
## Changing the render properties of the sea
The level of realism of the sea can be improved changing the properties of the sea if it is need, you can follow a tutorial about that in the internet and change the blender file (oceanrender2.blend) and save it. I tried several and i thought this one was fine in order to do not take a lot of time computing each frame.

# Files
## parameters.py
Here you have all the parameters that the macro is goingo to import. You can select to iterate between several parameters. Those parameters are only choppiness, wave scale, wind velocity and random seed. Is not very difficult to add more parameters but those are the parameters that are more important to change the simulation. Here: https://docs.blender.org/manual/en/dev/modeling/modifiers/simulate/ocean.html you can find what does each parameter exactly do related to the ocean creation. The parameters about the render are clearly explained in the code.

## macro.py
This is the macro. Theorically you will not need to change anything from here but there are some explanations inside about what the code does and I encourage you to improve the code and add more functions.

## VideoMaker.py
This is the program to make videos of the different episodes. You have to specify the folder of the episode and the folder where you want to save the video.
Example (done in the same path as data folder is):
python3 VideoMaker.py -i data/2021204820 -o data/20190421204820
