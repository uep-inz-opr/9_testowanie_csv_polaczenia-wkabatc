import csv
import unittest

inputFile = str(input())

calls_sum_dict = dict()

with open(inputFile,'r') as fin: 
    reader = csv.DictReader(fin, delimiter = ",")
    headers = next(reader)
    for row in reader:
        from_subscr = int(row['From'])
        if from_subscr not in calls_sum_dict:
            calls_sum_dict[from_subscr] = 0
        value = int(row['Duration(seconds)'])
        calls_sum_dict[from_subscr] += value

#print(max(calls_sum_dict.items(), key = lambda x:x[1]))

class MenadzerPolaczen:
    def __init__(self, filename):
      self.filename = filename
      self.data_dict = self.read_data()

    def read_data(self):
        calls_dict_sum = dict()
        with open(self.filename, 'r') as fin:
          reader = csv.reader(fin, delimiter= ",")
          headers = next(reader)

          for row in reader:
            from_subsr = int(row[0])
            if from_subsr not in calls_dict_sum:
              calls_dict_sum[from_subsr] = 0
            calls_dict_sum[from_subsr] += 1
        return calls_dict_sum

    def pobierz_najczesciej_dzwoniacego(self):
      return max(self.data_dict.items(), key= lambda x: x[1])

class SprawdzDzwoniacegoTest(unittest.TestCase):
  def test_czy_abonent_najczesciej_dzwoniacy_rozpoznany_poprawnie(self):
    mp = MenadzerPolaczen(inputFile)
    wynik = mp.pobierz_najczesciej_dzwoniacego()
    self.assertEqual((226,5), wynik)

unittest.main(argv=[''], defaultTest='SprawdzDzwoniacegoTest', exit=False)

if __name__ == '__main__':
    print(MenadzerPolaczen(input()).pobierz_najczesciej_dzwoniacego())
    pass