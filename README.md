# roomba_search
Roomba path finding using a * and dijkstra


A* 

.  .  .  .  .  .  .  .  .  .  
.  v  v  v  .  .  .  .  .  .  
v  v  v  v  <  .  .  .  .  .  
v  v  v  <  <  .  .  .  .  .  
>  A  <  <  <  .  .  .  .  .  
>  ^  <  <  <  .  .  .  .  .  
>  ^  <  <  <  <  .  .  .  .  
^  #########^  .  v  .  .  .  
^  #########v  v  v  Z  .  .  
^  <  <  <  <  <  <  <  .  .  

.  .  .  .  .  .  .  .  .  .  
.  3  4  5  .  .  .  .  .  .  
3  2  3  4  9  .  .  .  .  .  
2  1  2  3  8  .  .  .  .  .  
1  A  1  6  11 .  .  .  .  .  
2  1  2  7  12 .  .  .  .  .  
3  2  3  4  9  14 .  .  .  .  
4  #########14 .  18 .  .  .  
5  #########15 16 13 Z  .  .  
6  7  8  9  10 11 12 13 .  .  

