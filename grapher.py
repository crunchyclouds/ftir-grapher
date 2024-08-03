#importing relevant libraries
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import matplotlib


matplotlib.rcParams.update({'font.size': 18})

'''plots FTIR data'''

#ftir function
folder=r"D:\Data\FTIR\3-2_Comparisons"

#identifying csv files within the folder
files = [file for file in pathlib.Path(folder).glob("*.csv")]

#removing temporary files
for file in files:
    if "~" in str(file):
        files.remove(file)

#looping through all files
for file in files:
    print(f'Reading from {file}')
    print('Processing your files...')
    #reading excel data for cycle index and current capacity
    df = pd.read_csv(file,
                     header=1)
    print(df)
    y_axis = df['%T']
    x_axis = df['cm-1']

    #creating a plot
    series = str(pathlib.Path(file).stem)
    plt.xlim(4000,520) #reversed x-axis for display
    #plt.ylim(40,120)

    plt.plot(x_axis, y_axis,
             linewidth=3,
             marker='',
             label=series)
    plt.legend(loc='best')

    #informing user of status
    n=1
    print(f'Data set {n}/{len(files)} complete.')
    n+=1

#assigned constant values
plt.ylabel(r"% Transmittance")
plt.xlabel("FTIR Shift (cm^-1)")
plt.title(str(pathlib.Path(folder).stem))
plt.show()