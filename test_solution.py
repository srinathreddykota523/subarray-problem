import pytest
from solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 5, 3, 2, 1], 3),
        ([3, 4, 5, 6], 4),
        ([27, 10, 2, 30, 14, 21, 20, 5, 20, 19], 7)
    ],
)
def test_max_subarray(nums, expected):
    assert Solution().maxSubarray(nums) == expected