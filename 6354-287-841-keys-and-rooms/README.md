<h2> 6354 287
841. Keys and Rooms</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">There are <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">n</code> rooms labeled from <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">0</code> to <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">n - 1</code>&nbsp;and all the rooms are locked except for room <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">0</code>. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">When you visit a room, you may find a set of <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">distinct keys</strong> in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Given an array <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">rooms</code> where <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">rooms[i]</code> is the set of keys that you can obtain if you visited room <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">i</code>, return <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">true</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">if you can visit <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">all</strong> the rooms, or</em> <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">false</code> <em style="color: rgba(255, 255, 255, 0.65) !important; border-color: rgba(140, 122, 115, 0.65) !important;">otherwise</em>.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> rooms = [[1],[2],[3],[]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> true
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 2:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input:</strong> rooms = [[1,3],[3,0,1],[2],[0]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output:</strong> false
<strong style="border-color: rgb(112, 97, 92) !important;">Explanation:</strong> We can not enter room number 2 since the only key that unlocks it is in that room.
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">n == rooms.length</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">2 &lt;= n &lt;= 1000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">0 &lt;= rooms[i].length &lt;= 1000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">1 &lt;= sum(rooms[i].length) &lt;= 3000</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">0 &lt;= rooms[i][j] &lt; n</code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">All the values of <code style="background-color: rgb(38, 18, 23) !important; color: rgb(236, 155, 176) !important; border-color: rgb(173, 36, 70) !important;">rooms[i]</code> are <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">unique</strong>.</li>
</ul>
</div>