<h2> 13158 644
394. Decode String</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an encoded string, return its decoded string.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The encoding rule is: <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">k[encoded_string]</code>, where the <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">encoded_string</code> inside the square brackets is being repeated exactly <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code> times. Note that <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code> is guaranteed to be a positive integer.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">k</code>. For example, there will not be input like <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">3a</code> or <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">2[4]</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The test cases are generated so that the length of the output will never exceed <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">10<sup style="border-color: rgb(171, 35, 69) !important;">5</sup></code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "3[a]2[bc]"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "aaabcbc"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "3[a2[c]]"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "accaccacc"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "2[abc]3[cd]ef"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "abcabccdcdcdef"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= s.length &lt;= 30</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> consists of lowercase English letters, digits, and square brackets <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">'[]'</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> is guaranteed to be <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">a valid</strong> input.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">All the integers in <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> are in the range <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">[1, 300]</code>.</li>
</ul>
</div>