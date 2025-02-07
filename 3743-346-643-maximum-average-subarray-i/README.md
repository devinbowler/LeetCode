<h2> 3743 346
643. Maximum Average Subarray I</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given an integer array <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">nums</code> consisting of <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">n</code> elements, and an integer <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Find a contiguous subarray whose <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">length is equal to</strong> <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code> that has the maximum average value and return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">this value</em>. Any answer with a calculation error less than <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">10<sup style="border-color: rgb(171, 35, 69) !important;">-5</sup></code> will be accepted.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [1,12,-5,-6,50,3], k = 4
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 12.75000
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [5], k = 1
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 5.00000
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">n == nums.length</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= k &lt;= n &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">-10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup> &lt;= nums[i] &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup></code></li>
</ul>
</div>