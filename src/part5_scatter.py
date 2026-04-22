'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

def lmplot1(merge_df):
    sns.lmplot(data=merge_df, x='prediction_felony',y='prediction_nonfelony',hue='has_felony_charge',fit_reg=False)
    
    plt.title('Felony vs Nonfelony Prediction')
    plt.savefig('data/part5_plots/felony_nonfelony.png', bbox_inches='tight')
    plt.close()

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?  

def lmplot2(merge_df):
    sns.lmplot(data=merge_df, x='prediction_felony',y='y_felony',fit_reg=False)
    
    plt.title('Felony vs Nonfelony Prediction')
    plt.savefig('data/part5_plots/felony_y_felony.png', bbox_inches='tight')
    plt.close()

    print('Would you say based off of this plot if the model is calibrated or not?')
    print('The model is not calibrated. The point doesnt show a clear upward trend')