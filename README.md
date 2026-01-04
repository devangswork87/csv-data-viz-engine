# CSV Data Visualization Utility 📊

A small Python utility that takes a CSV file and automatically generates a graph (line, bar, or scatter) using **pandas** and **matplotlib**.  
You give it a file, tell it which columns to use, and it spits out a PNG graph like a well-trained robot.

---

## Features

- Reads data directly from a CSV file
- Supports **line**, **bar**, and **scatter** plots
- Automatically cleans missing and non-numeric values
- Calculates and displays the average of the Y-axis data
- Saves the graph as a PNG file
- Raises meaningful errors instead of silently failing (rare, I know)

---

### Path Handling

This script supports both absolute and relative file paths.

If absolute paths are used, the script can be executed from any directory.
Relative paths depend on the current working directory and may require
using `..` to navigate folders.

## Requirements

Make sure you have Python 3.8+ installed.

Install dependencies using:

```bash
pip install pandas matplotlib
```
