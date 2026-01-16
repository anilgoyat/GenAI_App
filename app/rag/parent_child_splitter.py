from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_parent_child_chunks(documents):
    # Parent splitter (large context)
    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )

    # Child splitter (fine-grained retrieval)
    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100
    )

    parents = parent_splitter.split_documents(documents)

    all_children = []
    parent_lookup = {}

    for i, parent in enumerate(parents):
        children = child_splitter.split_documents([parent])

        for child in children:
            child.metadata["parent_id"] = i

        parent_lookup[i] = parent
        all_children.extend(children)

    return all_children, parent_lookup
