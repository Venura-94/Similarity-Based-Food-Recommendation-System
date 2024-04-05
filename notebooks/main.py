from fastapi import FastAPI
from typing import List
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Define FastAPI application
app = FastAPI()

# Load data
try:
    interactions_matrix = pd.read_csv('interactions_matrix.csv')
except FileNotFoundError:
    print("Error: 'interactions_matrix.csv' file not found. Make sure the file exists in the correct location.")
    interactions_matrix = None
except Exception as e:
    print("An error occurred while loading the data:", e)
    interactions_matrix = None

# Debugging step 1: Check if data loading is successful
if interactions_matrix is not None:
    print("Data loaded successfully. Shape:", interactions_matrix.shape)
else:
    print("Data loading failed.")

# Similarity-based recommendation function
def similar_user(User_ID, interactions_matrix):
    if interactions_matrix is None:
        return None, None  # Return None if data loading failed
    similarity = []
    for user in range(1, interactions_matrix.shape[0] + 1):
        sim = cosine_similarity([interactions_matrix.loc[User_ID]], [interactions_matrix.loc[user]])
        similarity.append((user, sim))
    similarity.sort(key=lambda x: x[1], reverse=True)
    most_similar_user = [tup[0] for tup in similarity]
    similarity_score = [tup[1] for tup in similarity]
    most_similar_user.remove(User_ID)
    similarity_score.remove(similarity_score[0])
    return most_similar_user, similarity_score

# Debugging step 2: Verify functionality of the similar_user function
most_similar_user, similarity_score = similar_user(1, interactions_matrix)
print("Most similar user:", most_similar_user)
print("Similarity score:", similarity_score)

def recommendations(User_ID, num_of_foods, user_item_interactions):
    if interactions_matrix is None:
        return None  # Return None if data loading failed
    most_similar_user = similar_user(User_ID, user_item_interactions)[0]
    food_ids = set(list(interactions_matrix.columns[interactions_matrix.loc[User_ID] > 0]))
    recommendations = []
    already_interacted = food_ids.copy()
    for sim_user in most_similar_user:
        if len(recommendations) < num_of_foods:
            similar_user_food_ids = set(list(interactions_matrix.columns[interactions_matrix.loc[sim_user] > 0]))
            recommendations.extend(list(similar_user_food_ids.difference(already_interacted)))
            already_interacted = already_interacted.union(similar_user_food_ids)
        else:
            break
    return recommendations[:num_of_foods]

# Define FastAPI endpoints
@app.get("/recommend/{user_id}/{num_of_foods}")
async def get_recommendations(user_id: int, num_of_foods: int):
    rec = recommendations(user_id, num_of_foods, interactions_matrix)
    if rec is None:
        return {"error": "Data loading failed. Please check the logs for details."}
    else:
        return {"recommendations": rec}


