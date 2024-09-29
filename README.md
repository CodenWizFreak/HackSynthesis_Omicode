# 🚀 HackSynthesis - Team Omicode 🌍

Welcome to **HackSynthesis Omicode**! 🌟 This project aims to boost **disaster preparedness** by predicting natural calamities using **Machine Learning** 🧠, time-series models like **ARIMA** 📈, and a **blockchain-based relief fund collection gateway** 💸 powered by **smart contracts** on Ethereum 🔗.

---

## 🎯 Table of Contents

- [✨ Features](#features)
- [📸 Snapshots](#snapshots)
- [🔧 Installation](#installation)
- [📖 Usage](#usage)
- [⚙️ Technologies Used](#technologies-used)
- [👥 Contributors](#contributors)
- [📜 License](#license)

---

## ✨ Features

1. **Natural Calamity Probability Predictor 🌩️**:
   - Predicts the likelihood of natural disasters, such as **cloudbursts**, **floods**, and **rainfall** 🌧️ for specific dates using advanced **ML algorithms** like **Gradient Boosting** 🌲, **ARIMA time series analysis** 📉, and **Haversine Formula** 📐.

2. **State-Level Precipitation Timeline Videos 🎥**:
   - Generates **GeoTIFF**-based precipitation timeline videos across **India** 🇮🇳, its individual states 🗺️, and even **districts in West Bengal** 📍. The analysis can provide users with district-wise precipitation patterns, offering granular disaster insights.

3. **Blockchain-Based Relief Fund 💵**:
   - Utilizes **Solidity smart contracts** to enable secure and transparent **Web3 token-based donations**. Each transaction is stored on the **Ethereum blockchain** ensuring complete **trust** and **transparency**.

4. **District-Wise Disaster Forecasting for West Bengal 📊**:
   - Users can view **district-level** forecasting for **West Bengal** based on historical weather data 🌦️. This fine-grained prediction system analyzes past trends using **ARIMA** and **ML** models for highly localized disaster preparedness.

---

## 📸 Snapshots

![Natural Calamity Predictor Interface](https://github.com/user-attachments/assets/4a776950-5a4f-4f2d-b36c-b286736d619c)

👆 A glimpse of the app interface for predicting the probability of natural disasters using ML and ARIMA-based models.

![Precipitation Timeline Across States](https://github.com/user-attachments/assets/6a03594f-8c07-4d2d-8a0a-fb1ad6472927)

🎥 Visualize precipitation timelines across **India** and its **states** with **GeoTIFF** data.

![Blockchain Relief Fund](https://github.com/user-attachments/assets/0a66c26d-6060-4be5-a97b-65cd3ac2464e)

💸 Leverage **blockchain-based relief fund** collection, ensuring transparent, immutable donations.

![District Analysis in West Bengal](https://github.com/user-attachments/assets/822c525a-a86c-44a4-866a-201019000d53)

📊 Analyze **district-level precipitation** in **West Bengal** for a more detailed understanding of weather trends.

---

## 🔧 Installation

To set up **HackSynthesis Omicode** on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CodenWizFreak/HackSynthesis_Omicode.git
   cd HackSynthesis_Omicode
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the blockchain environment** 🏗️:
   - Ensure [Node.js](https://nodejs.org/) is installed.
   - Install **Truffle** and **Ganache**:
     ```bash
     npm install -g truffle
     npm install -g ganache-cli
     ```

5. **Compile and deploy smart contracts** 📝:
   ```bash
   truffle compile
   truffle migrate --network development
   ```

---

## 📖 Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Explore the Features**:
   - **Predict natural disasters**: Enter a specific date to receive predictions for cloudbursts, floods, etc.
   - **Generate Precipitation Videos**: Select a region (India, state, or district) and generate a precipitation video based on historical **GeoTIFF** data.
   - **District-Level Analysis**: Receive a detailed **district-wise** prediction for **West Bengal** based on **ARIMA** and **ML** models.
   - **Blockchain Donations**: Use the app to make Web3 token transactions toward the relief fund.

3. **Blockchain Transactions** 💰:
   - Make secure **Web3 token-based donations** for disaster relief using **Solidity-based smart contracts**.
   - Watch **live gas fees** ⛽ and **blockchain confirmations** in real-time.

---

## ⚙️ Technologies Used

- **Frontend**: Streamlit 💻
- **Backend**: Python (Flask), Streamlit 🚀
- **Machine Learning**: TensorFlow, Keras 🧠, Scikit-learn, XGBoost, Haversine Formula 📐, ARIMA (AutoRegressive Integrated Moving Average) 📉
- **Data Processing**: Pandas, NumPy 🧮, GeoTIFF, Rasterio 🌍
- **Blockchain**: Truffle, Ganache, Ethereum 🔗, MetaMask 🦊, Web3.py 🌐
- **Smart Contracts**: ERC-20 Token Standard 💎
- **Data Visualization**: Matplotlib, Seaborn, Plotly 📊
- **Geospatial Data**: GeoPandas, Folium 🗺️
- **Video Processing**: OpenCV 🎥, ImageIO 📅

---

## 👥 Contributors

- [Ananyo Dasgupta](https://github.com/CodenWizFreak) 🎓
- [Soumyadip Roy](https://github.com/SoumyadipRoy16) 🚀
- [Anidipta Pal](https://github.com/Anidipta) 🌟

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details. 📄

---

Let’s reshape the future of disaster management with advanced **machine learning**, **ARIMA models**, **geospatial analysis**, and **blockchain** technologies! 🚀
