

---

## NumPy Memory Optimizer

A small, nerdy command-line tool to analyze how much memory your NumPy arrays are actually consuming — and how much you can save by using more efficient data types.

## Features

- Calculates memory usage of NumPy arrays with different int dtypes
- Automatically selects the smallest unsigned integer type (uint8, uint16, etc.) that fits your data
- Compares memory usage against NumPy's default int64
- Displays memory savings in bytes and percentage
- Logs unexpected errors to error_log.json
- Clean, interactive CLI with support for repeated analysis

## Limitations

Currently, this tool only supports integer dtypes. Support for other data types (e.g., floats, booleans, complex numbers) will be added in future versions.

## Contributions Welcome

Want to help expand the tool? Feel free to fork, improve, and submit pull requests! Whether it's adding support for more dtypes, improving error handling, or enhancing the UI — all contributions are appreciated.

🛠️ Requirements

- Python 3.6+
- NumPy

Install dependencies with:

`bash
pip install numpy
`

## Usage

Run the script:

`bash
python numpy_memory_optimizer.py
`

Then follow the prompts:

- Enter the number of elements you want to analyze
- View memory usage and savings
- Choose to run another test or quit


##  Error Logging

Any unexpected exceptions are timestamped and saved to error_log.json for debugging purposes.

## Timezone

All timestamps are recorded in Nigerian local time (UTC+1).

---

