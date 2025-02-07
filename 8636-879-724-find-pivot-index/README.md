<h2> 8636 879
724. Find Pivot Index</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an array of integers <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">nums</code>, calculate the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">pivot index</strong> of this array.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">pivot index</strong> is the index where the sum of all the numbers <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">strictly</strong> to the left of the index is equal to the sum of all the numbers <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">strictly</strong> to the index's right.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">If the index is on the left edge of the array, then the left sum is <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">0</code> because there are no elements to the left. This also applies to the right edge of the array.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">leftmost pivot index</strong></em>. If no such index exists, return <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">-1</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [1,7,3,6,5,6]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 3
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [1,2,3]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> -1
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
There is no index that satisfies the conditions in the problem statement.</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [2,1,-1]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 0
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= nums.length &lt;= 10<sup style="border-color: rgb(172, 35, 70) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Note:</strong> This question is the same as&nbsp;1991:&nbsp;<a href="https://leetcode.com/problems/find-the-middle-index-in-array/" target="_blank" style="transition-property: -color !important; --link-color: rgb(117, 182, 234) !important; --link-color-hover: rgb(144, 196, 238) !important; --link-color-active: rgb(113, 179, 234) !important; --visited-color: rgb(160, 117, 234) !important; --visited-color-hover: rgb(179, 144, 238) !important; --visited-color-active: rgb(157, 113, 234) !important; border-color: rgb(22, 115, 202) !important;">https://leetcode.com/problems/find-the-middle-index-in-array/</a></p>
</div>