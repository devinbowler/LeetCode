<h2> 11419 601
108. Convert Sorted Array to Binary Search Tree</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an integer array <code style="background-color: rgb(38, 18, 24) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">nums</code> where the elements are sorted in <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">ascending order</strong>, convert <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">it to a </em><span data-keyword="height-balanced" style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;"><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">height-balanced</em></strong></span> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">binary search tree</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [-10,-3,0,5,9]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [0,-3,9,-10,null,5]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px; filter: saturate(0.9) brightness(0.8);" before-style="11">
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [1,3]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [3,1]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 24) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">1 &lt;= nums.length &lt;= 10<sup style="border-color: rgb(173, 36, 70) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 24) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">-10<sup style="border-color: rgb(173, 36, 70) !important;">4</sup> &lt;= nums[i] &lt;= 10<sup style="border-color: rgb(173, 36, 70) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 24) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">nums</code> is sorted in a <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">strictly increasing</strong> order.</li>
</ul>
</div>