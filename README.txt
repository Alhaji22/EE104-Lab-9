Michael Low
Lab 6
________

Youtube demonstration for RFI, Trend Prediction, and Red Alert: https://youtu.be/Qn2oiESfQrA

Youtube demonstration for EMS vehicle with Ahaji Sharka: https://www.youtube.com/watch?v=COA1PdLWoVk
________
For the Risk Factor Identification (RFI.py) program the file it reads is the hmeq.csv file. 
The program saves the edited data with the risk analysis column to the hmeq1.csv file. 

RFI.py starts by loading the data and filling empty cells with 0's so that it can perform mathematical calculations with those cells.
Then it adds a new column to the dataframe titled "riskAnalysis".
The next thing is a for loop that iterates through each row and assigns a combined_risk value based on the numbers in the row. 
The functions to add up the risk are mostly arbitrary at this point. 
At the end of the for loop it adds the value of "low risk", "medium risk", or "high risk" to the riskAnalysis column.
The last portion of the program saves the data to hmeq1.csv
________
The trend_prediction.py program takes data from covid_data.csv 
It takes data from 4/1/2022 through 6/30/2022 to try to predict the next three months. 
Then it uses that data to create predictions for 1st, 2nd, and 3rd order polynomial models. 
The models are created for both New_cases and Total_cases. 

________
For Red Alert the following modules need to be installed by powershell:
-pip install pygame

The Red Alert game works by having stars scroll across the screen. 
You have to click the red star before it reaches the other edge of the screen. 
The first change I made was to add a random additional speed to each of the stars so that they scroll at different rates.
The second change was to add the option to restart the game at the end screen by pressing "spacebar". 
________
The code used for the EMS vehicle is in EMS_GPIO.ipynb
Run each cell until the first while loop to get it to function. 