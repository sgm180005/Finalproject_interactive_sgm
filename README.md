[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/0tX0M0Sy)
# Challenge Lab 8: Digital Rain

## ☔ Digital Rain

## Demo
Demo Video: <https://youtu.be/C5WglUmk2DU>

## GitHub Repository
GitHub Repo: <https://github.com/sgm180005/Finalproject_rain_sgm.git>

## Description

The Matrix series of science fiction action films are about a dystopian future where humans are unknowingly trapped in a simulated reality designed by machines to distract them while their real bodies are being used as an energy resource. 😱

Production Designer Simon Whiteley designed the iconic matrix digital rain of downward flowing green characters that opens the movies. The effect represented the code behind the simulated reality in the Matrix and is such a recognizable piece of kinetic typography.

Check out the opening scene below:

[![The Matrix Opening](https://img.youtube.com/vi/Yp8mfKR27xg/0.jpg)](https://youtu.be/Yp8mfKR27xg "The Matrix Opening")



In this challenge, we’ll working on a Matrix Digital Rain inspired animated real-time art.

## Requirements



Follow along Chapter 08 of the Programming for Digital Artists material.

The series of videos in the chapter will help you to setup your program and build a basic digital rain for your screen saver. Concepts are explained along the way.

By the end of the videos, you should have these following features implemented.

- **Window & Title** - A 800x600 pixel window with a title.
- **Falling Particles** - Particles that fall down from the top of the screen at randomly generated locations along the x axis.
- **Particle Trails** - Each particle leaves a trail of fading particles that randomly vary in length.
    
    ![Example of digital rain effect at the end of the video walk-through.](docs/digital_rain_final.gif)
    
    Example of digital rain effect at the end of the video walk-through.
    

Once you have completed the video materials, continue to add features to your digital rain effect.

1. **Full screen** - Add the feature to allow a full screen display that is at least 1920x1080 pixels (HD).
    - Read up the pygame `display` module on how to create a full screen program.
        - [pygame.display — pygame v2.6.0 documentation](https://www.pygame.org/docs/ref/display.html)
2. **Colors** - Add different colors to the particle trails. Use your creativity, but make it look cool!
3. **Shapes/Characters** - Besides the square particle, add other shapes and/or characters to your particle rain effect.
    - You will want to look into pygames `draw` and `font` modules to learn how to draw/render other shapes and text to your particle surface.
        - [pygame.draw — pygame v2.6.0 documentation](https://www.pygame.org/docs/ref/draw.html)
        - [pygame.font — pygame v2.6.0 documentation](https://www.pygame.org/docs/ref/font.html)
4. **Innovation** - Make your screen saver unique by adding some new features and exploring new concepts.
    - There’s no exact number of features here, you are graded on effort and experimentation.
    - A rule of thumb would be to 1-2 significant features for full credit, but these depend on the complexity of features implemented.
    - Possible examples include: “Glitching Particles (some characters/shapes on the trail periodically change/glitch.)”, “Leading particles have a different color”, “Keyboard input - changes colors and other settings.”, “Mouse clicks causes more rain to fall on areas of the screen.”, etc…
5. **Commentary Demo Video** - Create a narrated commentary video that explains your program requirements and innovation clearly.
    1. **(If needed) Watch the below video on how to record your screen.**
        1. [How to use OBS for Screen Recording or Streaming - Beginner Tutorial](https://youtu.be/ySENWFIkL7c?si=Sdv_2UUNNi0CQFh7). (26 min)
        2. OBS is the recommended tool for screen-recordings.
        3. If you choose to record in  `.mkv`, you may remux it to  `.mp4` h.264 codec with OBS or [HandBrake](https://handbrake.fr/).
    2. **Presentation** - Demonstrate and describe all requirements including innovation as concisely as possible.
        1. **Show only your program running in full screen. Do not show your code, excepting the second or two when you are launching your program.** 
        2. You must show how you launch the program.
        3. Present your requirements in order of the grading criteria. If you present out-of-order, you risk losing points.
        4. State the requirement, then say a few words about it and ensure it is shown functioning in the video.
        5. If you couldn’t complete a requirement, just say so and move on to the next requirement but stay in order.
        6. If you don’t show it clearly in the video, you won’t receive credit for it.
        7. Watch your video before submitting.
    3. **Be Concise** - Keep your video **<2 mins**. Videos that go over with no good reason, risk being penalized.
    4. **Format** - **MP4** (h.264 codec), minimum **1920x1080** pixels, **24 FPS** or more, **<100mb**
        1. Filename: `pfda_c08_rain_<LastnameFirstname>.mp4`

## 💯 Grading Criteria



1. **10% - Deliverables** - All deliverables submitted in the right format and channels. 
2. **20% - Particles Falling** - Particles fall from the screen top & randomly spawned along the x axis. 
3. **20% - Particles Trails** - Particle display trails. The trails fade and vary in length.
4. **10% - Full Screen** - Program is able to run in full screen.
5. **10% - Colors** - Particle trails exhibit variation in colors with aesthetically-pleasing results. 
6. **20% - Shapes/Characters** - Use of other shapes and/or characters in the particle trails.
7. **10% - Innovation** - Innovative feature(s) exploring new concepts. 

## 🔗 Optional Resources



- **[Displaying Text on The Screen In Pygame - Beginner Tutorial](https://www.youtube.com/watch?v=ndtFoWWBAoE) (5 min)**
Pygame doesn't have built in functionality to allow you to display text on the screen. In order to display text, you have to work through a few steps of converting the text into an image(surface) and then showing the image(surface) on the screen. This video shows you how to do so.
- **[Drawing Shapes In Pygame - Beginner Tutorial](https://youtu.be/YDP1Hk7uZFA?si=3h48yQdUI4qtyn8Q) (11 min)**
This video goes through drawing basic shapes in pygram including circles, ellipses, arcs, lines and polygons.
- **[Using The Mouse In Pygame - Beginner Tutorial](https://youtu.be/YbouZ2X8fGk?si=xOID94frZBjnVt1O) (8 min)**
This video explains how to get mouse input from the player in pygame.
- **[The ultimate introduction to Pygame](https://youtu.be/AY9MnQ4x3zk?si=LHKt9Xz6jJqHjdPE) (3:47:57)**
One of the best introductory videos to using Pygame. Check it out if you are interested to learn more on how to use PyGame to learn game development skills.

## 🎏 Before You Begin



1. In VS Code, **Open** the assignment folder.
2. **Run** `cd src` in the terminal to change directories into the `src` folder. This is where you will save your code (a.k.a. source files).
3. If needed, **Execute** `code rain.py` to create an empty file called `rain.py` . 
4. Implement your code in `rain.py` .

## 💻 Demo



```bash
> python rain.py
```

Since all your digital rain effects are going to look different based on your modifications, it won’t be possible to show you an exact demo.

## ✅ How to Test?



Here’s how to test your code manually. 

In the VS Code terminal, **ensure that you are in the `src` folder where your code resides.**

- Run the program with `python rain.py`. Your program should:
    - Launch a full screen application and begin with digital rain particle trails falling from the top of the screen.

If you run into errors saying your file cannot be open, be sure that your current working directory is `src` and that you have saved your `.py` file there.

**No auto tests for this lab! 🥳**

## 💾 How to Commit Your Progress?



As the saying goes, “commit often and commit early.” 

Examples of stages you should commit is whenever you: 

- pass a test,
- make some tangible progress you’ll regret losing suddenly,
- code up a new feature,
- fixed a bug,
- started a new file with minimal code, etcetera.

These all make great opportunities to commit your changes.
In this course, you are expected to **break up your work into several commits** to show progression.

We want to see how your code evolved and progressed by glancing at your commit history, so ensure you use short but meaningful commit messages. 

**You will be penalized if your commit messages are too generic.** For example:

- “Update 1”, “test”, “committed”, etc.

Looking for tips on how to write better commit messages? Check out:

[How to Write Better Git Commit Messages – A Step-By-Step Guide (freecodecamp.org)](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)

## 📤 How to Submit?



For this lab, you will:

1. **Commit and push** your python code to your **GitHub** repository, 
2. **Record and submit** a video demonstration of your program on **eLearning.**



Whenever you push changes to the GitHub repository on the cloud, your work is submitted.

If the Lab Challenge has a deadline, just make sure to push your final changes before the Lab Challenge deadline. You will not be able to push changes to GitHub after the deadline.

To ensure your final changes are on GitHub, please review the files in your GitHub repository as well as the autograde test results (if any) after you push your changes from VS Code to GitHub.

You can double-check your submission by going to the “code” section of your GitHub repository, clicking on the `src` folder, and viewing the contents.

**Don’t forget to submit your video demo on eLearning!**