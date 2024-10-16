
# BDA2024 Autumn Lab 4

This repository contains the code for the BDA2024 Autumn Lab 4 project. To ensure a smooth setup and execution of the code, we use a `Pipfile` to manage dependencies and virtual environments. Follow the steps below to get started with this project.

## Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8 or higher**: This project is developed using Python 3.8. Please install or set your Python version accordingly.
- **pipenv**: We use `pipenv` for managing the virtual environment and dependencies. You can install it via pip:
  
  ```bash
  pip install pipenv
  ```

## Setting Up the Project

1. **Clone the repository**:
   
   First, clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/datamass-io/bda2024-autumn-lab4.git
   cd bda2024-autumn-lab4
   ```

2. **Install dependencies**:

   Use `pipenv` to install all the necessary dependencies specified in the `Pipfile`.
   
   ```bash
   pipenv install
   ```

   This will create a virtual environment and install all required packages listed in the `Pipfile`. If you only need the dependencies and not the development tools, you can use:

   ```bash
   pipenv install --ignore-pipfile
   ```

3. **Activate the virtual environment**:
   
   Once the dependencies are installed, activate the virtual environment:
   
   ```bash
   pipenv shell
   ```

4. **Run the project**:

   With the environment set up, you can now execute the necessary scripts. Make sure to check the documentation or lab instructions for the required command:

   ```bash
   python <your_script.py>
   ```

   Replace `<your_script.py>` with the actual Python script you want to run for the lab.

## Additional Commands

- **Check for outdated packages**:
  
  If you want to check for outdated packages, use:
  
  ```bash
  pipenv update
  ```

- **Exit the virtual environment**:

  When you are done working, simply exit the virtual environment with:
  
  ```bash
  exit
  ```

## Contribution

Feel free to submit issues or pull requests if you encounter any bugs or have suggestions for improvements.
