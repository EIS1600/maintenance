from pyarabic.number import extract_number_phrases


sample = """

قال أبو عبيد: توفي عدي سنة ست وستين.

وقال ابن سعد: توفي سنة ثمان وستين.

وقال هشام ابن الكلبي: توفي سنة سبع وستين، وله مائة وعشرون سنة

"""

print(extract_number_phrases(sample))