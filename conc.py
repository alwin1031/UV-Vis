import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def pre_read(pre_df):
    for i in range(len(pre_df.iloc[:,0])):
        if pre_df.iloc[i,0] == 'Data Points':
            skip_line = i+2
            break
    return skip_line

def Abs280(df):
    for i in range(len(df)):
        if df["nm"][i] == 280: 
            print('A280 = {}'.format(df["Abs"][i]))
            top = round(df["Abs"][i], 1) + 0.1
            break
    return top

def Figure(df, top):
    fig, ax = plt.subplots(dpi=300, figsize=(8,6))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(width=1.8)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(1.8)
    font1 = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 18}
    font2 = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 26}
    plt.plot(df.nm, df.Abs, c="black", lw=1.2)
    plt.plot([250, 750], [0, 0], 'k:')
    plt.axis([250, 750, -top/10, round(top*11/10, 1)])   # [xmin, xmax, ymin, ymax]
    plt.xlabel("Wavelengh (nm)", fontdict=font1, labelpad=10)
    plt.ylabel("Absorbance (a.u.)", fontdict=font1, labelpad=10)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.subplots_adjust(bottom=0.14)
    plt.title(title, fontdict=font2, pad=20)

if __name__ == '__main__':
    import sys
    import os
    input_path = sys.argv[1]
    title = sys.argv[2]
    # Pre-read the excel to find where data start from
    pre_df = pd.read_excel(input_path)
    skip_line = pre_read(pre_df)
    # Import data
    df = pd.read_excel(input_path, skiprows=skip_line)
    input_path = os.path.splitext(input_path)[0]
    top = Abs280(df)
    Figure(df, top)

    plt.savefig(input_path+".png")
    print('Done! d(//-v-)b')
