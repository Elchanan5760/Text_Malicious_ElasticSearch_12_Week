import csv

class Load_CSV:
    @staticmethod
    def read_csv():
        data = []
        with open('../data/tweets_injected 3.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
            return data