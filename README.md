# Comp730-FinalProject Alex+Nathan

## Overview of Class Diagram
Diagram for Alex Contribution:
![My Image](images/Alex.jpg)

Diagram for Nathan Contribution:
![My Image](images/Nathan.jpg)

## How to Run Project
1. Clone repository, replace `[Forlder name]` with a name of your choice.
    ```
    Git clone https://github.com/AWachenfeld/Comp730-FinalProject-AlexNathan.git [Folder name]
    ```

2. Install pandas for Python
    ```
    Windows:
    pip install pandas
    ```
    Other installation documentation: https://pandas.pydata.org/docs/getting_started/install.html

3. Cd in to project location where folders such as `Tests`, `Src`, and `Data` can be found.

4. Cd into `Src` folder.

5. Run Program
    ```
    python home.py
    ```

6. Navigate menus based on the on screen instructions

## How to Run Unittests for Project
1. Return to location where `Tests`, `Src`, and `Data` folders can be found.

2. To run all test cases/files use
    ```
    python -m unittest -v tests/test_*
    ```

3. To run individual test cases such as `test_contract_renewal.py` use
    ```
    python -m unittest -v tests/test_contract_renewal.py
    ```

4. For subsiquent runs of test cases replace `[Filename]` with the name of the file.
    ```
    python -m unittest -v tests/[filename]
    ```
