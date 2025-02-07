<h2> 9123 154
1004. Max Consecutive Ones III</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given a binary array <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums</code> and an integer <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code>, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the maximum number of consecutive </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">'s in the array if you can flip at most</em> <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code> <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0</code>'s.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 6
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> [1,1,1,0,0,<u style="border-color: rgb(112, 97, 92) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">1</strong>,1,1,1,1,<strong style="border-color: rgb(112, 97, 92) !important;">1</strong></u>]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 10
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> [0,0,<u style="border-color: rgb(112, 97, 92) !important;">1,1,<strong style="border-color: rgb(112, 97, 92) !important;">1</strong>,<strong style="border-color: rgb(112, 97, 92) !important;">1</strong>,1,1,1,<strong style="border-color: rgb(112, 97, 92) !important;">1</strong>,1,1</u>,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= nums.length &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums[i]</code> is either <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0</code> or <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0 &lt;= k &lt;= nums.length</code></li>
</ul>
</div>