"""
TYPES OF INTERPOLATION:-
    3. SPLINE:-
        SMOOOTH CURVES (VERY ADVANCED)  REQUIRES Scipy
        LESS OVERFITTING THAN HIGH-DEGREE POLYNOMIAL
    Used in:
        Physics simulations
        Signal processing
        Biomedical data
    SYNTAX:- df.interpolate(method='spline', order-2)

    4. TIME:-
        TIME SERIES SPECIFIC
        USES ACTUAL TIME GAPS
        NOT EQUAL SPACING ASSUMPTION
    Use cases:
        Stock prices
        Weather data
        IoT sensors
        Logs
    SYNTAX:- df.interpolate(method='time')
"""

import pandas as pd

# TIME INTERPOLATION EXAMPLE
dates = pd.date_range("2025-01-01", periods=5)

data = {
    "Temperature": [20, None, 26, None, 30]
}
df = pd.DataFrame(data, index=dates)
print("SAMPLE DATAFRAME:-")
print(df)

df["Temperature"] = df["Temperature"].interpolate(method="time")
print("\nAFTER TIME INTERPOLATION:-")
print(df)
print()


# SPLINE INTERPOLATION EXAMPLE
data2 = {
    "Sensor": [10, None, 25, None, 60]
}
df2 = pd.DataFrame(data2)
print("SAMPLE DATAFRAME:-")
print(df2)

df2["Sensor"] = df2["Sensor"].interpolate(method="spline", order=2)
print("\nAFTER SPLINE INTERPOLATION:-")
print(df2)

