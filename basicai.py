
import PyPDF2
import nltk # natural language tool kit
nltk.download('punkt')

from nltk.tokenize import word_tokenize

files = [
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\AnnualHealthCheck.pdf",
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\LeavePolicy.pdf",
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\NoticePeriod.pdf",
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\OfficeTime.pdf",
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\Separation.pdf",
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\Travel.pdf",
    r"F:\backup\SugumarStuffs\Gen AI\Sample Data Files\New folder\USA_Employee_Handbook-Freely_Available.pdf"
]

documents = []

for file in files:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    documents.append(text)


print("Documents Loaded:",len(documents))

query = input("Ask Question: ")

query_tokens = word_tokenize(query)

print("Query Tokens:", query_tokens)

for doc in documents:

    tokens = word_tokenize(doc)

    common = set(tokens).intersection(set(query_tokens))

    print("Common Tokens:", common)

    if len(common) > 0:
        print("\nRelevant Section:\n")
        print(doc[:500])
