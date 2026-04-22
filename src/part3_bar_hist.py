'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.

def barplot_fta(pred_universe):
    plt.figure()
    sns.countplot(data=pred_universe, x='fta')
    plt.title('Bar plot for fta column')
    plt.xlabel('fta')
    plt.ylabel('count')
    plt.savefig('data/part3_plots/barplot_fta.png', bbox_inches='tight')
    plt.close()

# 2. Hue the previous barplot by sex

def barplot_sex(pred_universe):
    plt.figure()
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    plt.title('Bar plot for sex column')
    plt.xlabel('fta')
    plt.ylabel('count')
    plt.savefig('data/part3_plots/barplot_sex.png', bbox_inches='tight')
    plt.close()

# 3. Plot a histogram of age_at_arrest

def histogram_age(pred_universe):
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.title('Histogram for age column')
    plt.xlabel('age_at_arrest')
    plt.ylabel('count')
    plt.savefig('data/part3_plots/histogram_age.png', bbox_inches='tight')
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 

def histogram_age_group(pred_universe):
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=[18,21,30,40,100])
    plt.title('Histogram for age group column')
    plt.xlabel('age_at_arrest')
    plt.ylabel('count')
    plt.savefig('data/part3_plots/histogram_age_group.png', bbox_inches='tight')
    plt.close()