<h2> 9084 5307
151. Reverse Words in a String</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an input string <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code>, reverse the order of the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">words</strong>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">A <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">word</strong> is defined as a sequence of non-space characters. The <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">words</strong> in <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> will be separated by at least one space.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">a string of the words in reverse order concatenated by a single space.</em></p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><b style="border-color: rgba(140, 122, 115, 0.65) !important;">Note</b> that <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "the sky is blue"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "blue is sky the"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "  hello world  "
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "world hello"
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> s = "a good   example"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "example good a"
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= s.length &lt;= 10<sup style="border-color: rgb(171, 35, 69) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> contains English letters (upper-case and lower-case), digits, and spaces <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">' '</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">There is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">at least one</strong> word in <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code>.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><b data-stringify-type="bold" style="border-color: rgba(140, 122, 115, 0.65) !important;">Follow-up:&nbsp;</b>If the string data type is mutable in your language, can&nbsp;you solve it&nbsp;<b data-stringify-type="bold" style="border-color: rgba(140, 122, 115, 0.65) !important;">in-place</b>&nbsp;with&nbsp;<code data-stringify-type="code" style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">O(1)</code>&nbsp;extra space?</p>
</div>