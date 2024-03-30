# CAPM Analysis Project

## Overview

The CAPM Analysis Project is designed to offer an in-depth tool for financial analysis, specifically through the lens of the Capital Asset Pricing Model (CAPM). This Python-based tool enables users to assess the risk and expected returns of securities compared to the overall market, providing valuable insights for investors and analysts alike.

## Features

- **Data Acquisition**: Automatically download historical stock and benchmark index data using Yahoo Finance.
- **Return Calculations**: Compute daily or monthly returns for selected securities and benchmarks.
- **Regression Analysis**: Perform regression analysis to determine the beta coefficient of a stock, indicating its volatility relative to the market.
- **Data Visualization**: Generate and visualize data plots showing the relationship between the stock returns and the benchmark returns.
- **Excel Reporting**: Export detailed analysis results, including statistical measures and plots, to an Excel file for further review or presentation.

## System Requirements

- Python 3.6 or higher
- Internet connection for data download
- Compatible with Windows, macOS, and Linux

## Installation Instructions

1. **Clone the Repository**
   Begin by cloning the project repository to your local machine using Git:

   ```bash
   git clone https://github.com/your-username/CAPM-Analysis-Project.git
   cd CAPM-Analysis-Project
   ```

2. **Set up a Virtual Environment** (Optional but recommended)
   Create and activate a virtual environment to manage the dependencies:

   - For Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - For macOS and Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   With your virtual environment activated, install the project dependencies:

   ```bash
   pip install pandas numpy openpyxl statsmodels yfinance plotly
   ```

## Usage

1. **Basic Usage Example**
   To use the CAPM Analysis tool, you can start by creating an instance of the `CAPMAnalysis` class with your desired parameters:

   ```python
   from CAPMAnalysis import CAPMAnalysis

   # Initialize the CAPMAnalysis class
   analysis = CAPMAnalysis(ticker="AAPL", benchmark="^GSPC", risk_free="^TYX", daily_or_monthly="D")

   # Download data and perform analysis
   analysis.download_data()
   analysis.calculate_returns()
   analysis.perform_regression()
   analysis.find_beta()
   analysis.plot_regression()
   analysis.save_to_excel()
   ```

2. **Saving and Viewing Results**
   The analysis results, including plots, are saved to an Excel file in the specified directory. Open this file with any compatible spreadsheet software to view your analysis.

## Contributing

We welcome contributions to the CAPM Analysis Project! Whether it's fixing bugs, adding new features, or improving documentation, your help is appreciated. Please check out our [Contributing Guide](CONTRIBUTING.md) for more details on submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
