<h2> 60269 2159
1. Two Sum</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an array of integers <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums</code>&nbsp;and an integer <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">target</code>, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">indices of the two numbers such that they add up to <code style="background-color: rgb(36, 17, 22) !important; color: rgb(247, 210, 219) !important; border-color: rgb(171, 35, 69) !important;">target</code></em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You may assume that each input would have <strong style="border-color: rgba(140, 122, 115, 0.65) !important;"><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">exactly</em> one solution</strong>, and you may not use the <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">same</em> element twice.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You can return the answer in any order.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [2,7,11,15], target = 9
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [0,1]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [3,2,4], target = 6
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [1,2]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums = [3,3], target = 6
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [0,1]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">2 &lt;= nums.length &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">-10<sup style="border-color: rgb(171, 35, 69) !important;">9</sup> &lt;= nums[i] &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">9</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">-10<sup style="border-color: rgb(171, 35, 69) !important;">9</sup> &lt;= target &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">9</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Only one valid answer exists.</strong></li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">O(n<sup style="border-color: rgb(171, 35, 69) !important;">2</sup>)</code><font face="monospace" style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</font>time complexity?</div>