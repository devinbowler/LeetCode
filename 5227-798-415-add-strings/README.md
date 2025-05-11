<h2> 5227 798
415. Add Strings</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given two non-negative integers, <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num1</code> and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num2</code> represented as string, return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">the sum of</em> <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num1</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">and</em> <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num2</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">as a string</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">You must solve the problem without using any built-in library for handling large integers (such as <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">BigInteger</code>). You must also not convert the inputs to integers directly.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> num1 = "11", num2 = "123"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "134"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> num1 = "456", num2 = "77"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "533"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> num1 = "0", num2 = "0"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "0"
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">1 &lt;= num1.length, num2.length &lt;= 10<sup style="border-color: rgb(170, 35, 69) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num1</code> and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num2</code> consist of only digits.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num1</code> and <code style="background-color: rgb(36, 17, 22) !important; color: rgb(236, 153, 174) !important; border-color: rgb(170, 35, 69) !important;">num2</code> don't have any leading zeros except for the zero itself.</li>
</ul>
</div>