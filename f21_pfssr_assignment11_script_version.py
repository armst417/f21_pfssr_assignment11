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
# 




# PROBLEM 1
#
# Now let's get to programming
#
# a) Import any helpful libraries
#
# b) Load the MA_Public_Schools_2017.csv file as a pandas data frame. Note: these data are from Kaggle: https://www.kaggle.com/ndalziel/massachusetts-public-schools-data and I have already removed a lot of columns.
import pandas as pd # Importing that pandas package. 
MAPS_2017 = pd.read_csv('MA_Public_Schools_2017.csv') # This can be read as long as you are in the same directory as the Python file.
# c) Adapt the example code in the chunk below to replace all spaces in column names with underscores. This is good practice in order to not cause problems with functions that don't allow spaces in variable names (e.g., smf.ols).

# starter code for 1c -- replace school_data w/ your dataframe name
MAPS_2017.columns = MAPS_2017.columns.str.replace(' ', '_') # notice this replaces the 1st argument w/ the 2nd

# d) Adapt the code from 1c to replace "%" sign with "Perc", because it is also good practice not to start column names with symbols.

MAPS_2017.columns = MAPS_2017.columns.str.replace('%', 'Perc') # replaces % with Perc

# e) Find the descriptives for numeric columns.

# Below prints the descriptive stats for the numerical columns
print('Descriptive stats for several: \n', MAPS_2017[['PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment','3_Enrollment','4_Enrollment', '5_Enrollment', '6_Enrollment', '7_Enrollment', '8_Enrollment', '9_Enrollment', '10_Enrollment', '11_Enrollment', '12_Enrollment', 'SP_Enrollment', 'Perc_First_Language_Not_English', 'Perc_English_Language_Learner', 'Perc_Students_With_Disabilities', 'Perc_High_Needs', 'Perc_Economically_Disadvantaged', 'Perc_African_American', 'Perc_Asian', 'Perc_Hispanic', 'Perc_White',	'Perc_Native_American', 'Perc_Native_Hawaiian,_Pacific_Islander', 'Perc_Multi-Race,_Non-Hispanic', 'Perc_Males', 'Perc_Females', 'Average_Class_Size', 'Number_of_Students', 'Salary_Totals', 'Average_Salary', 'FTE_Count', 'In-District_Expenditures', 'Total_In-district_FTEs', 'Average_In-District_Expenditures_per_Pupil', 'Total_Expenditures', 'Total_Pupil_FTEs', 'Average_Expenditures_per_Pupil']].describe())
# Below saves the descriptive stats for the numerical columns.
descriptiveMAPS2017 = MAPS_2017[['PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment','3_Enrollment','4_Enrollment', '5_Enrollment', '6_Enrollment', '7_Enrollment', '8_Enrollment', '9_Enrollment', '10_Enrollment', '11_Enrollment', '12_Enrollment', 'SP_Enrollment', 'Perc_First_Language_Not_English', 'Perc_English_Language_Learner', 'Perc_Students_With_Disabilities', 'Perc_High_Needs', 'Perc_Economically_Disadvantaged', 'Perc_African_American', 'Perc_Asian', 'Perc_Hispanic', 'Perc_White',	'Perc_Native_American', 'Perc_Native_Hawaiian,_Pacific_Islander', 'Perc_Multi-Race,_Non-Hispanic', 'Perc_Males', 'Perc_Females', 'Average_Class_Size', 'Number_of_Students', 'Salary_Totals', 'Average_Salary', 'FTE_Count', 'In-District_Expenditures', 'Total_In-district_FTEs', 'Average_In-District_Expenditures_per_Pupil', 'Total_Expenditures', 'Total_Pupil_FTEs', 'Average_Expenditures_per_Pupil']].describe()


# f) Commit your changes and push to GitHub!

# Ok, I see the change on my GitHub page now!






# PROBLEM 2
#

# a) Remove the District Code column.
MAPS_2017_noDC = MAPS_2017.drop('District_Code',1) # This drops just the district code column - https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe 
print('No district column:\n',MAPS_2017_noDC)  # Double checks that I dropped the district column.



# b) Create a new column called "TOTAL_Enrollment" that is the sum of all columns that end in "Enrollment".

