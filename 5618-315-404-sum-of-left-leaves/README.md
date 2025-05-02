<h2> 5618 315
404. Sum of Left Leaves</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given the <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">root</code> of a binary tree, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the sum of all left leaves.</em></p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">A <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">leaf</strong> is a node with no children. A <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">left leaf</strong> is a leaf that is the left child of another node.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" style="width: 277px; height: 302px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = [3,9,20,null,null,15,7]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 24
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> There are two left leaves in the binary tree, with values 9 and 15 respectively.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = [1]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 0
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The number of nodes in the tree is in the range <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">[1, 1000]</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>