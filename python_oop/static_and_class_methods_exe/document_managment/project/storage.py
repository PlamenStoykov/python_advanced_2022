from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def get_category(self, category_id: int):
        for category in self.categories:
            if category.id == category_id:
                return category

    def get_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                return document

    def get_topic(self, topic_id: int):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        searched_category = self.get_category(category_id)
        searched_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        searched_topic = self.get_topic(topic_id)
        searched_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        searched_document = self.get_document(document_id)
        searched_document.edit(new_file_name)

    def delete_category(self, category_id):
        searched_category = self.get_category(category_id)
        self.categories.remove(searched_category)

    def delete_topic(self, topic_id):
        searched_topic = self.get_topic(topic_id)
        self.topics.remove(searched_topic)

    def delete_document(self, document_id):
        searched_document = self.get_document(document_id)
        self.documents.remove(searched_document)

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += repr(doc) + '\n'
        return result

