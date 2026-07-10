"""This script collects data.

We sweep the input :math:`x` and measure the system response :math:`y`,
which follows a noisy quadratic relationship :math:`y = x^2`.
"""

import os

import numpy as np
import pandas as pd

rng = np.random.default_rng(4545)

x = np.linspace(0, 10, 200)
y = x**2 + rng.normal(scale=4.0, size=x.shape)

df = pd.DataFrame(data={"x": x, "y": y})
os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/data.csv", index=False)
