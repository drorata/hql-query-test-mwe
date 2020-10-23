import pytest
import pandas as pd


@pytest.fixture
def sqlC():
    # For this to work I had to tweak:
    # $ export JAVA_HOME="$(/usr/libexec/java_home --version 1.8)"
    import findspark

    findspark.init()

    from pyspark.sql import SparkSession
    from pyspark.sql import SQLContext

    spark = SparkSession.builder.master("local[*]").getOrCreate()
    sc = spark.sparkContext
    return SQLContext(sc)


@pytest.mark.datafiles("data.csv")
def test_fast_forward(sqlC, datafiles):
    path = str(datafiles)  # Convert from py.path object to path (str)
    df = sqlC.read.option("header", True).csv(path)
    df.createOrReplaceTempView("data")
    pd_result = sqlC.sql("SELECT * FROM data where customerId=1").toPandas()

    expected_result = pd.DataFrame(
        {"customerId": ["1", "1", "1"], "value": ["10", "20", "30"]}
    )

    pd.testing.assert_frame_equal(expected_result, pd_result)