# Below, I'm just creating a dataframe that only has the enrollment columns.
MAPS_2017_noDC_byColumn = MAPS_2017_noDC[['PK_Enrollment', 'K_Enrollment', '1_Enrollment', '2_Enrollment','3_Enrollment','4_Enrollment', '5_Enrollment', '6_Enrollment', '7_Enrollment', '8_Enrollment', '9_Enrollment', '10_Enrollment', '11_Enrollment', '12_Enrollment', 'SP_Enrollment']]
# Below, I add a new colum to the MAPS_2017_noDC dataframe that sums the enrollment from each grade to find the total enrollment in the district.
MAPS_2017_noDC['Total_Enrollment'] = MAPS_2017_noDC_byColumn.sum(axis=1) # Creating the total enrollment column such that each row is the total sum enrollment.
print(MAPS_2017_noDC) # Prints to terminal so I can check the data frame.

# c) Compute the mean of "TOTAL_Enrollment" for each District. (Hint: groupby)

# I have two interpretations of this problem. 
# INPTRETATION 1: The first interpretation was that I thought this problem might be asking to calculate
# the mean enrollment of all the Massachusetts districts included in the data set:

mean_totalE = MAPS_2017_noDC['Total_Enrollment'].mean() # Calculates the mean total enrollment from all districts.
print(mean_totalE) # Mean is 512.492208490059 students enrolled in a district.

# INTERPRETATION 2: My other interpretation was that this question is asking about the mean enrollment of each grade from each district:
## --> Note that I didn't use groupby here because I already made a dataframe with just the enrollment columns by grade.
MAPS_2017_noDC['Mean_Enrollment_by_Grade'] = MAPS_2017_noDC_byColumn.mean(axis=1) # For each district, finds the mean enrollment across all grades.
                                                                                    # I could have also divided the Total_Enrollment row by 15.
print(MAPS_2017_noDC)



# d) Commit your changes and push to GitHub!

# Did it! :)





# PROBLEM 3
#
# a) Visualize each bivariate relationship among Average_Class_Size, Average_Salary, Perc_Economically_Disadvantaged, and Perc_English_Language_Learner. Use the Seaborn function pairplot. The argument to pairplot should be school_data[['Average_Class_Size', 'Average_Salary', 'Perc_Economically_Disadvantaged', 'Perc_English_Language_Learner']], which will just pull those columns out from the full data frame.
import seaborn as sns # Importing seaborn
MAPS_2017_dataForGraph = MAPS_2017[['Average_Class_Size', 'Average_Salary', 'Perc_Economically_Disadvantaged', 'Perc_English_Language_Learner']] # Creating a data frame to use in graph.
print(MAPS_2017_dataForGraph) # Double checking my data frame is correct.

plot_MAPS_2017 = sns.pairplot(MAPS_2017_dataForGraph) # Creating pairplot.
plot_MAPS_2017.savefig("MAPS_2017_PairPlot.png") # Saving figure to my computer.
plot_MAPS_2017.fig.clf() # Clearing the figure so I can create a new one if needed.

# b) Describe what you see from the plots.

# The graphs along the diagonal from the upper left to the lower right corner are histograms. All other graphs are scatterplots.
# This makes sense since we are only graphing 1 numerical column instead of two along the diagonal of the pairplot.

# I see that the average class size is approximately normal/bell-shaped. 
# Furthermore, it looks like average salary in a district is multimodal. 
# The distribution for the % economically disadvantaged is skewed right, meaning more schools have a lower percent of 
# economically disadvantaged students.
# The % English language learners (ELLs) looks to be highly skewed right, meaning fewer schools have a very high % of ELLs.

# All of my scatterplots just have clusters of data, making it is difficult to discern any clear patterns.
# However, it looks like there might be a very weak relationship between % ELL and % economically disadvantaged.


# c) Based on your observations from 3b, and as a completely post-hoc, exploratory analysis, choose one of the 4 measures from 3a to be an outcome variable, and a second measure to be a predictor variable. Then run a linear regression, print the summary, and write a sentence interpreting the results (does not need to be detailed, just practice retrieving the relevant info on predictor significance, etc.)

