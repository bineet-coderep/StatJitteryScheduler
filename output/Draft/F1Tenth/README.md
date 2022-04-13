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
>> F1Tenth Network Report
>>	 Scheduling Policy:  HoldKill ;	 Misses:  3
		* Avg. Time Taken:  2.0230342292785646
		* Avg. Refinements Made:  0.02
		* Avg. Upper Bound d:  8.76262855344387
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroKill ;	 Misses:  3
		* Avg. Time Taken:  4.997739143371582
		* Avg. Refinements Made:  1.26
		* Avg. Upper Bound d:  15.928067916119746
		* SD. Upper Bound d:  0.5480550831624622
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  7.185490546226501
		* Avg. Refinements Made:  1.66
		* Avg. Upper Bound d:  14.199623740694104
		* SD. Upper Bound d:  0.6545090602179757
>>	 Scheduling Policy:  ZeroSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  6.07640423297882
		* Avg. Refinements Made:  1.42
		* Avg. Upper Bound d:  14.016338953408209
		* SD. Upper Bound d:  0.5002452402857631
```

  [F1Tenth_Trajs_safety_envelope.pdf](F1Tenth_Trajs_safety_envelope.pdf) 

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

 [F1Tenth_varC_varyC.pdf](F1Tenth_varC_varyC.pdf)  

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
>> F1Tenth Network Report
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  2
		* Avg. Time Taken:  4.60040964603424
		* Avg. Refinements Made:  0.88
		* Avg. Upper Bound d:  8.6505698747975
		* SD. Upper Bound d:  0.47629142773955974
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  4
		* Avg. Time Taken:  6.519974722862243
		* Avg. Refinements Made:  1.66
		* Avg. Upper Bound d:  20.683949483591764
		* SD. Upper Bound d:  1.4999902298423684
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  8
		* Avg. Time Taken:  6.070730910301209
		* Avg. Refinements Made:  1.44
		* Avg. Upper Bound d:  48.91860533815795
		* SD. Upper Bound d:  10.75159364380664
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  16
		* Avg. Time Taken:  6.7833133840560915
		* Avg. Refinements Made:  1.68
		* Avg. Upper Bound d:  65.29403034211668
		* SD. Upper Bound d:  16.638298491402438
```

