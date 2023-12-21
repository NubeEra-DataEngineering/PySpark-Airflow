# spark-submit --master local[*] --name MySparkJob pyspark_example.py

from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("PySparkExample").getOrCreate()

    # Your PySpark code here
    data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    df = spark.createDataFrame(data, ["Name", "Value"])
    df.show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()
