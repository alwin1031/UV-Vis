import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def pre_read(pre_df):
    for i in range(len(pre_df.iloc[:,0])):
        if pre_df.iloc[i,0] == 'Data Points':
            skip_line = i+2
            break
    return skip_line

def A280Nor_Conc(df):
    # A280 (No.941) normalize to 1
    A280_Abs = [x/df["Abs"][941] for x in df["Abs"]]
    
    return A280_Abs

def MaxNor_Conc(df):    
    Max_Abs = [x/max(df["Abs"]) for x in df["Abs"]]    
    return Max_Abs

def Base_Conc(df):
    # Baseline (non-negative figure)
    baseline = [x-abs(min(df["Abs"])) for x in df["Abs"]]
    return baseline

# Figure parameters
def plot(df, type_what):
    plt.plot(df["nm"], type_what,c = "black", lw=0.5)
    plt.axis([250, 750, -0.5, 2]) # [xmin, xmax, ymin, ymax]
    plt.xlabel("Wavelengh (nm)", fontweight = "bold")
    plt.ylabel("Absorbance (a.u.)", fontweight = "bold")
    # plt.title("Here is the Title", fontsize = 15, fontweight = "bold", y = 1)

if __name__ == '__main__':
    import sys
    import os
    input_path = sys.argv[1]
    # Pre-read the excel to find where data start from
    pre_df = pd.read_excel(input_path)
    skip_line = pre_read(pre_df)
    # Import data
    df = pd.read_excel(input_path, skiprows=skip_line)
    input_path = os.path.splitext(input_path)[0]
    os.mkdir(input_path)
    # Plot original concentration data
    plot(df, df)
    plt.savefig('{}/{}_Original_Conc.png'.format(input_path, input_path))
    plt.show(block=False)
    plt.close()
    # Plot A280 normalized data
    plot(df, A280Nor_Conc(df))
    plt.savefig('{}/{}_A280Nor_Conc.png'.format(input_path, input_path))
    plt.show(block=False)
    plt.close()
    # Plot maximum normalized data
    plot(df, MaxNor_Conc(df))
    plt.savefig('{}/{}_MaxNor_Conc.png'.format(input_path, input_path))
    plt.show(block=False)
    plt.close()
    # Plot baseline concentration data
    plot(df, Base_Conc(df))
    plt.savefig('{}/{}_Base_Conc.png'.format(input_path, input_path))
    plt.show(block=False)
    plt.close()
