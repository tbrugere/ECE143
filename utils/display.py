"""Functions used to display data"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython.display import HTML

def top10(bill:pd.DataFrame, by:str="title", rank:str="rank", ax=None, **kwargs):
    """
    Display the top 10 titles that appear the most on given billboard.
    

    :param bill pd.DataFrame: the billboard data
    :param title str: the name of the title column
    :param rank str: the name of the rank column
    :param args: eventually write to an ax, otherwise call plt.figure()
    :param kwargs: passed to plt.figure()
    """
    kwargs["figsize"] = kwargs.get("figsize", (16,8))
    x = bill.groupby(by=by)[rank]\
        .count()\
        .sort_values(ascending=False)\
        .head(10) #type:ignore
    if ax is None:
        plt.figure(**kwargs)
        ax = sns.barplot(x=x.index, y=x)
    else:
        sns.barplot(x=x.index, y=x, ax=ax)
    # ax.set_title('Top 10 songs on billboard')
    ax.set_ylabel('Number of times')
    ax.set_xlabel(by)
    ax.tick_params(axis="x", labelrotation=0)
    return ax

def table_comparison(title, title_a, title_b, values_a, values_b):
    newline = "\n"
    return HTML(f"""
          <style>
            table, th, td {{
            border: 1px solid black;
            }}
            table {{
              border-collapse:collapse
            }}
          ul {{
              text-align: left;
              margin-right: 2em;
            }}
          </style>
          <br>
                <table style="border: 1px solid black; border-collapse:collapse"> 
            <tr>
              <th colspan=2>{title}</th>
            </tr>
            <tr>
               <th style="border: 1px solid black;">{title_a}</th>
               <th style="border: 1px solid black;">{title_b}</th>
            </tr>
            <tr>
              <td style="border: 1px solid black;">
                <ul>
                  {newline.join(f"<li>{feature}</li>" for feature in values_a)}
                </ul>
              </td>
              <td style="border: 1px solid black;">
                <ul>
                  {newline.join(f"<li>{feature}</li>" for feature in values_b)}
                </ul>
              </td>
            </tr> 

          """
      )
