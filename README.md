# TFM.log
Automatic ELO-MMR updater for Terraforming Mars Game play log

This repo is using ELO-MMR system suggested by
> Ebtekar, A., & Liu, P. (2021). An Elo-like System for Massive Multiplayer Competitions. arXiv preprint arXiv:2101.00400.


# Log format
* Split season by file
* Seperate each round by `\n\n` (double space)
* Record results of each player by 
`Name Corperation VP`
with `\n`

# Standings
``` csv
rank,display_rating,max_rating,cur_sigma,num_contests,last_contest_index,last_contest_time,last_perf,last_change,handle
1,1758,1758,113,3,4,4,1869,63,최희원
2,1626,1626,95,5,5,5,1722,35,황덕근
3,1388,1388,133,2,2,2,1465,57,이규호
4,1346,1346,174,1,5,5,1541,386,김현채
5,1280,1280,174,1,4,4,1462,320,강현모
6,1268,1268,95,5,5,5,1322,24,서보성
7,1256,1256,133,2,2,2,1290,20,강민혁
8,1212,1212,174,1,1,1,1381,252,김보경
9,1199,1199,174,1,3,3,1365,239,한유진
10,1021,1021,174,1,5,5,1150,61,염규진
11,971,971,174,1,2,2,1090,11,한민구
```
