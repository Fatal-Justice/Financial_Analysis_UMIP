import pandas as pd
import csv
import sys
import matplotlib.pyplot as plt

def main():
  # Read the CSV file
  df = pd.read_csv(input('File Name: '))
  # Renaming Columns
  df.columns=['S.No.','Name','Mcap-Cr','Sales Qtr-Cr','Extra']
  # Cleaning data
  df['Sales Qtr-Cr' ]=df['Sales Qtr-Cr'].fillna(0)
  # List of index having sales qtr cr 0 but values are accidently in Extra Column. hence filing values from Extra to Sales where sales are zero.
  index_list=df.index[df['Sales Qtr-Cr']==0].tolist()
  for i in index_list:
    df.loc[i,'Sales Qtr-Cr']=df.loc[i,'Extra']
  # Calculate Ratio of Market cap and sales
  df['Mcap/Sales']=df['Mcap-Cr']/df['Sales Qtr-Cr']
  # Writing data to csv
  df.to_csv('Biodata.csv', index=False)
  df1=df.sort_values(by='Mcap/Sales', ascending=True)
  df1=df1[df1['Mcap/Sales']>0]
  df1.to_csv('Biodata_sort.csv', index=False)
  print(df1.tail(5))
  print(df1.head(5))

  # Plotting scatter plot for Mcap vs Mcap/Sales leaving outliers in Mcap
  df[df['Mcap/Sales']<100].plot.scatter(x='Mcap-Cr', y='Mcap/Sales')
  #df.loc[df['Mcap/Sales']<40,'Mcap/Sales'].plot.box()
  plt.savefig("scatterplot.jpg")

  # Plotting scatter plot for Mcap vs Mcap/Sales leaving outliers in Mcap
  df[(df['Mcap/Sales']<60) & (df['Mcap-Cr']< 10000)].plot.scatter(x='Mcap-Cr', y='Mcap/Sales')
  #plt.show()
  plt.savefig("scatterplot1.jpg")
  
  
  # Histogram of Mcap-Cr vs Mcap/Sales
  n_bins=20
  fig, axs = plt.subplots(1,2)
  axs[0].set_xlabel('Mcap-Cr')
  axs[0].hist(df['Mcap-Cr'], bins=n_bins)
  axs[1].set_xlabel('Mcap/Sales')
  axs[1].hist(df.loc[df['Mcap/Sales']<100,'Mcap/Sales'], bins=n_bins)
  plt.savefig("histogram.jpg")
  sys.exit()

if __name__=='__main__':
  main()
