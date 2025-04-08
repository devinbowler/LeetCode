<h2> 11016 1550
202. Happy Number</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Write an algorithm to determine if a number <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">n</code> is happy.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">A <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">happy number</strong> is a number defined by the following process:</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Repeat the process until the number equals 1 (where it will stay), or it <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">loops endlessly in a cycle</strong> which does not include 1.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Those numbers for which this process <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">ends in 1</strong> are happy.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">true</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">if</em> <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">n</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">is a happy number, and</em> <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">false</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">if not</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> n = 19
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> true
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong>
1<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> + 9<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> = 82
8<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> + 2<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> = 68
6<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> + 8<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> = 100
1<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> + 0<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> + 0<sup style="border-color: rgb(112, 97, 92) !important;">2</sup> = 1
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> n = 2
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> false
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">1 &lt;= n &lt;= 2<sup style="border-color: rgb(172, 35, 69) !important;">31</sup> - 1</code></li>
</ul>
</div>