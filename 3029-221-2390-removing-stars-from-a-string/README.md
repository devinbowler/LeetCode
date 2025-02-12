<h2> 3029 221
2390. Removing Stars From a String</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given a string <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">s</code>, which contains stars <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">*</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">In one operation, you can:</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Choose a star in <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">s</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Remove the closest <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">non-star</strong> character to its <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">left</strong>, as well as remove the star itself.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the string after <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">all</strong> stars have been removed</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Note:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The input will be generated such that the operation is always possible.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">It can be shown that the resulting string will always be unique.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "leet**cod*e"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "lecoe"
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> Performing the removals from left to right:
- The closest character to the 1<sup style="border-color: rgb(112, 97, 92) !important;">st</sup> star is 't' in "lee<strong style="border-color: rgb(112, 97, 92) !important;"><u style="border-color: rgb(112, 97, 92) !important;">t</u></strong>**cod*e". s becomes "lee*cod*e".
- The closest character to the 2<sup style="border-color: rgb(112, 97, 92) !important;">nd</sup> star is 'e' in "le<strong style="border-color: rgb(112, 97, 92) !important;"><u style="border-color: rgb(112, 97, 92) !important;">e</u></strong>*cod*e". s becomes "lecod*e".
- The closest character to the 3<sup style="border-color: rgb(112, 97, 92) !important;">rd</sup> star is 'd' in "leco<strong style="border-color: rgb(112, 97, 92) !important;"><u style="border-color: rgb(112, 97, 92) !important;">d</u></strong>*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "erase*****"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> ""
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The entire string is removed, so we return an empty string.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= s.length &lt;= 10<sup style="border-color: rgb(172, 35, 70) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">s</code> consists of lowercase English letters and stars <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">*</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">The operation above can be performed on <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">s</code>.</li>
</ul>
</div>