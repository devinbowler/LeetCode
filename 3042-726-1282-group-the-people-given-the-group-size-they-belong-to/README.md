<h2> 3042 726
1282. Group the People Given the Group Size They Belong To</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">There are <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">n</code> people&nbsp;that are split into some unknown number of groups. Each person is labeled with a&nbsp;<strong style="border-color: rgba(140, 122, 115, 0.65) !important;">unique ID</strong>&nbsp;from&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">0</code>&nbsp;to&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">n - 1</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given an integer array&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">groupSizes</code>, where <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">groupSizes[i]</code>&nbsp;is the size of the group that person&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">i</code>&nbsp;is in. For example, if&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">groupSizes[1] = 3</code>, then&nbsp;person&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">1</code>&nbsp;must be in a&nbsp;group of size&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">3</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return&nbsp;<em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">a list of groups&nbsp;such that&nbsp;each person&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(247, 210, 219) !important; border-color: rgb(172, 35, 69) !important;">i</code>&nbsp;is in a group of size&nbsp;<code style="background-color: rgb(37, 17, 23) !important; color: rgb(247, 210, 219) !important; border-color: rgb(172, 35, 69) !important;">groupSizes[i]</code></em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Each person should&nbsp;appear in&nbsp;<strong style="border-color: rgba(140, 122, 115, 0.65) !important;">exactly one group</strong>,&nbsp;and every person must be in a group. If there are&nbsp;multiple answers, <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">return any of them</strong>. It is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">guaranteed</strong> that there will be <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">at least one</strong> valid solution for the given input.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> groupSizes = [3,3,3,3,3,1,3]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [[5],[0,1,2],[3,4,6]]
<b style="border-color: rgb(112, 97, 92) !important;">Explanation:</b> 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> groupSizes = [2,1,3,3,3,2]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [[1],[0,5],[2,3,4]]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">groupSizes.length == n</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">1 &lt;= n&nbsp;&lt;= 500</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">1 &lt;=&nbsp;groupSizes[i] &lt;= n</code></li>
</ul>
</div>