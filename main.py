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
        print(f"processing {file_path}")
        loader = TextLoader(file_path)
    elif file_path.endswith(".pdf"):
        print(f"processing {file_path}")
        loader = PyPDFLoader(file_path)
    else:
        raise ValueError("Unsupported file type. Please use .txt or .pdf files")
    return loader.load()

def generate_requirements():
    print("Generating requirements file")
    os.system("pip freeze > requirements.txt")

def main():
    # load_secrets()
    file_path = input("enter file path of file (.txt or .pdf): ")
    question = input("Enter your question: ")

    docs = load_documents("docs/about_me_pdf.pdf")

    #produce requirements.txt
    #probably doesnt need to be done every time
    #generate_requirements()



if __name__ == "__main__":
    main()