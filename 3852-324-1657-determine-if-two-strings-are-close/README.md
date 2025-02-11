<h2> 3852 324
1657. Determine if Two Strings Are Close</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Two strings are considered <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">close</strong> if you can attain one from the other using the following operations:</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Operation 1: Swap any two <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">existing</strong> characters.

	<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
		<li style="border-color: rgba(140, 122, 115, 0.65) !important;">For example, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">a<u style="border-color: rgb(172, 35, 69) !important;">b</u>cd<u style="border-color: rgb(172, 35, 69) !important;">e</u> -&gt; a<u style="border-color: rgb(172, 35, 69) !important;">e</u>cd<u style="border-color: rgb(172, 35, 69) !important;">b</u></code></li>
	</ul>
	</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Operation 2: Transform <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">every</strong> occurrence of one <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">existing</strong> character into another <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">existing</strong> character, and do the same with the other character.
	<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
		<li style="border-color: rgba(140, 122, 115, 0.65) !important;">For example, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;"><u style="border-color: rgb(172, 35, 69) !important;">aa</u>c<u style="border-color: rgb(172, 35, 69) !important;">abb</u> -&gt; <u style="border-color: rgb(172, 35, 69) !important;">bb</u>c<u style="border-color: rgb(172, 35, 69) !important;">baa</u></code> (all <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">a</code>'s turn into <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">b</code>'s, and all <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">b</code>'s turn into <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">a</code>'s)</li>
	</ul>
	</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You can use the operations on either string as many times as necessary.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given two strings, <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">word1</code> and <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">word2</code>, return <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">true</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> if </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">word1</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> and </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">word2</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> are <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">close</strong>, and </em><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">false</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> otherwise.</em></p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> word1 = "abc", word2 = "bca"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> true
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> You can attain word2 from word1 in 2 operations.
Apply Operation 1: "a<u style="border-color: rgb(112, 97, 92) !important;">bc</u>" -&gt; "a<u style="border-color: rgb(112, 97, 92) !important;">cb</u>"
Apply Operation 1: "<u style="border-color: rgb(112, 97, 92) !important;">a</u>c<u style="border-color: rgb(112, 97, 92) !important;">b</u>" -&gt; "<u style="border-color: rgb(112, 97, 92) !important;">b</u>c<u style="border-color: rgb(112, 97, 92) !important;">a</u>"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> word1 = "a", word2 = "aa"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> false
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation: </strong>It is impossible to attain word2 from word1, or vice versa, in any number of operations.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> word1 = "cabbba", word2 = "abbccc"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> true
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> You can attain word2 from word1 in 3 operations.
Apply Operation 1: "ca<u style="border-color: rgb(112, 97, 92) !important;">b</u>bb<u style="border-color: rgb(112, 97, 92) !important;">a</u>" -&gt; "ca<u style="border-color: rgb(112, 97, 92) !important;">a</u>bb<u style="border-color: rgb(112, 97, 92) !important;">b</u>"
Apply Operation 2: "<u style="border-color: rgb(112, 97, 92) !important;">c</u>aa<u style="border-color: rgb(112, 97, 92) !important;">bbb</u>" -&gt; "<u style="border-color: rgb(112, 97, 92) !important;">b</u>aa<u style="border-color: rgb(112, 97, 92) !important;">ccc</u>"
Apply Operation 2: "<u style="border-color: rgb(112, 97, 92) !important;">baa</u>ccc" -&gt; "<u style="border-color: rgb(112, 97, 92) !important;">abb</u>ccc"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">1 &lt;= word1.length, word2.length &lt;= 10<sup style="border-color: rgb(172, 35, 69) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">word1</code> and <code style="background-color: rgb(37, 17, 23) !important; color: rgb(236, 154, 175) !important; border-color: rgb(172, 35, 69) !important;">word2</code> contain only lowercase English letters.</li>
</ul>
</div>