<h2> 11831 1821
746. Min Cost Climbing Stairs</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given an integer array <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">cost</code> where <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">cost[i]</code> is the cost of <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">i<sup style="border-color: rgb(173, 36, 70) !important;">th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You can either start from the step with index <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">0</code>, or the step with index <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">1</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the minimum cost to reach the top of the floor</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> cost = [10,<u style="border-color: rgb(112, 97, 92) !important;">15</u>,20]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 15
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> cost = [<u style="border-color: rgb(112, 97, 92) !important;">1</u>,100,<u style="border-color: rgb(112, 97, 92) !important;">1</u>,1,<u style="border-color: rgb(112, 97, 92) !important;">1</u>,100,<u style="border-color: rgb(112, 97, 92) !important;">1</u>,<u style="border-color: rgb(112, 97, 92) !important;">1</u>,100,<u style="border-color: rgb(112, 97, 92) !important;">1</u>]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 6
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">2 &lt;= cost.length &lt;= 1000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">0 &lt;= cost[i] &lt;= 999</code></li>
</ul>
</div>