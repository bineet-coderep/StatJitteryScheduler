# RC Network

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
>> RC Network Report
>>	 Scheduling Policy:  HoldKill ;	 Misses:  3
		* Avg. Time Taken:  2.2995774650573733
		* Avg. Refinements Made:  0.04
		* Avg. Upper Bound d:  1.897666590828917
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroKill ;	 Misses:  3
		* Avg. Time Taken:  2.037513155937195
		* Avg. Refinements Made:  0
		* Avg. Upper Bound d:  1.897666590828917
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  2.9964530181884768
		* Avg. Refinements Made:  0.52
		* Avg. Upper Bound d:  1.8193169444756219
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  ZeroSkip-Next ;	 Misses:  3
		* Avg. Time Taken:  2.5378466129302977
		* Avg. Refinements Made:  0.3
		* Avg. Upper Bound d:  1.6219567001076776
		* SD. Upper Bound d:  0.0
```

 [rc_network_safety_envelope.pdf](/home/bineet.local/MyResearch/StatJitteryScheduler/StatJitteryScheduler/output/Draft/RC/rc_network_safety_envelope.pdf) 

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

 [rc_varyC.pdf](rc_varyC.pdf) 

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
>> RC Network Report
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  2
		* Avg. Time Taken:  2.4191008234024047
		* Avg. Refinements Made:  0.04
		* Avg. Upper Bound d:  1.7830593004562654
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  4
		* Avg. Time Taken:  2.9248682498931884
		* Avg. Refinements Made:  0.16
		* Avg. Upper Bound d:  1.8193169444756219
		* SD. Upper Bound d:  0.0
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  8
		* Avg. Time Taken:  4.344029116630554
		* Avg. Refinements Made:  1.02
		* Avg. Upper Bound d:  1.9787756535384244
		* SD. Upper Bound d:  0.07726447791102707
>>	 Scheduling Policy:  HoldSkip-Next ;	 Misses:  16
		* Avg. Time Taken:  5.251054663658142
		* Avg. Refinements Made:  1.44
		* Avg. Upper Bound d:  2.459378330279948
		* SD. Upper Bound d:  0.17991400819683015
```

