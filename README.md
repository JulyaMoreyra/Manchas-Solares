# Sunspot Data Analysis
https://github.com/JulyaMoreyra/Manchas-Solares/assets/130570629/e681ac01-2a97-4e9c-a55e-a07b6f513a5a

## Project Description

This Python project is designed to analyze and process sunspot data from text files in an interactive matter with the user.

## Features
* **Data Import:** The program reads sunspot data from two text files (SN_d_tot_V2.0.txt for daily data and SN_m_tot_V2.0.txt for monthly averages) and processes the information into dictionaries for easy access.
* **Sunspot Analysis:** Provides functions to count the days without observed sunspots for a specified year and month.
* **Input Validation:** Ensures that the year entered by the user is within the valid range (1818-2018).

## Requirements
* Python 3.x

## How to Run
 1. Ensure the required text files (SN_d_tot_V2.0.txt and SN_m_tot_V2.0.txt) are in the same directory as the script.
 2. Run the script using a Python 3.x interpreter.
    ```
    python Trabalho_Programacao_de_Computadores.py
    ```
3. Follow the on-screen prompts to input the year and receive the analysis results.

## Functions
### funcao_1(ano)
* **Purpose:**
  
    This function is designed to count the days in each month of a specified year where no sunspots were observed.
* **Parameters:**
  
    * *ano (int):* The year you want to count the sunspot-free days.
* **Returns:**
  
    * *str_saida_dias_sem_mancha (str):* A string containing the output information, which includes the number of days without observed sunspots for each month of the given year.
* **Detailed Explanation:**
  
    The *funcao_1* function takes a year as an input and analyzes sunspot data to determine how many days in each month of that year had no recorded sunspots.

    The function checks if the input year is within the valid range (1818-2018) and prompts the user to correct the input if it is out of range.

    The result is returned as a formatted string detailing the sunspot-free days for each month.

#### funcao_1_1(ano)
* **Description:**
  
    This function counts the number of days in a given year where no data was collected on sunspots. It helps in identifying gaps in the sunspot observation data.
* **Parameters:**

  * *ano (int):* The year you want to count the days without sunspot data.
* **Returns:**

  * *str_saida_dias_sem_mancha (str):* A string that provides details about the days in the specified year where sunspot data was not collected.

### funcao_2()
* **Description:**

    This function determines the year and month with the highest number of days without sunspots.
  
    It analyzes the data to identify the month that had the fewest sunspots and outputs a formatted string with the results.

* **Parameters:**

    * *mes_sem_dado (str):* The month with the fewest sunspots.
    * *ano_mes_sem_dados (str):* The year corresponds to the month with the fewest sunspots.
    * *soma_mes (int):* The number of days without sunspots in a given month.
    * *soma_mes_sem_dado (int):* The month with the highest number of sunspot-free days.
    * *lista_mes (list):* A list containing the months with the fewest sunspot observations.
    * *lista_ano (list):* A list containing the years corresponding to the months in lista_mes.
    * *lista_mes_final (list):* A list containing the months written out in full.
* **Returns:**

    * *str_saida (str):* A formatted string indicating the month with the fewest sunspots and the corresponding year.
