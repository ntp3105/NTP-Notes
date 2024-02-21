# NTP-Notes
This Git repo is created to store the important notes done on various topics, intended to compile all the tids-bits and tips found on various learning resources like LinkedIN, Books, IG, Git, Coursera, Kaggles, Software documentations. The following topics will be compiled here:
1) Git, Github, Github Actions
2) Machine Learning
     i) Supervised Learning
         . Continuous Regression
         . Logistic Regression
         . Boosting
         . Bagging
         . Decision Trees
    ii) Unsupervised Learning
         . Clustering
         . Dimensional Reduction
3) Deep learning
         . Image processing
         . Text processing -> natural Language Processing
         . Computer vision
         . Speech recognition
         . pattern Recognition
4) Data Science
5) Data Engineering
6) MLOps
7) Finance
8) Statistics and mathematics
9) Python programming + Object-Oriented Programming (OOP)


how to use requirements.txt in coding?

Here's a guide on how to use requirements.txt in coding:

1. Creating a requirements.txt file:

    Open a plain text editor (like Notepad, TextEdit, or VS Code) and create a new file named requirements.txt.
    List each required package on a separate line, following this format:

·        <package_name>==<version_number>

Example:

requests==2.28.1

numpy==1.23.4

pandas==1.5.0

2. Installing packages using requirements.txt:

A. Using pip directly:

    Open a terminal or command prompt and navigate to the directory containing your requirements.txt file.
    Run the following command:

Bash

pip install -r requirements.txt

Use code with caution. Learn more

     

B. Using virtual environments (recommended):

    Create a virtual environment to isolate project-specific dependencies:

Bash

python -m venv myvenv

Use code with caution. Learn more

·  ·  Activate the virtual environment:

    Windows: myvenv\Scripts\activate.bat
    Linux/macOS: source myvenv/bin/activate

·  Then, install packages from requirements.txt:

Bash

pip install -r requirements.txt

Use code with caution. Learn more

     

3. Updating requirements.txt:

    To add new packages:
        Install them using pip install <package_name> while your virtual environment is active.
        They'll be automatically added to requirements.txt.
    To update existing packages:
        Run pip freeze > requirements.txt to regenerate the file with updated versions.

4. Sharing your project:

    Include requirements.txt to allow others to easily install the necessary packages for your project.

Additional tips:

    Use constraints to specify compatible version ranges (e.g., numpy>=1.22,<1.25).
    Pin exact versions for reproducibility (e.g., numpy==1.23.4).
    Consider tools like pipenv or poetry for advanced dependency management features.
