# Steering

## Varying Scheduling Policy

### Parameters

```shell
initPoint=[10,10]
H=150
R=50
EPSILON=0.0001
EPOCH=50
```

### Results

```shell
>> Steering Network Report
>>	 Scheduling Policy:  HoldKill ;	 Misses:  3
		* Avg. Time Taken:  1.675321044921875
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  3.8093535275443546
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroKill ;	 Misses:  3
		* Avg. Time Taken:  5.288655776977539
		* Avg. Refinements Made:  1.56
		* Avg. Upper Bound d:  7.835086026316143
		* SD. Upper Bound d:  0.14953745434319754
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  3.2592306470870973
		* Avg. Refinements Made:  0.38
		* Avg. Upper Bound d:  4.650475979003898
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  7.032051749229431
		* Avg. Refinements Made:  1.46
		* Avg. Upper Bound d:  7.207225134030079
		* SD. Upper Bound d:  0.20324532413697333
```

 [steering_safety_envelope.pdf](steering_safety_envelope.pdf) 

## Varying $c$

### Parameters

```shell
initPoint=[10,10]
H=150
R=10
EPSILON=0.0001
EPOCH=50
STEP=20
c=0.51
```

### Results

 [steering_varyC.pdf](steering_varyC.pdf) 

## Varying No. Of Misses

### Parameters

```shell
initPoint=[10,10]
H=150
R=50
EPSILON=0.0001
EPOCH=50
K_miss_list=[2,4,8,16]
```

### Results

```shell
>> Steering Network Report
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  2
		* Avg. Time Taken:  2.6603681659698486
		* Avg. Refinements Made:  0.06
		* Avg. Upper Bound d:  3.6254914217562866
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  4
		* Avg. Time Taken:  3.9452413845062257
		* Avg. Refinements Made:  0.68
		* Avg. Upper Bound d:  5.645861879343299
		* SD. Upper Bound d:  0.13611940907774886
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  8
		* Avg. Time Taken:  7.185072922706604
		* Avg. Refinements Made:  1.5
		* Avg. Upper Bound d:  9.577500298104399
		* SD. Upper Bound d:  0.9676083296637149
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  16
		* Avg. Time Taken:  6.059765701293945
		* Avg. Refinements Made:  1.58
		* Avg. Upper Bound d:  12.906991697072526
		* SD. Upper Bound d:  2.429184920731469
```

