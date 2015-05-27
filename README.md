# map-reduce
Map Reduce Examples using Python and Java

hadoop jar /usr/hdp/2.2.4.2-2/hadoop-mapreduce/hadoop-streaming.jar -mapper ./Mapper.py -reducer ./Reducer.py -file ./Mapper.py -file ./Reducer.py -input <input directory> -output <output directory>
