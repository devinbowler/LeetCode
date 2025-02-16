<h2> 2550 1946
649. Dota2 Senate</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">In the world of Dota2, there are two parties: the Radiant and the Dire.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">one</strong> of the two rights:</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Ban one senator's right:</strong> A senator can make another senator lose all his rights in this and all the following rounds.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Announce the victory:</strong> If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given a string <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">senate</code> representing each senator's party belonging. The character <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">'R'</code> and <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">'D'</code> represent the Radiant party and the Dire party. Then if there are <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">n</code> senators, the size of the given string will be <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">n</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">"Radiant"</code> or <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">"Dire"</code>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> senate = "RD"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "Radiant"
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> senate = "RDD"
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> "Dire"
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">n == senate.length</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">1 &lt;= n &lt;= 10<sup style="border-color: rgb(172, 36, 70) !important;">4</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">senate[i]</code> is either <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">'R'</code> or <code style="background-color: rgb(38, 17, 23) !important; color: rgb(236, 155, 175) !important; border-color: rgb(172, 36, 70) !important;">'D'</code>.</li>
</ul>
</div>