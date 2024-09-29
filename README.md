
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
  
## Flow of control:
  ![Screenshot 2024-09-29 115457](https://github.com/user-attachments/assets/e502715c-2cb1-471b-ba73-9bbb384bca52)

## Snapshots
![f65251eae4f4bbe974811ac962cc0ec158dbd92fc40dd3c8cf24e769](https://github.com/user-attachments/assets/4a776950-5a4f-4f2d-b36c-b286736d619c)


https://github.com/user-attachments/assets/6a03594f-8c07-4d2d-8a0a-fb1ad6472927


![a377e179219cfa05f72980d237d91bdef822abfc2dcacff318ea9d35](https://github.com/user-attachments/assets/0a66c26d-6060-4be5-a97b-65cd3ac2464e)


![3de08fc47caea6d37205b7f171222d6447b965f74e3e8b091dae6eca](https://github.com/user-attachments/assets/822c525a-a86c-44a4-866a-201019000d53)

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
- **Blockchain**: Truffle, Ganache, Ethereum

## Contributors

- [Ananyo Dasgupta](https://github.com/CodenWizFreak)
- [Soumyadip Roy](https://github.com/SoumyadipRoy16)
- [Anidipta Pal](https://github.com/Anidipta)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


