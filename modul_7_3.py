class WordsFinder:
    file_names = []

    def __new__(cls, *args, **kwargs):
        WordsFinder.file_names.append(args)
        return super().__new__(cls)
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        a = ''
        b = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_name, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for word in line:
                    if word in b:
                        line = line.replace(word, '')
                a = a + line
            all_words.update({self.file_name: a.split()})
        return all_words






    def find(self, word):
        word_position = {}
        list = self.get_all_words()[self.file_name]
        for i in range(len(list)):
            if list[i] == word.lower():
                word_position.update({self.file_name: i+1})
                return word_position

    def count(self, word):
        word_number = {}
        list = self.get_all_words()[self.file_name]
        word_number.update({self.file_name: list.count(word.lower())})
        return word_number

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего






