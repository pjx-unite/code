from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract_all, size

spark = SparkSession.builder.appName("CountSubstring").getOrCreate()

# Sample DataFrame (replace this with your exploded one)
data = [("bringing in",), ("going strong",), ("done",)]
df = spark.createDataFrame(data, ["text"])

# Use regexp_extract_all to get all occurrences of 'ing'
from pyspark.sql.functions import expr

# Add column with list of all matches of 'ing'
df_with_matches = df.withColumn("ing_matches", expr("regexp_extract_all(text, 'ing', 0)"))

# Count how many times 'ing' occurs in each row
df_with_count = df_with_matches.withColumn("ing_count", size(col("ing_matches")))

df_with_count.show()

# Sum total count
total = df_with_count.agg({"ing_count": "sum"}).collect()[0][0]
print(f"Total 'ing' occurrences: {total}")
