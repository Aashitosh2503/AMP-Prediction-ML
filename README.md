# 🧬 Antimicrobial Peptide Prediction using Machine Learning

## About the Project

This project is a simple machine learning approach to predict whether a given peptide sequence is antimicrobial (AMP) or not.

Antimicrobial peptides are important because they can help fight infections, especially with the growing issue of antibiotic resistance. The idea here was to see if we can use basic sequence information to make meaningful predictions.

---

## What I Did

* Collected peptide sequences and labeled them as AMP or non-AMP
* Extracted features from sequences:

  * Amino acid composition
  * Sequence length
  * Positive charge (K, R residues)
* Trained a **Random Forest model**
* Evaluated performance using classification metrics and confusion matrix
* Analyzed feature importance to understand what influences predictions
* Built a **Streamlit web app** for easy interaction

---

## Key Observations

* Positively charged residues (especially **Lysine (K)** and **Arginine (R)**) played a major role
* This aligns with biological understanding of AMPs
* The model achieved around **80–85% accuracy**, which is reasonable for a simple feature-based approach

---

## Web App

I also created a small web application using Streamlit where you can:

* Enter a peptide sequence
* Get prediction instantly (AMP / Not AMP)

---

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## Future Improvements

* Use larger datasets (like APD3 or CAMP)
* Try deep learning models (CNN / LSTM)
* Add more biochemical features
* Improve model generalization

---

## Final Note

This project helped me understand how machine learning can be applied to biological problems, especially in peptide research. It’s a small step, but a meaningful one towards combining ML with bioinformatics.
