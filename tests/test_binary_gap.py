import os
import sys

# ensure project root is importable when pytest runs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from binary_gap import solution


def test_gap_example_9():
	# 9 -> binary 1001 -> gap length 2
	assert solution(9) == 2


def test_gap_example_20():
	# 20 -> binary 10100 -> gap length 1
	assert solution(20) == 1
