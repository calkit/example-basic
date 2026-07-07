"""Plot our raw data."""

import json
import os

import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/raw/data.csv").set_index("time")
    ax = df.voltage.plot()
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/x-vs-y.png")
    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(
            {"mean": float(df.voltage.mean()), "std": float(df.voltage.std())},
            f,
            indent=2,
        )
