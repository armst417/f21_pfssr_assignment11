# EPSY 5122: Programming for Social Science Researchers
# Assignment 11
# Due Wednesday, December 1 by 2:30pm

# Problem 0
#
# If you've made it to this document, you likely already did Problem 0 from the readme. But just in case, here it is again!
#
# a) Let's watch some videos! I recommend all the videos in this series (for future learning), but we will just focus on two now. Watch the first half of this video (https://www.youtube.com/watch?v=_NrSWLQsDL4&list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV&index=3) -- just the part about forking, you can ignore pull requests! Then watch this video: https://www.youtube.com/watch?v=yXT1ElMEkW8&list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV&index=6 (you don't have to do the terminal git commands, you can use the clone strategy we used in class)
#
# b) Using what you learned in 0a, fork my GitHub repository (remote repo) to your own account, then clone to your hard drive (local repo) using GitKraken (or use the command-line if you want the extra challenge). After finishing EACH problem below, make sure to STAGE and COMMIT with a comment (e.g., "Just finished Part 1! Git is fun!" or whatever). Then PUSH back to GitHub.
# Note on privacy!
#
# By default, GitHub repos are public (promoting open source sharing of code), but of course you are more than welcome to make your code for this assignment private, as is your right! Unfortunately, it's a little bit complicated because GitKraken recently made a change that the free version of their software doesn't allow for private repo access, and you need the paid version. So here are 3 ways to do this privately:
#
# 1) GitKraken partners with GitHub to provide a free pack of resources (including the pro version of GitKraken) for students. That's you! So you can sign up here only if you want to do this: https://education.github.com/pack?utm_source=github+gitkraken
#
# 2) Just keep your GitHub repo public while you're working on this project. Use free GitKraken. Then switch the GitHub repo to Private only when you're done using GitKraken to push to GitHub.
#
# 3) Keep the repo private and use the terminal git commands in the YouTube video for Problem 0a.
#
# To make the repo private: On your GitHub repo, go to Settings > Manage Access > Manage (under Public Repository) > Change Visibility. Then add me (jkbye) as a 'collaborator' so I can see it: Settings > Manage Access > Invite a Collaborator (green button) > add 'jkbye'.
# Problem 1
#
# Now let's get to programming
#
# a) Import any helpful libraries
#
# b) Load the MA_Public_Schools_2017.csv file as a pandas data frame. Note: these data are from Kaggle: https://www.kaggle.com/ndalziel/massachusetts-public-schools-data and I have already removed a lot of columns.
import pandas as pd # Importing that pandas package so that I can 
MAPS_2017 = pd.read_csv('MA_Public_Schools_2017.csv')
# c) Adapt the example code in the chunk below to replace all spaces in column names with underscores. This is good practice in order to not cause problems with functions that don't allow spaces in variable names (e.g., smf.ols).

# starter code for 1c -- replace school_data w/ your dataframe name
MAPS_2017.columns = MAPS_2017.columns.str.replace(' ', '_') # notice this replaces the 1st argument w/ the 2nd

# d) Adapt the code from 1c to replace "%" sign with "Perc", because it is also good practice not to start column names with symbols.

MAPS_2017.columns = MAPS_2017.columns.str.replace('%', 'Perc') # replaces % with Perc

# e) Find the descriptives for numeric columns.

print('Descriptive stats for several: \n', MAPS_2017[['PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment','3_Enrollment','4_Enrollment', '5_Enrollment', '6_Enrollment', '7_Enrollment', '8_Enrollment', '9_Enrollment', '10_Enrollment', '11_Enrollment', '12_Enrollment', 'SP_Enrollment', 'Perc_First_Language_Not_English', 'Perc_English_Language_Learner', 'Perc_Students_With_Disabilities', 'Perc_High_Needs', 'Perc_Economically_Disadvantaged', 'Perc_African_American', 'Perc_Asian', 'Perc_Hispanic', 'Perc_White',	'Perc_Native_American', 'Perc_Native_Hawaiian,_Pacific_Islander', 'Perc_Multi-Race,_Non-Hispanic', 'Perc_Males', 'Perc_Females', 'Average_Class_Size', 'Number_of_Students', 'Salary_Totals', 'Average_Salary', 'FTE_Count', 'In-District_Expenditures', 'Total_In-district_FTEs', 'Average_In-District_Expenditures_per_Pupil', 'Total_Expenditures', 'Total_Pupil_FTEs', 'Average_Expenditures_per_Pupil']].describe())

