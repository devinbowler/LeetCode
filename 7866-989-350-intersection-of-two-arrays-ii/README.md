<h2> 7866 989
350. Intersection of Two Arrays II</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given two integer arrays <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums1</code> and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums2</code>, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">an array of their intersection</em>. Each element in the result must appear as many times as it shows in both arrays and you may return the result in <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">any order</strong>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [2,2]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [4,9]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> [9,4] is also accepted.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Follow up:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">What if <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums1</code>'s size is small compared to <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums2</code>'s size? Which algorithm is better?</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">What if elements of <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">nums2</code> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>
</div>