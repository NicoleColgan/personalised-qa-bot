from langchain.document_loaders import TextLoader, PyPDFLoader
import os
import configparser

def load_secrets():
    config = configparser.RawConfigParser()
    config.read("secret.properties")
    for section in config.sections():
        for key, value in config.items(section):
            print(f"saving {key.upper()} as an environmental variable")
            os.environ[key.upper()] = value

def load_documents(file_path):
    print("Loading docs")
    if file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file type. Please use .txt or .pdf files")
    return loader.load()



def main():
    load_secrets()
    file_path = input("enter file path of file (.txt or .pdf): ")
    question = input("Enter your question: ")

    docs = load_documents("docs/about_me.txt")



if __name__ == "__main__":
    main()