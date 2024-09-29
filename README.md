# 🚀 HackSynthesis 🌍

# Welcome to Pragati Aid by Team Omicode

### **"Empowering Communities through Intelligent Rainfall Forecasting for Natural Disaster Resilience."**

---

🌟 This project aims to boost **disaster preparedness** by predicting natural calamities using **Machine Learning** 🧠, time-series models like **ARIMA** 📈, and a **blockchain-based relief fund collection gateway** 💸 powered by **smart contracts** on Ethereum 🔗.

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

## Flowchart

![Screenshot 2024-09-29 115457](https://github.com/user-attachments/assets/79ba4ce1-bc29-4e2e-9892-e32d3b660afd)


## 📸 Snapshots

![Natural Calamity Predictor Interface](https://github.com/user-attachments/assets/4a776950-5a4f-4f2d-b36c-b286736d619c)

👆 A glimpse of the app interface for predicting the probability of natural disasters using ML and ARIMA-based models.

https://github.com/user-attachments/assets/6a03594f-8c07-4d2d-8a0a-fb1ad6472927


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

### Unique Selling Propositions (USPs)
1. **Comprehensive Disaster Preparedness**: Integrates advanced machine learning and time-series models for accurate natural calamity predictions.
2. **Localized Forecasting**: Provides detailed district-level predictions for natural disasters in West Bengal, ensuring targeted insights.
3. **Blockchain-Based Relief Fund**: Utilizes smart contracts on Ethereum for secure, transparent, and traceable donation processes.
4. **GeoTIFF Visualization**: Generates dynamic precipitation timeline videos using GeoTIFF data, enhancing user understanding of weather trends.


---


### Feasibility
1. **Data-Driven Decision Making**: Leverages extensive historical weather data to enhance prediction accuracy and reliability.
2. **Scalable Framework**: The system can be adapted to different regions beyond India, allowing for wider application in disaster management.
3. **Technological Reliability**: Built using proven technologies such as Python, Ethereum, and TensorFlow, ensuring a solid foundation for the project.
4. **Community Engagement**: Encourages active participation through a blockchain-based donation system, fostering trust and local involvement.

---

### Novelty
1. **Interdisciplinary Integration**: Combines machine learning, geospatial analysis, and blockchain technology for a comprehensive disaster management solution.
2. **Real-Time Disaster Insights**: Offers real-time analytics on disaster probabilities and blockchain transactions, enhancing situational awareness.
3. **GeoTIFF Data Utilization**: Innovatively employs GeoTIFF data to create detailed precipitation timeline visualizations for informed decision-making.
4. **Localized Impact Focus**: Prioritizes district-specific data, highlighting the importance of localized forecasting in effective disaster preparedness.

### Other Aspects
1. **Community Empowerment**: Equips communities with tools and information necessary for proactive disaster preparedness and response.
2. **Holistic Disaster Ecosystem**: Encompasses the entire disaster management process, from prediction to relief fund allocation, fostering resilience.
3. **Open-Source Development**: Promotes collaborative contributions from developers and researchers to innovate and improve disaster management solutions.
4. **Awareness and Education**: Aims to raise public awareness about disaster preparedness and community involvement through a user-friendly platform.

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
