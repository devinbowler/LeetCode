<h2> 4437 90
2095. Delete the Middle Node of a Linked List</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given the <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">head</code> of a linked list. <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Delete</strong> the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">middle node</strong>, and return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the</em> <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">head</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">of the modified linked list</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">middle node</strong> of a linked list of size <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">n</code> is the <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">⌊n / 2⌋<sup style="border-color: rgb(172, 35, 70) !important;">th</sup></code> node from the <b style="border-color: rgba(140, 122, 115, 0.65) !important;">start</b> using <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">0-based indexing</strong>, where <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">⌊x⌋</code> denotes the largest integer less than or equal to <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">x</code>.</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">For <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">n</code> = <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1</code>, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">2</code>, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">3</code>, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">4</code>, and <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">5</code>, the middle nodes are <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">0</code>, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1</code>, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1</code>, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">2</code>, and <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">2</code>, respectively.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png" style="width: 500px; height: 77px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> head = [1,3,4,7,1,2,6]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [1,3,4,1,2,6]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png" style="width: 250px; height: 43px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> head = [1,2,3,4]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [1,2,4]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png" style="width: 150px; height: 58px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> head = [2,1]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [2]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The number of nodes in the list is in the range <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">[1, 10<sup style="border-color: rgb(172, 35, 70) !important;">5</sup>]</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= Node.val &lt;= 10<sup style="border-color: rgb(172, 35, 70) !important;">5</sup></code></li>
</ul>
</div>