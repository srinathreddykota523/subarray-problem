# Pricing Data Validation

## Problem Statement

A retail company stores price adjustment values recorded for products
during a pricing run.

A continuous range of products is considered valid when there are no
three distinct positions `i`, `j`, and `k` within that range such that:

    nums[i] + nums[j] = nums[k]

The three positions must be different, although the values at those
positions may be the same.

Given an integer array `nums`, return the maximum length of a valid
non-empty contiguous subarray.

### Example

Input:

[2, 3, 5, 3, 2, 1]

Output:

3

Explanation:

The range [2, 3, 5] is invalid because:

2 + 3 = 5

The maximum valid subarray length is 3.
