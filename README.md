# deepglobe
Simple python script using DeepGlobe's neural network model to try and guess the location of an inputted image.



#instructions

1. Install the required libraries: Flask, numpy, tensorflow, opencv-python, and matplotlib. You can install them using pip by running the following command in your terminal or command prompt:

`pip install Flask numpy tensorflow opencv-python matplotlib`

2. Save the code as a Python file with a name, for example `app.py`.

3. Download the trained DeepGlobe model file from their challenge website (`path_to_model.h5`) and save it in the same directory as your Python file. (The .h5 extension is important)

4. Create a new directory named "templates" in the same directory as your Python file.

5. Run the Python file by running the following command in your terminal or command prompt:
`python app.py`

6. Open a web browser and go to the URL `http://localhost:5000/`. You should see a webpage with an "Upload Image" button.

7. Click the "Choose File" button and select an image file from your computer or paste the URL of an image on the web in the text box.

8. Click the "Predict" button. After a few seconds, you should see a new webpage with a map showing the predicted location of the image.

That's it.

I could make it a website and you had to do was upload the image but im too lazy to do that and there's no money in it so this is good as it is gonna get
