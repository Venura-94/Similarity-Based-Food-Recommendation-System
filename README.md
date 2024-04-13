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

## How Cosine similarity works in this particular case
Let's consider a scenario where we have two users and their ratings for only two items:

User 1: [4, 5]
User 2: [2, 3]

In this simplified example, each user's vector represents their ratings for two items. Now, let's calculate the cosine similarity between these two vectors:

- Dot product of the two vectors:
  \( 4 \times 2 + 5 \times 3 = 8 + 15 = 23 \)

- Magnitudes of the vectors:
  \( \|User\_1\| = \sqrt{4^2 + 5^2} = \sqrt{16 + 25} = \sqrt{41} \)  
  \( \|User\_2\| = \sqrt{2^2 + 3^2} = \sqrt{4 + 9} = \sqrt{13} \)

- Cosine similarity:
  \( \text{cos}(\theta) = \frac{23}{\sqrt{41} \times \sqrt{13}} \)

Now, let's visualize these vectors:
   (4, 5)  User 1
       *
          \
           \
            \
             \
              \
               \
                \
(2, 3)  *---------*  User 2










