# Importing Libraries

import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode='w') as outfile:
        json.dump(enriched_posts, outfile, indent=4)

'''
This function, process_posts, processes raw post data by enriching it with metadata and standardizing tags. It first loads posts from a JSON file (raw_file_path) 
and extracts metadata from each post's text using extract_metadata(). The extracted metadata is merged with the original post data and stored in a list. 
Next, it calls get_unified_tags() to ensure consistent tagging across posts. Each post's tags are then updated to their unified versions. Finally, the 
processed posts are saved in a new JSON file (processed_file_path) with proper formatting. This function ensures the posts are enriched, well-structured, and 
tagged consistently.
'''

def extract_metadata(post):
    template = f'''
    You are given a LinkedIn Post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language, tags
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language Should be English or Hinglish (Hinglish means hindi + english)
    
    Here is the actual post on which you need to perform this task:
    {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post': post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res

'''
This function, extract_metadata(post), processes a given LinkedIn post to extract key metadata, including the number of lines, the language (English or Hinglish)
, and up to two relevant tags. It constructs a structured prompt using a template and utilizes a language model (llm) to generate a JSON response. The function 
then attempts to parse this response into a structured format using JsonOutputParser(). If the response is too large or malformed, it raises an 
OutputParserException. This ensures that metadata extraction is automated and follows a standardized format.
'''



def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    # Loop through each post and extract the tags
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])  # Add the tags to the set

    unique_tags_list = ','.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list. 
       Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
       Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
       Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
       Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    3. Output should have mapping of original tag and the unified tag. 
       For example: {{"Jobseekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation}}

    Here is the list of tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res


'''
The function get_unified_tags(posts_with_metadata) processes tags from multiple LinkedIn posts and standardizes them by merging similar tags into unified 
categories. It first collects all unique tags from the posts and formats them into a string. Then, it constructs a structured prompt instructing the language 
model (llm) to map similar tags to a common term (e.g., "Jobseekers" and "Job Hunting" merge into "Job Search"). The response is parsed into a JSON format, 
ensuring each original tag has a corresponding unified tag. If the response is too large or improperly formatted, an exception is raised. This approach ensures 
consistency and reduces redundancy in tag classification.
'''


if __name__ == "__main__":
    process_posts("C:/LinkedIn_Post_Generator/data/raw_posts.json", "C:/LinkedIn_Post_Generator/data/processed_posts.json")