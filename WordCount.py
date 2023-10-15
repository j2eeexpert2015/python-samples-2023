# WordCount.py

# Importing necessary libraries
from pyspark.sql import SparkSession
from pyspark import SparkContext
import os


def word_count(file_path):
    """
    Function to count the occurrence of each word in the given file.
    """
    # Create a SparkSession
    spark = SparkSession.builder \
        .appName("PySpark WordCount") \
        .master("local[*]") \
        .getOrCreate()

    # Get SparkContext from SparkSession
    sc = SparkContext.getOrCreate()

    # Read the text file
    rdd = sc.textFile(file_path)

    # Split the lines into words, map each word with a count of 1, and then reduce by key (word)
    counts = rdd.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)

    # Collect the results and print them
    for (word, count) in counts.collect():
        print("{}: {}".format(word, count))

    # Stop the SparkSession
    spark.stop()


if __name__ == "__main__":
    # Assume the textFile is inside the resources directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'data', 'sample.txt')

    word_count(file_path)
