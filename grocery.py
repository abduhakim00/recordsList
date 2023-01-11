class Grocery:
    filename = 'groceriesList.txt'

    def delete_record(self, record_name):
        pass

    def edit_record(self, record_name, new_record):
        pass

    def add_record(self, record):
        pass

    @classmethod
    def find_total(cls):
        pass

    @classmethod
    def set_filename(cls, text):
        cls.filename = text;
