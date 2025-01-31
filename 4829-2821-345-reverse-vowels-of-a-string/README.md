<h2> 4829 2821
345. Reverse Vowels of a String</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given a string <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">s</code>, reverse only all the vowels in the string and return it.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The vowels are <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">'a'</code>, <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">'e'</code>, <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">'i'</code>, <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">'o'</code>, and <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">'u'</code>, and they can appear in both lower and upper cases, more than once.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<div class="example-block" style="color: rgba(232, 229, 227, 0.55) !important; border-color: rgba(140, 122, 115, 0.08) !important;">
<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Input:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">s = "IceCreAm"</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Output:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">"AceCreIm"</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Explanation:</strong></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;">The vowels in <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">s</code> are <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">['I', 'e', 'e', 'A']</code>. On reversing the vowels, s becomes <code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">"AceCreIm"</code>.</p>
</div>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<div class="example-block" style="color: rgba(232, 229, 227, 0.55) !important; border-color: rgba(140, 122, 115, 0.08) !important;">
<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Input:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">s = "leetcode"</span></p>

<p style="border-color: rgba(140, 122, 115, 0.55) !important;"><strong style="border-color: rgba(140, 122, 115, 0.55) !important;">Output:</strong> <span class="example-io" style="border-color: rgba(140, 122, 115, 0.55) !important;">"leotcede"</span></p>
</div>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">1 &lt;= s.length &lt;= 3 * 10<sup style="border-color: rgb(170, 35, 69) !important;">5</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 16, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">s</code> consist of <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">printable ASCII</strong> characters.</li>
</ul>
</div>