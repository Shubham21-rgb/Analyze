# Data Processing Project

This project processes data from an Excel file and generates a JSON result. It uses Python with Pandas and is set up with a CI/CD pipeline using GitHub Actions.

## Setup

1. Ensure you have Python 3.11+ installed.
2. Install the required Python packages:
   ```bash
   pip install pandas==2.3.0
   ```

## Usage

Run the script to process the data:
```bash
python execute.py
```

## CI/CD

The project includes a GitHub Actions workflow that:
- Runs code linting with ruff.
- Executes the script to generate a JSON file.
- Publishes the JSON result to GitHub Pages.

## License

This project is licensed under the MIT License.