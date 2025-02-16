<h2> 653 1004
933. Number of Recent Calls</h2><hr><div style="border-color: rgba(140, 122, 115, 0.65) !important;"><p style="border-color: rgba(140, 122, 115, 0.65) !important;">You have a <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">RecentCounter</code> class which counts the number of recent requests within a certain time frame.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">Implement the <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">RecentCounter</code> class:</p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">RecentCounter()</code> Initializes the counter with zero recent requests.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">int ping(int t)</code> Adds a new request at time <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">t</code>, where <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">t</code> represents some time in milliseconds, and returns the number of requests that has happened in the past <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">3000</code> milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">[t - 3000, t]</code>.</li>
</ul>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">It is <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">guaranteed</strong> that every call to <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">ping</code> uses a strictly larger value of <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">t</code> than the previous call.</p>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong class="example" style="border-color: rgba(140, 122, 115, 0.65) !important;">Example 1:</strong></p>

<pre style="background-color: rgb(24, 26, 27) !important; color: rgb(200, 192, 188) !important; border-color: rgb(126, 109, 103) !important;"><strong style="border-color: rgb(112, 97, 92) !important;">Input</strong>
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
<strong style="border-color: rgb(112, 97, 92) !important;">Output</strong>
[null, 1, 2, 3, 3]

<strong style="border-color: rgb(112, 97, 92) !important;">Explanation</strong>
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [<u style="border-color: rgb(112, 97, 92) !important;">1</u>], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [<u style="border-color: rgb(112, 97, 92) !important;">1</u>, <u style="border-color: rgb(112, 97, 92) !important;">100</u>], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [<u style="border-color: rgb(112, 97, 92) !important;">1</u>, <u style="border-color: rgb(112, 97, 92) !important;">100</u>, <u style="border-color: rgb(112, 97, 92) !important;">3001</u>], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, <u style="border-color: rgb(112, 97, 92) !important;">100</u>, <u style="border-color: rgb(112, 97, 92) !important;">3001</u>, <u style="border-color: rgb(112, 97, 92) !important;">3002</u>], range is [2,3002], return 3
</pre>

<p style="border-color: rgba(140, 122, 115, 0.65) !important;">&nbsp;</p>
<p style="border-color: rgba(140, 122, 115, 0.65) !important;"><strong style="border-color: rgba(140, 122, 115, 0.65) !important;">Constraints:</strong></p>

<ul style="border-color: rgba(140, 122, 115, 0.65) !important;">
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;"><code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">1 &lt;= t &lt;= 10<sup style="border-color: rgb(175, 36, 71) !important;">9</sup></code></li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">Each test case will call <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">ping</code> with <strong style="border-color: rgba(140, 122, 115, 0.65) !important;">strictly increasing</strong> values of <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">t</code>.</li>
	<li style="border-color: rgba(140, 122, 115, 0.65) !important;">At most <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">10<sup style="border-color: rgb(175, 36, 71) !important;">4</sup></code> calls will be made to <code style="background-color: rgb(39, 18, 24) !important; color: rgb(237, 157, 177) !important; border-color: rgb(175, 36, 71) !important;">ping</code>.</li>
</ul>
</div>