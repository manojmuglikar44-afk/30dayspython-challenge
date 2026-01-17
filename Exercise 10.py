for i in range(11):
    print(i)
---> 0
1
2
3
4
5
6
7
8
9
10

i=0
while i < 11:
    print(i)
    i=i+1
---> 0
1
2
3
4
5
6
7
8
9
10

for i in range(11):
    print(10 - i)
---> 10
9
8
7
6
5
4
3
2
1
0
  
i=10
while i<11 and i>=0:
    print(i)
    i=i-1
---> 10
9
8
7
6
5
4
3
2
1
0  
  
for i in range(0,11):
    print(i,'x',i,'=',i*i)
---> 0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)
---> Python
Numpy
Pandas
Django
Flask

for i in range(0,101,2):
    print(i)
---> 0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100

for i in range(100,-1,-2):
    print(i)
---> 100
98
96
94
92
90
88
86
84
82
80
78
76
74
72
70
68
66
64
62
60
58
56
54
52
50
48
46
44
42
40
38
36
34
32
30
28
26
24
22
20
18
16
14
12
10
8
6
4
2
0

# Exercises: Level 2

sum = 0
for i in range(0,101):
    sum+=i
print(sum)
---> 5050

sum_even= 0
sum_odd= 0
for i in range(0,101,2):
    sum_even+=i
print(f'Sum of all Even no. is {sum_even}')
for i in range(1,101,2):
    sum_odd+=i
print(f'Sum of all odd no. is {sum_odd}')
---> Sum of all Even no. is 2550
Sum of all odd no. is 2500
