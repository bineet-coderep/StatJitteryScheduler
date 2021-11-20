# ECRTS21

NOTE: Default K_miss=1

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
>> ECRTS21 Network Report
>>	 Scheduling Policy:  HoldKill ;	 Misses:  1
		* Avg. Time Taken:  2.2804419088363646
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  3.552410946232964
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroKill ;	 Misses:  1
		* Avg. Time Taken:  5.5535932588577275
		* Avg. Refinements Made:  1.5
		* Avg. Upper Bound d:  11.124222236778344
		* SD. Upper Bound d:  0.7125944817984784
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  1
		* Avg. Time Taken:  2.1695320892333982
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  7.065491120420102
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroSkip-Next ;	 Misses:  1
		* Avg. Time Taken:  4.054093766212463
		* Avg. Refinements Made:  0.86
		* Avg. Upper Bound d:  9.783937700063724
		* SD. Upper Bound d:  0.4907314888439187
```

 [ECRTS21_safety_envelope.pdf](ECRTS21_safety_envelope.pdf) 

## Varying $c$

### Parameters

```shell
initPoint=[10,10]
H=100
R=10
EPSILON=0.0001
EPOCH=50
STEP=20
c=0.51
```

### Results

 [ECRTS21_varyC.pdf](ECRTS21_varyC.pdf) 

## Varying No. Of Misses

### Parameters

```shell
initPoint=[10,10]
H=150
R=50
EPSILON=0.0001
EPOCH=50
K_miss_list=[2,3]
```

### Results

```shell
>> ECRTS21 Network Report
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  2
		* Avg. Time Taken:  5.130885791778565
		* Avg. Refinements Made:  1.26
		* Avg. Upper Bound d:  11.807078464420075
		* SD. Upper Bound d:  0.7721191653406313
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  5.650118184089661
		* Avg. Refinements Made:  1.56
		* Avg. Upper Bound d:  19.7785692064253
		* SD. Upper Bound d:  1.8446932803844678
```

