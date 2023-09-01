# Learning data processing / pre processing
Data processing is the a broader term that encompasses all the operations and transformations persformed on data throughout the entire data lifecycle, from collection and preprocessing to analysis and reporting.
<br><br>
Pre processing is the initial step where you clean, organize, and transform raw data into a format that is suitable for analysis or machine learning.

## Table Of Content
* [Virtual Environment](#1-virtual-environment)
* [Required Library](#2-required-library)
* [Data processing / exploration](#3-data-processing--data-exploration-data-visualisation)
    - [Data imputation](#data-imputation)
    - [Data Correlation](#data-correlation)
    - [Multicollinearity](#multicollinearity)
    - [Convert categoricals values to munerical values](#convert-categoricals-values-to-munerical-values)
* [Data Balancing](#data-balancing)

## 1. Virtual environment

```code 
$ python -m venv {name of venv}
```

### Activate venv
#### Linux
```code 
$ source {name}/bin/activate 
```

#### window
```code
$ {name}/Scripts/activate
```

## 2. Required library
* pandas
* matplotlib
* seaborn
* scikit-learn

``` code
$ pip install pandas matplotlib seaborn scikit-learn
```

## 3. Data processing & Data exploration (Data visualisation)
Find patterns within the dataset to understand how it may affect the model in certain way at the same time find the relationship between variables.

### Data imputation
Refers to the procedure of using alternative value inplace of missing data.

### Data correlation
Find weakness and strength between variables in the dataset.

### Multicollinearity
Exists if an independant variable is highly correlated with one or more of the other indepandant variable.

### Convert categoricals values to munerical values
1. Binary Data (T/F or Y/N)
2. Oridinal Data (Got Ranking) - Label Encoding
    * Income level having elements as low, medium, high
    * School grade (A,B,C)
3. Nominal Data (No Ranking) - One Hot Encoding
    * HDB types
    * Reason for loan

## 4. Data Balancing
Data balancing is the process of ensuing that a machine learning dataset is representative of the real-world pupulation from which it it drawn.
Ensure that target variable is balenced.
1. Over-sampling
    - Used when the amount of data collect is insufficient. Supplementing the training data with multiple copies of some of the minority classes.
2. Under-sampling
    - Used when the amount of data is sufficient. Delete samples from the majority classes.
