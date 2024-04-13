## Similarity-Based-Food-Recommendation-System 
## Kaggle Data Set - https://www.kaggle.com/datasets/schemersays/food-recommendation-system/code

### Focus of the Project - Similarity between users and recommend items based on food interacted by other similar users

## Project Structure

- Task 1: What is collaborative filtering and how to collect data to build a recommendation system and load the required libraries and the dataset into the jupyter notebook session  

- Task 2: Perform exploratory data analysis on the dataset to observe the user interactions with the item, for example which item is the most interacted item and which user has interacted with most items etc  

- Task 3: Create user item matrix to start building the collaborative recommendation system  

- Task 4: Find which users are most similar to the other users from user time matrix(Cosine similarity - Nearest neighbors are then determined based on these similarity scores), this will help to recommend items to the users which the other similar users have interacted with  

- Task 5: Build a similarity based recommendation system based on collaborative filtering  

# Pipeline Architecture for Food Recommendations

![image](https://github.com/Venura-94/Similarity-Based-Food-Recommendation-System/assets/137409412/5c261349-225b-4637-9e4b-e33fe43d63d2)

## How Cosine similarity works in this particular case as an example for understanding the concept


![image](https://github.com/Venura-94/Similarity-Based-Food-Recommendation-System/assets/137409412/4a70bc30-cec5-4166-b182-459cfa98186e)


### Now, let's visualize these vectors:

       (4, 5)  User 1
           *
              \
               \
                \
                 \
                  \
                   \
                    \
(2, 3)  *-----------*  User 2


 - But in my case its whole lot of dimensions in the interaction matrix and cannot draw like this. but the same concept.







