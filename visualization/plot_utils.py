import matplotlib.pyplot as plt

def plot_moving_average(data, column, window):
    """
    Plots moving average for a specified column.
    """
    data[f"{column}_ma"] = data[column].rolling(window=window).mean()
    plt.figure(figsize=(10, 6))
    plt.plot(data["date"], data[column], label="Actual")
    plt.plot(data["date"], data[f"{column}_ma"], label=f"{window}-Day Moving Average", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.legend()
    plt.title(f"Moving Average Plot for {column}")
    plt.show()
