import unittest
import WordCounter as wc


class TestWordCounter(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(wc.GenerateCounterDict(""), {'count': [], 'word': []})

    def testOne(self):
        self.assertEqual(wc.GenerateCounterDict("One"), {'word': ['one'], 'count': [1]})
        self.assertEqual(wc.GenerateCounterDict("One, Two"), {'word': ['one', 'two'], 'count': [1, 1]})
        self.assertEqual(wc.GenerateCounterDict("One, Two. Three"), {'word': ['one', 'two', 'three'], 'count': [1, 1, 1]})
        self.assertEqual(wc.GenerateCounterDict("One,./,;:\' Two.@ Three\n End"), {'word': ['one', 'two', 'three', 'end'], 'count': [1, 1, 1, 1]})

    def testMany(self):
        self.assertEqual(wc.GenerateCounterDict("One one one"), {'word': ['one'], 'count': [3]})
        self.assertEqual(wc.GenerateCounterDict("One, one. two"), {'word': ['one', 'two'], 'count': [2, 1]})
        self.assertEqual(wc.GenerateCounterDict("One, One. Two, two"), {'word': ['one', 'two'], 'count': [2, 2]})
        self.assertEqual(wc.GenerateCounterDict("One,* Onee. \":;Onee\n one"), {'word': ['one', 'onee'], 'count': [2, 2]})

    def testSortEmpty(self):
        counter = wc.GenerateCounterDict('')
        answer, extraanswer = wc.SortedCounter(counter)
        self.assertEqual(answer, [])
        self.assertEqual(extraanswer, '')

    def testSortOne(self):
        counter = wc.GenerateCounterDict('One, Two. Three')
        answer, extraanswer = wc.SortedCounter(counter)
        self.assertEqual(answer, [])
        self.assertEqual(extraanswer, 'one, two, three')

    def testSortMany(self):
        counter = wc.GenerateCounterDict('One, One. Two, two. TWO')
        answer, extraanswer = wc.SortedCounter(counter)
        self.assertEqual(answer, ['two - 3', 'one - 2'])
        self.assertEqual(extraanswer, '')
        counter = wc.GenerateCounterDict('One one one')
        answer, extraanswer = wc.SortedCounter(counter)
        self.assertEqual(answer, ['one - 3'])
        self.assertEqual(extraanswer, '')

    def testSortAny(self):
        counter = wc.GenerateCounterDict('One, One. Two, two, TWO\n three three three three\n new NEW a, b: c!')
        answer, extraanswer = wc.SortedCounter(counter)
        self.assertEqual(answer, ['three - 4', 'two - 3', 'one - 2', 'new - 2'])
        self.assertEqual(extraanswer, 'a, b, c')


if __name__ == '__main__':
    unittest.main()
