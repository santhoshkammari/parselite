from src.parselite import FastParser
parser = FastParser(extract_pdf=False)
print(parser(["https://www.geeksforgeeks.org/multithreading-python-set-1/"]))
