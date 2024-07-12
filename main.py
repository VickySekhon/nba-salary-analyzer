import pandas as pd
import matplotlib.pyplot as plt

# Read data
nba_data = './nba.csv'
nba_df = pd.read_csv(nba_data)

wnba_data = './wnba.csv'
wnba_df = pd.read_csv(wnba_data)


# Initialize salary data
nba_salaries = nba_df["Salary"][0:166] # restrict to 166 nba stars to match wnba dataset
wnba_salaries = wnba_df["salary"]


# Calculations
total_nba_salaries = nba_salaries.sum()
total_wnba_salaries = wnba_salaries.sum()

print(f"""Total Salary Allocation
      NBA:  ${total_nba_salaries:>15,.2f}
      WNBA: ${total_wnba_salaries.astype(float):>14,.2f}
     """) # add commas and restrict formatting to 2 decimal places

highest_paid_nba_salary = nba_salaries.max()
highest_paid_nba_player = nba_df.loc[nba_df['Salary'].idxmax(), 'Name']

highest_paid_wnba_salary = wnba_salaries.max()
highest_paid_wnba_player = wnba_df.loc[wnba_df['salary'].idxmax(), 'player']

print(f"""Highest Paid Stars
      NBA:  
      Player: {highest_paid_nba_player}, Salary: ${highest_paid_nba_salary:>14,.2f}
      WNBA:
      Player: {highest_paid_wnba_player}, Salary: ${highest_paid_wnba_salary.astype(float):>11,.2f}
     """) # add commas and restrict formatting to 2 decimal places

lowest_paid_nba_salary = nba_salaries.min()
lowest_paid_nba_player = nba_df.loc[nba_df['Salary'].idxmin(), 'Name']

lowest_paid_wnba_salary = wnba_salaries.min()
lowest_paid_wnba_player = wnba_df.loc[wnba_df['salary'].idxmin(), 'player']

print(f"""Lowest Paid Stars
      NBA:  
      Player: {lowest_paid_nba_player}, Salary: ${lowest_paid_nba_salary:>10,.2f}
      WNBA:
      Player: {lowest_paid_wnba_player}, Salary: ${lowest_paid_wnba_salary.astype(float):>11,.2f}
     """) # add commas and restrict formatting to 2 decimal places

# NBA-specific calculations

average_paid_nba_salary = nba_salaries.mean()
print(f"""Average Paid NBA Star
     ${average_paid_nba_salary:>13,.2f}
     """)

median_paid_nba_salary = nba_salaries.median() 
print(f"""Median Salary of NBA Stars
     ${median_paid_nba_salary:>13,.2f}
     """)


# Plot a graph of all salaries

# determine graph type
bar = nba_df.plot.bar(x="Name", y="Salary", rot=0, color="#0000FF")

# Set labels and title
bar.set_xlabel("Player Names")
bar.set_ylabel("Salary ($)")
bar.set_title("Top 459 NBA Players' Salaries")

plt.show()