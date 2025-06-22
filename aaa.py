from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

# Start Spark
spark = SparkSession.builder.appName("SubstringMatchCount").getOrCreate()

# Step 1: Read the JSON array file
# The JSON file is a single array: ["ersd/avav", "ersd/avav", "dhshh/abab"]
df = spark.read.json("path/to/your/file.json", multiLine=True)

# Step 2: Explode the array into individual rows
df_strings = df.select(explode(col("value")).alias("text"))

# Step 3: Filter rows that contain the substring "avav"
df_matches = df_strings.filter(col("text").contains("avav"))

# Step 4: Count how many fields contain the substring
count = df_matches.count()

print(f"Number of fields containing 'avav': {count}")
