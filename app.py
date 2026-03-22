import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Amino acids
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Feature function
def extract_features(sequence):
    features = []
    
    for aa in amino_acids:
        features.append(sequence.count(aa))
    
    features.append(len(sequence))
    features.append(sequence.count("K") + sequence.count("R"))
    
    return features

# Dataset (same as your project)
amp_sequences = [
    "GLFDIVKKVVGAFGSL","KLLKLLKKLLKLLK","GIGKFLHSAKKFGKAFVGEIMNS"
]
non_amp_sequences = [
    "AGTCKLIVGLS","LLAVAGVAG","GASGDLGAS"
]

sequences = amp_sequences + non_amp_sequences
labels = [1]*len(amp_sequences) + [0]*len(non_amp_sequences)

data = pd.DataFrame({"sequence": sequences, "label": labels})

columns = list(amino_acids) + ["length", "positive_charge"]

X = data['sequence'].apply(extract_features)
X = pd.DataFrame(X.tolist(), columns=columns)
y = data['label']

model = RandomForestClassifier()
model.fit(X, y)

# UI
st.title("Antimicrobial Peptide Predictor")

sequence = st.text_input("Enter peptide sequence:")

if st.button("Predict"):
    features = extract_features(sequence)
    features = pd.DataFrame([features], columns=columns)
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.success("AMP ✅")
    else:
        st.error("Not AMP ❌")
