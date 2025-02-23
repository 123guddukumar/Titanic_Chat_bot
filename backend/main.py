from fastapi import FastAPI, Query
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = FastAPI()

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

def generate_plot():
    """ Generate histogram of passenger ages and return base64 image """
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'].dropna(), bins=20, kde=True, color="blue")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.title("Passenger Age Distribution")
    
    # Save plot as base64 string
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

@app.get("/query/")
def process_query(question: str = Query(..., description="Ask about Titanic dataset")):
    """ Process user queries and return text or visualization responses """
    question = question.lower()

    if "percentage of passengers were male" in question:
        male_percentage = (df['Sex'].value_counts(normalize=True) * 100)['male']
        return {"answer": f"{male_percentage:.2f}% of passengers were male."}

    elif "histogram of passenger ages" in question:
        image_base64 = generate_plot()
        return {"image": image_base64}

    elif "average ticket fare" in question:
        avg_fare = df["Fare"].mean()
        return {"answer": f"The average ticket fare was ${avg_fare:.2f}."}

    elif "passengers embarked from each port" in question:
        embark_counts = df["Embarked"].value_counts().to_dict()
        return {"answer": f"Passengers embarked from: {embark_counts}"}

    return {"answer": "I don't understand that question yet!"}
