import os
import re
from typing import List


def main():
    tokenized_problem = tokenize_input("Problem name: ")
    generate_files(tokenized_problem)


def tokenize_input(prompt: str) -> List[str]:
    """
    Prompts the user for a string, which is tokenized and has punctuation removed.
    :param prompt:
    :return: tokenized input
    """

    # Prompt the user for the problem name
    problem = input(prompt).lower().strip()

    token_regex = "([^\s\-_]+)"  # Matches the words
    replace_regex = "[^\w]+"  # Matches punctuation

    # Tokenize the string into words
    matches = re.findall(token_regex, problem)

    # Remove all punctuation from the word tokens
    tokens = [re.sub(replace_regex, "", word) for word in matches]

    # Ensure the input is valid
    if not tokens:
        print("Problem name is empty")
        exit(100)
    for token in tokens:
        if token == "":
            print("Invalid problem name")
            exit(101)

    return tokens


def get_leetcode_url(tokenized_problem: List[str]) -> str:
    """
    Returns the url of an assumed to exist problem
    :param tokenized_problem:
    :return: The url of the leetcode problem
    """

    protocol = "https://"
    domain = "leetcode.com"
    path = f"/problems/{'-'.join(tokenized_problem)}/"

    return f"{protocol}{domain}{path}"


def generate_readme(title: str, url: str, local_path: str) -> None:
    """
    Generates the readme from a template
    :param title:
    :param url:
    :param local_path:
    :return:
    """
    # Open the template
    with open("resources/readme_template.txt", "r") as infile:
        content = infile.read()

    # Change the placeholders in the template
    modified = content.replace("title", title).replace("url", url)

    # Generate the new readme file
    with open(f"{local_path}/README.md", "w") as outfile:
        outfile.write(modified)


def generate_class(
    title: str, class_name: str, local_path: str, file_name: str
) -> None:
    """
    Generates the class from a template
    :param title:
    :param class_name:
    :param local_path:
    :param file_name:
    :return:
    """
    # Open the template
    with open("resources/class_template.txt", "r") as infile:
        content = infile.read()

    # Change the placeholders in the template
    modified = content.replace("title", title).replace("class_name", class_name)

    # Generate the new class file
    with open(f"{local_path}/{file_name}.py", "w") as outfile:
        outfile.write(modified)


def generate_test(
    class_name: str,
    local_path: str,
    file_name: str,
) -> None:
    """
    Generates a test file from a template.
    :param class_name:
    :param local_path:
    :param file_name:
    :return:
    """

    # Open the template
    with open("resources/test_template.txt", "r") as infile:
        content = infile.read()

    # Change the placeholders in the template
    modified = content.replace("class_name", class_name).replace("file_name", file_name)

    # Generate the new test file
    with open(f"{local_path}/test_{file_name}.py", "w") as outfile:
        outfile.write(modified)


def generate_directory(local_path: str) -> None:
    """
    Creates the directory to contain problem-related files
    :param local_path:
    :return:
    """

    try:
        # Make the directory
        os.makedirs(local_path, exist_ok=False)
    except OSError:
        print(f"Directory {local_path} already exists")
        exit(110)


def generate_files(tokenized_problem: List[str]) -> None:
    class_name = "".join(word.title() for word in tokenized_problem)
    file_name = "_".join(tokenized_problem)
    local_path = f"src/problems/{file_name}"
    title = " ".join(tokenized_problem).title()
    url = get_leetcode_url(tokenized_problem)

    generate_directory(local_path)
    generate_class(title, class_name, local_path, file_name)
    generate_test(class_name, local_path, file_name)
    generate_readme(title, url, local_path)


if __name__ == "__main__":
    main()
