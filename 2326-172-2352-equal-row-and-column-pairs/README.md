<h2> 2326 172
2352. Equal Row and Column Pairs</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given a <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">0-indexed</strong> <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">n x n</code> integer matrix <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">grid</code>, <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">return the number of pairs </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">(r<sub style="border-color: rgb(171, 35, 69) !important;">i</sub>, c<sub style="border-color: rgb(171, 35, 69) !important;">j</sub>)</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> such that row </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">r<sub style="border-color: rgb(171, 35, 69) !important;">i</sub></code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> and column </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">c<sub style="border-color: rgb(171, 35, 69) !important;">j</sub></code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> are equal</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg" style="width: 150px; height: 153px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> grid = [[3,2,1],[1,7,6],[2,7,7]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 1
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg" style="width: 200px; height: 209px; filter: saturate(0.9) brightness(0.8);" before-style="2">
<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 3
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">n == grid.length == grid[i].length</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= n &lt;= 200</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= grid[i][j] &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">5</sup></code></li>
</ul>
</div>