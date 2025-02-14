<h2> 9564 249
977. Squares of a Sorted Array</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an integer array <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(171, 35, 69) !important;">nums</code> sorted in <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">non-decreasing</strong> order, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">an array of <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [-4,-1,0,3,10]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [0,1,9,16,100]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [-7,-3,2,3,11]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [4,9,9,49,121]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(171, 35, 69) !important;"><span style="border-color: rgb(171, 35, 69) !important;">1 &lt;= nums.length &lt;= </span>10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(171, 35, 69) !important;">-10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup> &lt;= nums[i] &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(171, 35, 69) !important;">nums</code> is sorted in <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">non-decreasing</strong> order.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(171, 35, 69) !important;">O(n)</code> solution using a different approach?</div>