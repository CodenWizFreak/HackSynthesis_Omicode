
# HackSynthesis- Team Omicode

Welcome to **HackSynthesis Omicode**! This project aims to enhance disaster preparedness by providing insights into potential natural calamities through machine learning, along with a relief fund collection gateway on the blockchain.

## Table of Contents

- [Features](#features)
- [Snapshots](#snapshots)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [License](#license)

## Features

1. **Natural Calamity Probability Predictor**:
   - A Streamlit app where users can enter a date to receive the probability of natural calamities such as cloudbursts, floods, or rainfall.
  
2. **Precipitation Timeline Video**:
   - The app creates a timeline video of the precipitation gradient across India or West Bengal based on user-defined start and end dates.
  
3. **Blockchain-Based Relief Fund**:
   - A Solidity smart contract that allows users to contribute to a relief fund using Web3 tokens, ensuring transparent and secure transactions.
  
## Snapshots



## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/CodenWizFreak/HackSynthesis_Omicode.git
   cd HackSynthesis_Omicode
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the blockchain environment:
   - Ensure you have [Node.js](https://nodejs.org/) installed.
   - Install Truffle and Ganache:
     ```bash
     npm install -g truffle
     npm install -g ganache-cli
     ```

5. Compile and migrate the smart contracts:
   ```bash
   truffle compile
   truffle migrate --network development
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Interact with the App**:
   - Open your web browser and go to `http://localhost:8501` to access the app.
   - Enter the required dates and explore the features.

3. **Blockchain Transactions**:
   - Use the provided functionality in the app to make Bitcoin token transactions for the relief fund.

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Streamlit
- **Machine Learning**: Tensorflow, Keras
- **Blockchain**: Solidity, Truffle, Ganache, Ethereum

## Contributors

- [Ananyo Dasgupta](https://github.com/CodenWizFreak)
- [Soumyadip Roy](https://github.com/SoumyadipRoy16)
- [Anidipta Pal](https://github.com/Anidipta)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize any part of this README to better fit your project specifics!
