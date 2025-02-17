<h2> 10507 551
328. Odd Even Linked List</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given the <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">head</code> of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the reordered list</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">first</strong> node is considered <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">odd</strong>, and the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">second</strong> node is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">even</strong>, and so on.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Note that the relative order inside both the even and odd groups should remain as it was in the input.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You must solve the problem&nbsp;in <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">O(1)</code>&nbsp;extra space complexity and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">O(n)</code> time complexity.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg" style="width: 300px; height: 123px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> head = [1,2,3,4,5]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [1,3,5,2,4]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg" style="width: 500px; height: 142px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> head = [2,1,3,5,6,4,7]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [2,3,6,7,1,5,4]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The number of nodes in the linked list is in the range <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">[0, 10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup>]</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">-10<sup style="border-color: rgb(171, 35, 69) !important;">6</sup> &lt;= Node.val &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">6</sup></code></li>
</ul>
</div>