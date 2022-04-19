# F1Tenth

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
>> AircraftPitch Network Report
>>	 Scheduling Policy:  HoldKill ;	 Misses:  1
		* Avg. Time Taken:  2.49275794506073
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  59.97728110875382
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroKill ;	 Misses:  1
		* Avg. Time Taken:  2.168485198020935
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  136.5108878007394
		* SD. Upper Bound d:  6.333528800068534
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  1
		* Avg. Time Taken:  2.1487897205352784
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  150.80337618857388
		* SD. Upper Bound d:  0.2752379627059522
>>	 Scheduling Policy:  ZeroSkip-Next ;	 Misses:  1
		* Avg. Time Taken:  2.157558979988098
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  169.22801475924723
		* SD. Upper Bound d:  2.8326971221086965
```

  [AircraftPitch_Trajs_safety_envelope.pdf](AircraftPitch_Trajs_safety_envelope.pdf) 

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

 [AircraftPitch_varC_varyC.pdf](AircraftPitch_varC_varyC.pdf) 

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
> AircraftPitch Network Report
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  2
		* Avg. Time Taken:  4.213998789787293
		* Avg. Refinements Made:  0.66
		* Avg. Upper Bound d:  263.378896089011
		* SD. Upper Bound d:  18.063558877930493
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  5.011608214378357
		* Avg. Refinements Made:  1.4
		* Avg. Upper Bound d:  550.5728613343381
		* SD. Upper Bound d:  86.08570364697106
```

