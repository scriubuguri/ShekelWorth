#ShekelWorth

This is a full stack project that allows users to quickly and easily convert between different currencies. The app utilizes the [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch up-to-date exchange rates, ensuring accurate and reliable conversions.

## Features

- *Real-Time Exchange Rates*: The app fetches the latest exchange rates from ExchangeRate-API to provide users with current and accurate conversion rates.
- *User-Friendly Interface*: A clean and intuitive interface makes it easy for users to input the amount, select currencies, and view the converted result.
- *Wide Range of Currencies*: Supports a variety of currencies, enabling users to convert between major global currencies effortlessly.

## Installation

1. Clone this repository

Open a terminal and change the current directory to the location where you want to clone the repository.
Type the following command and press enter:

```bash
git clone https://github.com/scriubuguri/ShekelWorth.git
```

2. Create a virtual environment with the following command:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Sign up to ExchangeRate-API [here](https://www.exchangerate-api.com/sign-in) and get your API key.

6. Open the `shekelworthapp/views.py` file and add your API key on the *API_KEY* variable.


## Usage

Before run the app, open the `shekelworth` folder (where you have the `manage.py` file) and apply the migrations:

```bash
python3 manage.py migrate
```

Run the app with the following command:

```bash
python3 manage.py runserver
```

Open your browser and navigate to *http://localhost:8000/* to view the app.

Choose the currencies from the dropdown menu and enter the amount to convert.

Press the `Submit` button to view the converted result.


## Author

- **scriubuguri**

