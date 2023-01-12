import main


class Grocery:
    filename = main.FILENAME

    def delete_record(self, record_name):
        with open(self.filename, 'r') as f:
            data = f.readlines()
        data = filter(lambda x: x.split('-')[0] != record_name, data)
        with open(self.filename, 'w') as w:
            w.writelines(data)

    def edit_record(self, record_name, new_record):
        with open(self.filename, 'r') as f:
            data = f.readlines()
        for i in range(len(data)):
            if data[i].split('-')[0] == record_name:
                data[i] = new_record+'\n'
        with open(self.filename, 'w') as w:
            w.writelines(data)

    def add_record(self, record):
        with open(self.filename, 'a') as f:
            f.write(record+'\n')

    @classmethod
    def find_total(cls):
        with open(cls.filename, 'r') as f:
            data = map(lambda x: int(x.split('-')[-1].split('\\')[0]), f.readlines())
            print(sum(data))

    @classmethod
    def set_filename(cls, text):
        cls.filename = text

