# European Airport Traffic Analysis ✈️
A Python-based data analysis tool that processes airport traffic surveys to generate statistical reports and visualize flight patterns
## 📋 Project Overview
This application processes large datasets (CSV) of flight information from major European airports (e.g., Heathrow, Charles de Gaulle, Munich). It performs data cleaning, statistical analysis, and generates visual histograms to help users understand flight delays, terminal usage, and weather impacts.

**Key Features:**
* **Data Ingestion:** Parses raw CSV flight data with robust error handling for missing or incorrect formats.
* **Input Validation:** Validates user inputs for airport codes (IATA) and date ranges.
* **Statistical Reporting:** Calculates metrics such as:
    * Total flight volume per terminal.
    * Airline-specific delay percentages.
    * Weather correlation (flights departing in rain/low temps).
* **Data Visualization:** Renders dynamic histograms using `graphics.py` to show flight frequency by hour.
* **Persistence:** Exports detailed analysis results to a `results.txt` file for reporting.


## 📊 Example Usage
**User Input:**
> Enter Airport Code: **LHR**(or CDG)
> Enter Year: **2025**(**2021** if CDG used)

**System Output:**
> "Analyzing London Heathrow 2025..."
> "Total Flights: 490"
> "British Airways Delay Rate: 15.79%"
> *[Histogram Window Opens]*
