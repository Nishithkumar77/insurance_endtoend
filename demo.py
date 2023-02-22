## batch prediction
## training pipeline

from Insurance.pipeline.batch_prediction import start_batch_prediction

file_path = r"C:\Users\nsaha\Downloads\insurance_endtoend\insurance_endtoend\insurance.csv"

if __name__ == "__main__":
    try:
        output = start_batch_prediction(input_file_path=file_path)

    except Exception as e:
        print(e)