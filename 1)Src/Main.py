import argparse
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)


def generate_csv_graph(file_path: str, x_col: str, y_col: str, output_name: str, graph_type: str = "line"):
    """Automates CSV data visualization.

    Parameters:
    file_path: Path to the CSV file.
    x_col: Column name for the X axis.
    y_col: Column name for the Y axis (numeric).
    output_name: Path to the output PNG file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded CSV file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to read CSV '{file_path}': {e}")

    if df.empty:
        raise ValueError("CSV file is empty")

    if x_col not in df.columns or y_col not in df.columns:
        raise KeyError(
            f"Required columns not found. Available: {list(df.columns)}")

    # Keep only rows where x and y are present
    df = df.dropna(subset=[x_col, y_col])
    logging.info(f"Rows after cleaning: {len(df)}")

    # Convert y to numeric and fail if no numeric values
    df = df.copy()
    df[y_col] = pd.to_numeric(df[y_col], errors="coerce")
    if df[y_col].isnull().all():
        raise ValueError(f"No numeric data found in column '{y_col}'")

    # Set the canvas size for the graph
    plt.figure(figsize=(6, 4))
    # --- GRAPH TYPE SELECTION LOGIC ---
    allowed_graphs = {"line", "bar", "scatter"}
    if graph_type not in allowed_graphs:
        raise ValueError(f"graph_type must be one of {allowed_graphs}")
    if graph_type == "line":
        plt.plot(df[x_col], df[y_col], marker='o')
    elif graph_type == "bar":
        plt.bar(df[x_col], df[y_col], color='skyblue', edgecolor='navy')
    elif graph_type == "scatter":
        plt.scatter(df[x_col], df[y_col], color='purple', alpha=0.7)
    # Label the axes for clarity
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    # Dynamic title: Calculates mean rainfall formatted to 2 decimal places
    plt.title(f"{y_col} Analysis(Avg:{df[y_col].mean():.2f})")
    # Export the final visualization as a PNG file
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_name), exist_ok=True)
    plt.savefig(output_name)
    logging.info(f"Graph saved to {output_name}")
    # Render the plot on screen
    plt.show()
    return {
        "rows_used": len(df),
        "average_y": df[y_col].mean(),
        "output_file": output_name
    }


if __name__ == "__main__":
    # Execute the function with specific file paths and output names
    info = generate_csv_graph(
        file_path=r"D:\Python Things\csv-data-viz-engine\2)Data\Rainfall in cm.csv",
        x_col="Months",
        y_col="Rainfalls",
        output_name=r"D:\Python Things\csv-data-viz-engine\Output\rainfall.png",
        graph_type="bar"
    )
    print("Graph info:", info)
