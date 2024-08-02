# Spam/Ham Email Recognizer

## Project Overview

This program determines if a given email is a spam email or a ham email. The method used for spam filtering is Naïve Bayes Classifier with Laplace Smoothing, which is supervised learning, and is trained using the texts available inside the `/datasets` folder.

## How to run

1. Clone the repository and navigate to its location inside your computer.
2. Run the program inside the `/code` folder using the command `python3 main.py`.
3. The program will prompt the user to enter the value of `k`, which is the `smoothing factor` used for the laplace smoothing.
4. The program will then run through each .txt file inside the `classify` folder in the `datasets` directory and write a `classify.out` as an output. Each line in the output file contains the filename of the .txt file classified, its classification (ham/spam) and the computed probability.


