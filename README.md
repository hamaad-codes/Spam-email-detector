# 📩 Spam Email Detection - Machine Learning Project

This is a machine learning-based project that detects whether an email message is spam or not.

## 🔍 Features
- Text preprocessing using TF-IDF Vectorization
- Spam classification using Logistic Regression
- Clean and interactive web interface using Streamlit
- Evaluation via confusion matrix and classification report

## 📁 Project Structure
```
.
├── app.py                  # Streamlit web app
├── outputs/
│   ├── spam_model.pkl      # Trained model
│   ├── vectorizer.pkl      # TF-IDF vectorizer
│   └── confusion_matrix.png
├── data/
│   └── spam.csv            # Raw dataset
├── notebooks/
│   ├── 01_EDA.ipynb        # Exploratory Data Analysis
│   └── 02_Modeling.ipynb   # Model training and evaluation
├── src/
│   └── utils.py            # Utility functions
├── requirements.txt
└── README.md
```

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/spam-email-detector.git
   cd spam-email-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 📊 Model Performance
- Accuracy: ~94%
- Precision (Spam): 1.00
- Recall (Spam): 0.81

## 📦 Built With
- Python
- Scikit-learn
- Pandas, NumPy
- Streamlit
- Matplotlib, Seaborn

## 📌 Author
Made with ❤️ by Hammad Zafar(https://www.linkedin.com/in/hamaad-zafar)