\## Compute Log — PR 4



==================================================

SYSTEM INFORMATION

==================================================

OS:         Windows 11

Version:    10.0.26200

Machine:    AMD64

Processor:  Intel64 Family 6 Model 151 Stepping 2, GenuineIntel

Python:     3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) \[MSC v.1943 64 bit (AMD64)]



Benchmark 1 — sum(range(5,000,000))

&nbsp; Result:  12,499,997,500,000

&nbsp; Time:    0.0703 seconds



Benchmark 2 — list comprehension (n=1,000,000)

&nbsp; First 5: \[0, 1, 4, 9, 16]

&nbsp; Time:    0.0852 seconds



Benchmark 3 — string join (n=100,000)

&nbsp; Length:  588,889 characters

&nbsp; Time:    0.0105 seconds



==================================================

SUMMARY

==================================================

&nbsp; sum benchmark:    0.0703s

&nbsp; list benchmark:   0.0852s

&nbsp; string benchmark: 0.0105s



\## RAM



Total RAM: 16 GB

