<h2> 4631 593
1431. Kids With the Greatest Number of Candies</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">There are <code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">n</code> kids with candies. You are given an integer array <code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">candies</code>, where each <code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">candies[i]</code> represents the number of candies the <code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">i<sup style="border-color: rgb(173, 36, 70) !important;">th</sup></code> kid has, and an integer <code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">extraCandies</code>, denoting the number of extra candies that you have.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Return <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">a boolean array </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">result</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> of length </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">n</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">, where </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">result[i]</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> is </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">true</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> if, after giving the </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">i<sup style="border-color: rgb(173, 36, 70) !important;">th</sup></code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> kid all the </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">extraCandies</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">, they will have the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">greatest</strong> number of candies among all the kids</em><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">, or </em><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">false</code><em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;"> otherwise</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Note that <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">multiple</strong> kids can have the <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">greatest</strong> number of candies.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> candies = [2,3,5,1,3], extraCandies = 3
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [true,true,true,false,true] 
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> candies = [4,2,1,1,2], extraCandies = 1
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [true,false,false,false,false] 
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 3:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> candies = [12,1,12], extraCandies = 10
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> [true,false,true]
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">n == candies.length</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">2 &lt;= n &lt;= 100</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">1 &lt;= candies[i] &lt;= 100</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(237, 156, 176) !important; border-color: rgb(173, 36, 70) !important;">1 &lt;= extraCandies &lt;= 50</code></li>
</ul>
</div>