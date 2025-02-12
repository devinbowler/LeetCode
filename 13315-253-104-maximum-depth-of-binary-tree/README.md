<h2> 13315 253
104. Maximum Depth of Binary Tree</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given the <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">root</code> of a binary tree, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">its maximum depth</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">A binary tree's <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">maximum depth</strong>&nbsp;is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = [3,9,20,null,null,15,7]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 3
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = [1,null,2]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 2
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The number of nodes in the tree is in the range <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">[0, 10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup>]</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">-100 &lt;= Node.val &lt;= 100</code></li>
</ul>
</div>