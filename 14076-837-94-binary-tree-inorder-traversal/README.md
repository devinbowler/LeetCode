<h2> 14076 837
94. Binary Tree Inorder Traversal</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given the <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 173) !important; border-color: rgb(170, 35, 69) !important;">root</code> of a binary tree, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the inorder traversal of its nodes' values</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<div class="example-block" style="color: rgba(232, 229, 227, 0.55) !important; border-color: rgba(140, 122, 115, 0.08) !important;">
<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Input:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">root = [1,null,2,3]</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Output:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">[1,3,2]</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Explanation:</strong></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px; filter: saturate(0.9) brightness(0.8); color: rgba(232, 229, 227, 0.55) !important;" before-style="10"></p>
</div>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<div class="example-block" style="color: rgba(232, 229, 227, 0.55) !important; border-color: rgba(140, 122, 115, 0.08) !important;">
<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Input:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Output:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">[4,2,6,5,7,1,3,9,8]</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Explanation:</strong></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/tree_2.png" style="width: 350px; height: 286px; filter: saturate(0.9) brightness(0.8);" before-style="10"></p>
</div>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<div class="example-block" style="color: rgba(232, 229, 227, 0.55) !important; border-color: rgba(140, 122, 115, 0.08) !important;">
<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Input:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">root = []</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Output:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">[]</span></p>
</div>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 4:</strong></p>

<div class="example-block" style="color: rgba(232, 229, 227, 0.55) !important; border-color: rgba(140, 122, 115, 0.08) !important;">
<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Input:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">root = [1]</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Output:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">[1]</span></p>
</div>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The number of nodes in the tree is in the range <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 173) !important; border-color: rgb(170, 35, 69) !important;">[0, 100]</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 173) !important; border-color: rgb(170, 35, 69) !important;">-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</div>