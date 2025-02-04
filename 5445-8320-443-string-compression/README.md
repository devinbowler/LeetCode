<h2> 5445 8320
443. String Compression</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an array of characters <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">chars</code>, compress it using the following algorithm:</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Begin with an empty string <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code>. For each group of <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">consecutive repeating characters</strong> in <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">chars</code>:</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">If the group's length is <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1</code>, append the character to <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Otherwise, append the character followed by the group's length.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The compressed string <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">s</code> <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">should not be returned separately</strong>, but instead, be stored <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">in the input character array <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">chars</code></strong>. Note that group lengths that are <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">10</code> or longer will be split into multiple characters in <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">chars</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">After you are done <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">modifying the input array,</strong> return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the new length of the array</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You must write an algorithm that uses only constant extra space.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> chars = ["a","a","b","b","c","c","c"]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> chars = ["a"]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> Return 1, and the first character of the input array should be: ["a"]
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The only group is "a", which remains uncompressed since it's a single character.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">1 &lt;= chars.length &lt;= 2000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(171, 35, 69) !important;">chars[i]</code> is a lowercase English letter, uppercase English letter, digit, or symbol.</li>
</ul>
</div>