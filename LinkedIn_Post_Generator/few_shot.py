#Importing Libraries


import json
import pandas as pd


class FewShotPosts:
    def __init__(self, file_path="C:/LinkedIn_Post_Generator/data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"

        elif 5 <= line_count <= 10:
            return "Medium"

        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient="records")

'''
The FewShotPosts class consists of several functions that help manage and filter LinkedIn posts for few-shot learning. The __init__ method initializes the class 
by loading a dataset from a specified file path and processes the data. The load_posts function reads the JSON file, normalizes it into a Pandas DataFrame, 
categorizes post lengths based on line count, and extracts unique tags from all posts. The categorize_length function assigns each post a length 
category: "Short" (less than 5 lines), "Medium" (5 to 10 lines), or "Long" (more than 10 lines). The get_tags function retrieves and returns all unique tags 
present in the dataset. Finally, the get_filtered_posts function filters the posts based on user-specified criteria—length, language, and tag—returning 
relevant posts as a dictionary. These functions collectively ensure that relevant example posts are available to guide the model in generating 
new LinkedIn content.
'''


if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Short", "English", "Job Search")
    print(posts)