descriptiveMAPS2017 = MAPS_2017[['PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment','3_Enrollment','4_Enrollment', '5_Enrollment', '6_Enrollment', '7_Enrollment', '8_Enrollment', '9_Enrollment', '10_Enrollment', '11_Enrollment', '12_Enrollment', 'SP_Enrollment', 'Perc_First_Language_Not_English', 'Perc_English_Language_Learner', 'Perc_Students_With_Disabilities', 'Perc_High_Needs', 'Perc_Economically_Disadvantaged', 'Perc_African_American', 'Perc_Asian', 'Perc_Hispanic', 'Perc_White',	'Perc_Native_American', 'Perc_Native_Hawaiian,_Pacific_Islander', 'Perc_Multi-Race,_Non-Hispanic', 'Perc_Males', 'Perc_Females', 'Average_Class_Size', 'Number_of_Students', 'Salary_Totals', 'Average_Salary', 'FTE_Count', 'In-District_Expenditures', 'Total_In-district_FTEs', 'Average_In-District_Expenditures_per_Pupil', 'Total_Expenditures', 'Total_Pupil_FTEs', 'Average_Expenditures_per_Pupil']].describe()

#
# f) Commit your changes and push to GitHub!

# Ok, I see the change on my GitHub page now!



# Problem 2
#
# a) Remove the District Code column.
MAPS_2017_noDC = MAPS_2017.drop('District_Code',1) # This drops just the district code column - https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe 
print('No district column:\n',MAPS_2017_noDC) 
#
# b) Create a new column called "TOTAL_Enrollment" that is the sum of all columns that end in "Enrollment".

# Below, I'm just creating a dataframe that only has the enrollment columns.
MAPS_2017_noDC_byColumn = MAPS_2017_noDC[['PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment','3_Enrollment','4_Enrollment', '5_Enrollment', '6_Enrollment', '7_Enrollment', '8_Enrollment', '9_Enrollment', '10_Enrollment', '11_Enrollment', '12_Enrollment', 'SP_Enrollment']]
# Below, I add a new colum to the MAPS_2017_noDC dataframe that sums the enrollment from each grade to find the total enrollment in the district.
MAPS_2017_noDC['Total_Enrollment'] = MAPS_2017_noDC_byColumn.sum(axis=1)
print(MAPS_2017_noDC)
# c) Compute the mean of "TOTAL_Enrollment" for each District. (Hint: groupby)

# I have two interpretations of this problem. The first interpretation was that I thought this meant to calculate
# the mean enrollment of all the Massachusetts districts included in the data set:

mean_totalE = MAPS_2017_noDC['Total_Enrollment'].mean() # Calculates the mean total enrollment from all districts.
print(mean_totalE) # Mean is 512.492208490059.

# My other interpretation was that this question is asking about the mean enrollment of each grade from each district:
## --> Note that I didn't use groupby here because I already made a dataframe with just the enrollment columns by grade.
MAPS_2017_noDC['Mean_Enrollment_by_Grade'] = MAPS_2017_noDC_byColumn.mean(axis=1) # For each district, finds the mean enrollment across all grades.
                                                                                    # I could have also divided the Total_Enrollment row by 15.
print(MAPS_2017_noDC)

# d) Commit your changes and push to GitHub!

# Did it! :)


