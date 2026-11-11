# 🛡️ FraudShield AI – Financial Transaction Fraud Detection

A Python-based machine learning project that analyzes financial transactions and predicts potential fraudulent activity using classification algorithms.

## 📌 About the Project

FraudShield AI is an educational fraud detection system designed to identify suspicious financial transactions using machine learning.

The project generates a synthetic financial transaction dataset, preprocesses the data, trains multiple machine learning models, evaluates their performance, and selects the best-performing model for fraud prediction.

It also provides a desktop GUI where users can enter transaction details and analyze potential fraud risks.

## ✨ Features

- Synthetic financial transaction dataset generation
- Automated data preprocessing and cleaning
- Logistic Regression classification
- Random Forest classification
- Automatic model selection using F1 Score
- Fraud probability estimation
- Interactive transaction analysis
- Transaction history tracking
- Model performance comparison
- Dark-themed desktop dashboard

## 🧠 Machine Learning Algorithms

**1. Logistic Regression**

A supervised classification algorithm used to estimate the probability of a transaction belonging to a particular class.

**2. Random Forest Classifier**

An ensemble learning algorithm that combines multiple decision trees to improve classification performance.

The application compares both models using:

- Accuracy
- Precision
- Recall
- F1 Score

The model with the higher F1 Score is selected automatically.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical operations and data generation |
| Pandas | Dataset creation and preprocessing |
| Scikit-learn | Machine learning and model evaluation |
| Tkinter / CustomTkinter | Desktop graphical interface |
| CSV | Dataset storage |

## 📂 Project Structure

```text
FraudShield-AI/
│
├── app.py              # Desktop GUI
├── main.py             # Model training and selection
├── generatedata.py     # Synthetic dataset generation
├── processing.py       # Data preprocessing
├── transactions.csv    # Generated dataset
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/FraudShield-AI.git
```

**2. Navigate to the project directory**

```bash
cd FraudShield-AI
```

**3. Install dependencies**

```bash
pip install numpy pandas scikit-learn
```

Tkinter is generally included with standard Python installations.

**4. Run the application**

```bash
python app.py
```

Make sure the transaction dataset has been generated before launching the application, or use the integrated dataset-generation workflow if configured.

## 🔄 Project Workflow

```text
Synthetic Data Generation
          |
          v
    Data Preprocessing
          |
          v
   Feature Selection
          |
          v
     Train-Test Split
          |
          v
    Model Training
          |
          v
   Model Evaluation
          |
          v
    Model Selection
          |
          v
      GUI Dashboard
          |
          v
   Fraud Prediction
```

## 📊 Transaction Features

The synthetic dataset contains the following transaction attributes:

| Feature | Description |
|---|---|
| amount | Transaction amount |
| hour | Transaction time |
| account_age | Account age in days |
| transactions | Transaction count |
| distance | Transaction distance |
| international | International transaction indicator |
| failed_pin | Failed PIN attempts |
| device_changed | Device change indicator |
| is_fraud | Target classification label |

## 🔍 Fraud Prediction

Users can enter transaction details through the Fraud Analysis section.

The selected model provides:

- Predicted transaction status
- Estimated fraud probability
- Basic verification recommendation

**Prediction classes:**

- `0` – Likely Legitimate
- `1` – Potential Fraud

## ⚠️ Disclaimer

This project uses synthetically generated financial transaction data and rule-based labels for educational purposes.

It is not a production-ready banking fraud detection system and should not be used to make real financial security decisions.

## 🚀 Future Improvements

- Integration of real-world financial transaction datasets
- Advanced anomaly detection techniques
- Improved fraud probability calibration
- Persistent transaction history using a database
- Model saving and loading instead of retraining on every launch
- Real-time transaction monitoring
- Enhanced dashboard visualizations

## 👨💻 Author

**Jasman Singh**

Interested in Python, Machine Learning, Cybersecurity, and Software Development.

---

⭐ If you find this project interesting, consider giving it a star!
