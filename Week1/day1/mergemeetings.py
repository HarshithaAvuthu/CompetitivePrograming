import unittest
from operator import itemgetter
import unittest


def merge_ranges(meetings):

    # Merge meeting ranges
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings,key=itemgetter(0))
    pdl = [meetings[0]]
    # print(pdl)
    meetings = meetings[1:]
    for (nstart, nend) in meetings:
        (start, end) = pdl[-1]
        
        if end>=nstart:
            if end<=nend:
                end = nend
            pdl[-1] = (start, end)
        else:
            pdl.append((nstart, nend))
        # print(pdl)
    return pdl







# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (11, 13),(2,5),(1,3)])
        expected = [(1, 8),(11,13)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)