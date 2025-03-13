<h2> 7688 257
452. Minimum Number of Arrows to Burst Balloons</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">points</code> where <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">points[i] = [x<sub style="border-color: rgb(172, 35, 69) !important;">start</sub>, x<sub style="border-color: rgb(172, 35, 69) !important;">end</sub>]</code> denotes a balloon whose <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">horizontal diameter</strong> stretches between <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">x<sub style="border-color: rgb(172, 35, 69) !important;">start</sub></code> and <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">x<sub style="border-color: rgb(172, 35, 69) !important;">end</sub></code>. You do not know the exact y-coordinates of the balloons.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Arrows can be shot up <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">directly vertically</strong> (in the positive y-direction) from different points along the x-axis. A balloon with <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">x<sub style="border-color: rgb(172, 35, 69) !important;">start</sub></code> and <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">x<sub style="border-color: rgb(172, 35, 69) !important;">end</sub></code> is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">burst</strong> by an arrow shot at <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">x</code> if <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">x<sub style="border-color: rgb(172, 35, 69) !important;">start</sub> &lt;= x &lt;= x<sub style="border-color: rgb(172, 35, 69) !important;">end</sub></code>. There is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">no limit</strong> to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given the array <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">points</code>, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">minimum</strong> number of arrows that must be shot to burst all balloons</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> points = [[10,16],[2,8],[1,6],[7,12]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 2
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> points = [[1,2],[3,4],[5,6],[7,8]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 4
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> One arrow needs to be shot for each balloon for a total of 4 arrows.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> points = [[1,2],[2,3],[3,4],[4,5]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> 2
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">1 &lt;= points.length &lt;= 10<sup style="border-color: rgb(172, 35, 69) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">points[i].length == 2</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">-2<sup style="border-color: rgb(172, 35, 69) !important;">31</sup> &lt;= x<sub style="border-color: rgb(172, 35, 69) !important;">start</sub> &lt; x<sub style="border-color: rgb(172, 35, 69) !important;">end</sub> &lt;= 2<sup style="border-color: rgb(172, 35, 69) !important;">31</sup> - 1</code></li>
</ul>
</div>