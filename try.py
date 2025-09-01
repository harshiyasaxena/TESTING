import re
import pandas as pd

def process_excel(input_file, output_file):
    # Read Excel
    df = pd.read_excel(input_file, engine="openpyxl")

    # Ensure Hours column exists
    if "Hours" not in df.columns:
        raise ValueError("The Excel file must contain a column named 'Hours'.")

    # Insert Minutes column after Hours
    hours_index = df.columns.get_loc("Hours")
    df.insert(hours_index + 1, "Minutes", df["Hours"] * 60)

    # Add US and DA columns at the end (start with 0)
    df["US"] = 0.0
    df["DA"] = 0.0

    # Regex to detect sequences
    pattern = re.compile(r"\b\d{8}[A-Z]?\b")

    # Function to count valid sequences
    def count_sequences(text):
        if pd.isna(text):
            return 0
        return len(pattern.findall(str(text)))

    # Step 1: compute row-level US/DA values
    for i, row in df.iterrows():
        text = str(row.get("HEHEHE", ""))
        minutes = row["Minutes"]

        if "US" in text:
            c = count_sequences(text)
            if c > 0:
                df.at[i, "US"] = minutes / c

        if "DA" in text:
            c = count_sequences(text)
            if c > 0:
                df.at[i, "DA"] = minutes / c

    # Step 2: cumulative totals within same Employee + Date
    if "Employee" in df.columns and "Date" in df.columns:
        df[["US", "DA"]] = (
            df.groupby(["Employee", "Date"])[["US", "DA"]]
              .cumsum()   # cumulative sum
        )

    # Save result
    df.to_excel(output_file, index=False, engine="openpyxl")


if __name__ == "__main__":
    input_file = "From.xlsx"   # your input file
    output_file = "Transformed.xlsx"
    process_excel(input_file, output_file)
    print(f"Transformed file saved as {output_file}")

// changes
