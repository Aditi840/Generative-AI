#Importing Libraries

from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


'''
The code initializes an instance of FewShotPosts, likely a class that provides predefined LinkedIn post examples. The function get_length_str(length) maps 
user-selected post length options ("Short," "Medium," or "Long") to corresponding text descriptions. "Short" corresponds to 1–5 lines, "Medium" to 6–10 lines, 
and "Long" to 11–15 lines. This ensures a clear interpretation of the length selection, helping to generate posts of the appropriate size.
'''

def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


'''
The generate_post function creates a LinkedIn post based on the specified length, language, and tag. It first calls get_prompt(length, language, tag), which 
likely constructs a relevant prompt for generating the post. This prompt is then passed to llm.invoke(prompt), where llm (a language model) generates a response. 
Finally, the function returns the generated content, ensuring a dynamic and context-aware post creation process.
'''


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


'''
The get_prompt function constructs a detailed prompt for generating a LinkedIn post based on user inputs. It first converts the selected length into a 
descriptive string using get_length_str(length). Then, it creates a structured prompt containing the topic (tag), length, and language, ensuring clarity for 
the language model. If the language is "Hinglish," the text should be a mix of Hindi and English but written in the English script. Additionally, the function 
retrieves example posts using few_shot.get_filtered_posts(length, language, tag). If relevant examples exist, they are appended to the prompt to guide the 
language model’s writing style, with a maximum of two samples included.
'''


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Job Search"))