# Problem 3
#
# a) Visualize each bivariate relationship among Average_Class_Size, Average_Salary, Perc_Economically_Disadvantaged, and Perc_English_Language_Learner. Use the Seaborn function pairplot. The argument to pairplot should be school_data[['Average_Class_Size', 'Average_Salary', 'Perc_Economically_Disadvantaged', 'Perc_English_Language_Learner']], which will just pull those columns out from the full data frame.
import seaborn as sns
MAPS_2017_dataForGraph = MAPS_2017[['Average_Class_Size', 'Average_Salary', 'Perc_Economically_Disadvantaged', 'Perc_English_Language_Learner']]
print(MAPS_2017_dataForGraph)

plot_MAPS_2017 = sns.pairplot(MAPS_2017_dataForGraph)
plot_MAPS_2017.savefig("MAPS_2017_PairPlot.png")
plot_MAPS_2017.fig.clf()
# b) Describe what you see from the plots.

# The data along the diagonal from the upper left to the lower right corner is itself against itself looks to instead create histograms?
# This would make sense since we are only graphing 1 numerical column instead of two against one another.
# If my assumption here is correct, I see that the average class size is approximately normal/bell-shaped. 
# Furthermore, it looks like average salary in a district is multimodal. Likely, there are some highly paid admin.
# The distribution for the % economically disadvantaged is skewed right, meaning more schools have a lower percent of 
# economically disadvantaged students.
# The % English language learners looks to be highly skewed right, meaning fewer schools have a very high % of 
# economically disadvantaged students.

# All of my scatterplots just have clusters of data and it is difficult in my diagrams to discern
# specific patterns. It looks like there might be a weak relationship between % ELL and % economically disadvantaged.


# c) Based on your observations from 3b, and as a completely post-hoc, exploratory analysis, choose one of the 4 measures from 3a to be an outcome variable, and a second measure to be a predictor variable. Then run a linear regression, print the summary, and write a sentence interpreting the results (does not need to be detailed, just practice retrieving the relevant info on predictor significance, etc.)

# Again the data from my pairplot() was difficult to discern any clear linear relationships.

# However, I think % English language learners vs. % economically disadvantaged might show a weak linear relationship.
MAPS_2017_LinearReg = sns.regplot(x="Perc_English_Language_Learner", y="Perc_Economically_Disadvantaged", data=MAPS_2017)
MAPS_2017_LinearReg.set_title("Percent English Language Learner vs. Percent Economically Disadvantaged")
MAPS_2017_LinearReg.get_figure().savefig("MAPS_2017_LinearReg.png")
MAPS_2017_LinearReg.clear()
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.formula.api as smf
lm = smf.ols(formula = "Perc_English_Language_Learner ~ Perc_Economically_Disadvantaged", data = MAPS_2017).fit()
summary_lm = lm.summary()
print(summary_lm)

# We see the R^2 value is 0.367, indicating a weak positive relationship between % ELL and % economically disadvantaged.
# This also means that approximately 36.7% of the variation in % economically disadvantaged can be explained by %ELL.
# Although this is not a reliable predictor based on this very weak, positive relationship, the equation of the line
# suggests that for every 1 percent increase in % ELL, there is, on average, an approximate 0.3561% increase in % economically
# disadvantaged.   

# d) Commit your changes and push to GitHub!



# 
# Problem 4
#
# a) Create a new linear regression model that takes the model from 3c and adds both of the remaining variables from 3a as additional predictor variables. To do this, the formula interface would look like "outcome_name ~ predictor1_name + predictor2_name + predictor3_name"
#
# b) Print the summary from 4a, and write a short interpretation of the results, especially comparing it to Problem 3c.
#
# c) Add School_Type as another predictor to your model. Interpret the new predictor in your output. How is it different from the other predictors?
#
# d) Commit your changes and push to GitHub!
#
# # Problem 4 code here (can split into multiple code chunks if you want)
#
# Problem 5
#
# a) Make sure this Python script is saved.
#
# b) Stage, commit, and push all changes to your GitHub repository.
#
# c) Submit a link to your repository as your submission for the assignment on Canvas. Remember the note from Problem 0: you can keep your repo private and add me as a collaborator.
