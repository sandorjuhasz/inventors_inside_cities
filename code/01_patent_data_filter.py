import pandas as pd


# parameters
path_input_file = "data/geoc_inv.txt"
selected_country_code = "US"
period_start = 2011
period_end = 2020
path_output_file = f"outputs/geoc_inv_US_{period_start}_{period_end}.csv"


def filter_patent_data(data_path, country_code, period_start, period_end):
    """simple function to select and filter the original patent data"""
    df = pd.read_csv(data_path, sep=",")

    # keep inventors from the selected country
    df = df[df["ctry_code"] == country_code]

    # focus on selected time period
    df["date_column"] = pd.to_datetime(df["filing_date"])
    df["year"] = df["date_column"].dt.year
    df = df[(df["year"] >= period_start) & (df["year"] <= period_end)]

    return df


# filter and save
data_for_export = filter_patent_data(
    path_input_file, country_code="US", period_start=period_start, period_end=period_end
)
data_for_export.to_csv(path_output_file, sep=";", index=False)
