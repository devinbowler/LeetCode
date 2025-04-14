<h2> 1760 3094
819. Most Common Word</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given a string <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">paragraph</code> and a string array of the banned words <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">banned</code>, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the most frequent word that is not banned</em>. It is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">guaranteed</strong> there is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">at least one word</strong> that is not banned, and that the answer is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">unique</strong>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The words in <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">paragraph</code> are <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">case-insensitive</strong> and the answer should be returned in <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">lowercase</strong>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "ball"
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> paragraph = "a.", banned = []
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "a"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= paragraph.length &lt;= 1000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">paragraph consists of English letters, space <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">' '</code>, or one of the symbols: <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">"!?',;."</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">0 &lt;= banned.length &lt;= 100</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">1 &lt;= banned[i].length &lt;= 10</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 35, 70) !important;">banned[i]</code> consists of only lowercase English letters.</li>
</ul>
</div>