<h2> 5252 145
1207. Unique Number of Occurrences</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an array of integers <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">arr</code>, return <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">true</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">if the number of occurrences of each value in the array is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">unique</strong> or </em><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">false</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> otherwise</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> arr = [1,2,2,1,1,3]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> true
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>&nbsp;The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> arr = [1,2]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> false
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> arr = [-3,0,1,-3,1,1,1,-3,10,0]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> true
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= arr.length &lt;= 1000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">-1000 &lt;= arr[i] &lt;= 1000</code></li>
</ul>
</div>