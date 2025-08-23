## Gas Station Problem

Given a circular list of gas stations, where we can go from station ``i`` to the station ``i + 1``, and the last one
goes back to the first one, find the index of the station from where we start to be able to traverse all the stations
and go back to the initial one without running out of gas.

![](../static/gas-station-problem.png)

Some constraints of the problem are:

```
|gas| == |cost|
gas[i] >= 0
cost[i] >= 0
```

- Can only move forward
- The gas tank starts empty
- ``gas[i]`` represents the amount of gas at the station ``i``
- ``cost[i]`` represents the cost to go from the station ``i`` to the next one
- The answer is guaranteed to be unique
- If the station searching for doesn't exist, return -1

A brute force solution:

**For** each station ``i``:<br>
&nbsp;&nbsp;Start traversing from there<br>
&nbsp;&nbsp;**If** the car goes back to ``i``:<br>
&nbsp;&nbsp;&nbsp;&nbsp;``i`` is the right station, return it