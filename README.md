# leetcode

    ```
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from imagededup.methods import PHash
import os

# Initialize Spark session
spark = SparkSession.builder.appName("ImageDeduplication").getOrCreate()

# Path to your image directory
image_dir = "/path/to/your/images"

# Read images as binary files
image_df = spark.read.format("binaryFile").load(image_dir)

# Initialize PHash object
phash = PHash()

# Define UDF to compute perceptual hash
def compute_phash(image_path):
    try:
        return phash.encode_image(image_path)
    except Exception as e:
        return None

# Register UDF with Spark
phash_udf = udf(compute_phash, StringType())

# Compute phash for each image
image_df = image_df.withColumn("phash", phash_udf(col("path")))

# Convert Spark DataFrame to Pandas to use imagededup for finding duplicates
image_pd_df = image_df.select("path", "phash").toPandas()

# Group by hash and find duplicates
duplicates = {}
for hash_value, group in image_pd_df.groupby("phash"):
    if len(group) > 1:
        duplicates[hash_value] = list(group["path"])

# Save duplicate results to a text file
output_file = "/path/to/output/duplicates.txt"
with open(output_file, "w") as f:
    for hash_value, paths in duplicates.items():
        f.write(f"Duplicate Group ({hash_value}):\n")
        f.write("\n".join(paths) + "\n\n")

print(f"Duplicate image list saved to: {output_file}")
    ```