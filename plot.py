from tkinter import Grid
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np


def line_plot(weeks, attributes, city, category):

    plt.style.use('seaborn-dark')

    fig, ax = plt.subplots(figsize=(8,6))
    ax.set(autoscale_on=True)

    plt.plot_date(weeks, attributes)
    plt.gcf().autofmt_xdate
    date_format = mpl_dates.DateFormatter('%b, %d, %Y')
    plt.gca().xaxis.set_major_formatter(date_format)
   
    ax.set_xlabel('Week')
    ax.set_ylabel(category)
    ax.set_title(f'{category} for {city}')

    fig.autofmt_xdate(rotation=45)
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    fig.savefig('time_plot.png')