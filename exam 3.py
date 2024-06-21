from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        print("Preparing the document for printing...")
        self.print()

class PDFDocument(Document):
    def print(self):
        print("Printing PDF document.")

class WordDocument(Document):
    def print(self):
        print("Printing Word document.")

class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document.")
from document import Document, PDFDocument, WordDocument, ExcelDocument

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == 'pdf':
            return PDFDocument()
        elif doc_type == 'word':
            return WordDocument()
        elif doc_type == 'excel':
            return ExcelDocument()
        else:
            raise ValueError("Unknown document type")
from document_factory import DocumentFactory

if __name__ == "__main__":
    doc_types = ['pdf', 'word', 'excel']

    for doc_type in doc_types:
        document = DocumentFactory.create_document(doc_type)
        document.prepare_for_printing()
        print()
