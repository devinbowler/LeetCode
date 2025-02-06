<h2> 3306 101
1679. Max Number of K-Sum Pairs</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given an integer array <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">nums</code> and an integer <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">k</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">In one operation, you can pick two numbers from the array whose sum equals <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">k</code> and remove them from the array.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the maximum number of operations you can perform on the array</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [1,2,3,4], k = 5
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 2
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [3,1,3,4,3], k = 6
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 1
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= nums.length &lt;= 10<sup style="border-color: rgb(172, 35, 70) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= nums[i] &lt;= 10<sup style="border-color: rgb(172, 35, 70) !important;">9</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= k &lt;= 10<sup style="border-color: rgb(172, 35, 70) !important;">9</sup></code></li>
</ul>
</div>