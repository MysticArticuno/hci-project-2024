# Final Project for CSCI-4235: Human Computer Interaction
###### Contributers: 
* Grayson Murdock
* Magariou Diallo
* Tamilore Olanipekun

## Installation

To begin, please clone the repository using the command `git clone https://github.com/MysticArticuno/hci-project-2024.git`. Ensure you have git installed. You may use GitHub Desktop if you prefer.

### Python API

Ensure you have a working version of Python on your system. To check if you do, run the command `python --version`. If this returns text similar to `Python 3.12.7`, then Python is installed

[!NOTE]
Some versions of Python use the command `python3` instead of `python`. If the above command does not work, try using `python3`

After cloning, make sure you set up a python virtual environment.
To do this, navigate to the API folder and run the following commands:
###### Windows:
```
python -m venv .venv
.venv\Scripts\activate.bat
```

###### Mac/Linux:
```
python -m venv .venv
source ./.venv/bin/activate
```

Once the virtual environment is activated, you will need to install Flask with the command `pip install Flask`. When the installation is complete, start the Flask server by running `flask -app main.py run`