# Again the data from my pairplot() was difficult to discern any clear linear relationships.

# However, I think % English language learners vs. % economically disadvantaged might show a weak linear relationship.
MAPS_2017_LinearReg = sns.regplot(x="Perc_English_Language_Learner", y="Perc_Economically_Disadvantaged", data=MAPS_2017) # Setting up linear regression plot.
MAPS_2017_LinearReg.set_title("Percent English Language Learner vs. Percent Economically Disadvantaged") # Setting title of linear regression plot.
MAPS_2017_LinearReg.get_figure().savefig("MAPS_2017_LinearReg.png") # Getting the plot and saving it to my computer.
MAPS_2017_LinearReg.clear() # Clearing the plot in case I want to create a new one.

# Below, I am importing matplotlib.pyplot, scipy.stats, and statsmodels.formula.api
import statsmodels.formula.api as smf # Downloading statsmodels.formula.api in order to generate a description of the linear model.
lm = smf.ols(formula = "Perc_Economically_Disadvantaged ~ Perc_English_Language_Learner", data = MAPS_2017).fit() # ELLs as independent and % economically disadvantaged as dependent.
summary_lm = lm.summary() # Saving the linear model for this data as summary_lm
print(summary_lm) # Printing the summary to my terminal when I run this code.

# We see the R^2 value is 0.367, indicating a weak positive relationship between % ELL and % economically disadvantaged.
# This also means that approximately 36.7% of the variation in % economically disadvantaged can be explained by %ELL.
# Although this is not a reliable predictor based on this very weak, positive relationship, the equation of the line
# suggests that for every 1 percent increase in % ELL, there is, on average, an approximate 0.3561% increase in % economically
# disadvantaged (however, we see that this is a weak linear relationship; therefore, this interpretation isn't very useful).   

# d) Commit your changes and push to GitHub!

# Done!







#
# PROBLEM 4
#
# a) Create a new linear regression model that takes the model from 3c and adds both of the remaining variables from 3a as additional predictor variables. To do this, the formula interface would look like "outcome_name ~ predictor1_name + predictor2_name + predictor3_name"

# Below, I am creating a new linear model as described in 4(a) & calleding it lm2
lm2 = smf.ols(formula = "Perc_Economically_Disadvantaged ~  Perc_English_Language_Learner + Average_Class_Size + Average_Salary", data = MAPS_2017).fit()

 
# b) Print the summary from 4a, and write a short interpretation of the results, especially comparing it to Problem 3c.

summary_lm2 = lm2.summary() # Saving the summary statistics as summary_lm2
print(f"Below are the linear model results for 4(b):\n{summary_lm2}") # Printing the summary statistics in my terminal.

# The R-squared value for this linear model is 0.485, which is larger than what I got in 3(c). This means that approximately
# 48.5% of the variation in % economically disadvantaged can be explained by the independent variables. However, this is still
# a fairly weak correlation.



# c) Add School_Type as another predictor to your model. Interpret the new predictor in your output. How is it different from the other predictors?

lm3 = smf.ols(formula = "Perc_Economically_Disadvantaged ~ Perc_English_Language_Learner + Average_Class_Size + Average_Salary + School_Type", data = MAPS_2017).fit() # Adding School_Type
summary_lm3 = lm3.summary() # Saving the summary of lm3
print(summary_lm3) # Printing the summary to my terminal

# School_Type contains categorical data instead of numeric data. I noticed the variable School_Type[T.Public School] has all the same information listed as
# the row titled Intercept. Since it is instead categorical and not something we graph, I think it just repeats the intercept information but will not be taken into
# account in the linear regression model equation in the same way (i.e., the 47.7140 does not mean it is a coefficient in front of the school type variable). 
# Also, since the variable is titled School_Type[T.Public School], I wonder how I can obtain the charter school information, since I am assuming this is a multiple regression
# model just for public schools?

# d) Commit your changes and push to GitHub!
#



# Problem 5
#
# a) Make sure this Python script is saved.
#
# b) Stage, commit, and push all changes to your GitHub repository.
#
# c) Submit a link to your repository as your submission for the assignment on Canvas. Remember the note from Problem 0: you can keep your repo private and add me as a collaborator.
