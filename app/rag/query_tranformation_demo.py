from .query_transformer import get_query_transformer

def main():
    qt = get_query_transformer("groq")

    query = "Explain LCEL in LangChain"

    print("\n--- Original Query ---")
    print(query)

    print("\n--- Rewritten Query ---")
    print(qt.rewrite_query(query))

    print("\n--- Multi Query Expansion ---")
    for q in qt.multi_query(query):
        print("-", q)

    print("\n--- HyDE Output ---")
    print(qt.hyde(query))


if __name__ == "__main__":
    main()
