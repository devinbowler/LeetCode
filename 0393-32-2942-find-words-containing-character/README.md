<h2> 393 32
2942. Find Words Containing Character</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You are given a <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">0-indexed</strong> array of strings <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">words</code> and a character <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">x</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">an <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">array of indices</strong> representing the words that contain the character </em><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">x</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Note</strong> that the returned array may be in <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">any</strong> order.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> words = ["leet","code"], x = "e"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [0,1]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> "e" occurs in both words: "l<strong style="border-color: rgb(112, 97, 92) !important;"><u style="border-color: rgb(112, 97, 92) !important;">ee</u></strong>t", and "cod<u style="border-color: rgb(112, 97, 92) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">e</strong></u>". Hence, we return indices 0 and 1.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> words = ["abc","bcd","aaaa","cbc"], x = "a"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [0,2]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> "a" occurs in "<strong style="border-color: rgb(112, 97, 92) !important;"><u style="border-color: rgb(112, 97, 92) !important;">a</u></strong>bc", and "<u style="border-color: rgb(112, 97, 92) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">aaaa</strong></u>". Hence, we return indices 0 and 2.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> words = ["abc","bcd","aaaa","cbc"], x = "z"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> []
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> "z" does not occur in any of the words. Hence, we return an empty array.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= words.length &lt;= 50</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= words[i].length &lt;= 50</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">x</code> is a lowercase English letter.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">words[i]</code> consists only of lowercase English letters.</li>
</ul>
</div>