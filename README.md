# Email Automation – Stock Report

A Python script that retrieves an IBM stock quote from the Alpha Vantage API, saves the response as JSON, and emails a short stock report using Gmail SMTP.

## Features

- Retrieves a stock quote through Alpha Vantage
- Saves the API response to `stocks.json`
- Extracts the symbol, opening price, daily high and low, and percentage change
- Sends a formatted email through Gmail SMTP

## Requirements

- Python 3
- `requests`

Install the dependency:

```bash
python -m pip install requests
```

## Configuration and security

**Do not run or publish this repository with the credentials currently present in its scripts.** The repository contains exposed email credentials and an API key. Revoke or rotate them before use.

For a safe future version, load credentials from environment variables or a local `.env` file that is excluded from Git. Never commit real passwords, app passwords, or API keys.

## Run

The repository contains both `main.py` and `Main`, which implement similar email-report workflows. Review the credential configuration in the chosen script before running it:

```bash
python main.py
```

## Output

The script writes the API response to `stocks.json` and attempts to send an email containing the stock summary.

## Notes

- The current request is configured for the IBM symbol.
- API availability, rate limits, and SMTP account settings can affect execution.
- This project demonstrates API integration, JSON handling, and email automation; it is not financial advice.
