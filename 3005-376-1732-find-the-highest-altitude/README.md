<h2> 3005 376
1732. Find the Highest Altitude</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">There is a biker going on a road trip. The road trip consists of <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">n + 1</code> points at different altitudes. The biker starts his trip on point <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0</code> with altitude equal <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given an integer array <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">gain</code> of length <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">n</code> where <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">gain[i]</code> is the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">net gain in altitude</strong> between points <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">i</code>​​​​​​ and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">i + 1</code> for all (<code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">0 &lt;= i &lt; n)</code>. Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">highest altitude</strong> of a point.</em></p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> gain = [-5,1,5,0,-7]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 1
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> gain = [-4,-3,-2,-1,4,3,2]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 0
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">n == gain.length</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= n &lt;= 100</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 154, 174) !important; border-color: rgb(171, 35, 69) !important;">-100 &lt;= gain[i] &lt;= 100</code></li>
</ul>
</div>