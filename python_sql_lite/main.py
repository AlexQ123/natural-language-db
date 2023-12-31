import argparse
import openai
import os

from query import select_from_table
from schema import get_schema
from db import create_connection

DATABASE = "./pythonsqlite.db"

def main(conn, question):
    # Set a system environment variable, and name it '452_API_KEY'
    openai.api_key = os.environ.get('452_API_KEY');
    print(f"Question: {question}")

    prompt = f"""
    
    Given the following SQL Schema that models a video-sharing platform similar to YouTube:{get_schema()}
    Write a SQLite query to answer this question: {question}
    
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=200
    )


    q = response["choices"][0]["text"]

    print(f"AI-generated SQL query: \n{q}")
    print("Answer: \n")

    try:
        select_from_table(conn, q)
    except Exception as e:
        print("The AI-generated SQL produced an error: ", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="natural language query")
    args = parser.parse_args()
    conn = create_connection(DATABASE)

    main(conn, question=args.query)

