from timeit import timeit

print timeit('"0|20\\n0|Kristi|SELL|3000\\n0|Will|BUY|5000\\n0|Tom|BUY|50000\\n0|Shilpa|BUY|1500\\n1|Tom|BUY|1500000\\n3|25\\n5|Shilpa|SELL|1500\\n8|Kristi|SELL|600000\\n9|Shilpa|BUY|500\\n10|15\\n11|5\\n14|Will|BUY|100000\\n15|Will|BUY|100000\\n16|Will|BUY|100000\\n17|25\\n".split("\\n")', number=1000000)

print timeit('"0|20\\n0|Kristi|SELL|3000\\n0|Will|BUY|5000\\n0|Tom|BUY|50000\\n0|Shilpa|BUY|1500\\n1|Tom|BUY|1500000\\n3|25\\n5|Shilpa|SELL|1500\\n8|Kristi|SELL|600000\\n9|Shilpa|BUY|500\\n10|15\\n11|5\\n14|Will|BUY|100000\\n15|Will|BUY|100000\\n16|Will|BUY|100000\\n17|25\\n".splitlines()', number=1000000)

