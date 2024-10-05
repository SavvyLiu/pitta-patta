from pyspark.sql import SparkSession

from pyspark.sql.functions import lower


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext

file_path = "youtube_comments.csv"
df = spark.read.csv(file_path)


df_clean = df.withColumn('cleaned_comment', lower(df['_c0']))

from pyspark.sql.functions import regexp_replace

df_clean = df_clean.withColumn('cleaned_comment', regexp_replace('cleaned_comment', '[^a-zA-Z\s]', ''))


df_clean.show(5)

from pyspark.ml.feature import StopWordsRemover

# Initialize the StopWordsRemover without parameters
remover = StopWordsRemover() \
    .setInputCol("cleaned_comment") \
    .setOutputCol("filtered_comment")

print(df_clean.first().cleaned_comment)
# Transform the DataFrame
df_clean = remover.transform(df_clean)

df_clean.show(5)