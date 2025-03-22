<h2> 8990 560
222. Count Complete Tree Nodes</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given the <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">root</code> of a <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">complete</strong> binary tree, return the number of the nodes in the tree.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">According to <strong style="border-color: rgba(140, 122, 115, 0.65) !important;"><a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank" style="transition-property: -color !important; --link-color: rgb(117, 182, 234) !important; --link-color-hover: rgb(144, 196, 238) !important; --link-color-active: rgb(113, 179, 234) !important; --visited-color: rgb(160, 117, 234) !important; --visited-color-hover: rgb(179, 144, 238) !important; --visited-color-active: rgb(157, 113, 234) !important; border-color: rgb(22, 115, 202) !important;">Wikipedia</a></strong>, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">1</code> and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">2<sup style="border-color: rgb(170, 35, 69) !important;">h</sup></code> nodes inclusive at the last level <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">h</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Design an algorithm that runs in less than&nbsp;<code data-stringify-type="code" style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">O(n)</code>&nbsp;time complexity.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = [1,2,3,4,5,6]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 6
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = []
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 0
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> root = [1]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 1
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The number of nodes in the tree is in the range <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">[0, 5 * 10<sup style="border-color: rgb(170, 35, 69) !important;">4</sup>]</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">0 &lt;= Node.val &lt;= 5 * 10<sup style="border-color: rgb(170, 35, 69) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The tree is guaranteed to be <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">complete</strong>.</li>
</ul>
</div>