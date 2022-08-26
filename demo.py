from housing.pipeline import pipeline


def main():
    pipeline=pipeline()
    pipeline.run_pipeline()

if __name__=="main":
    main()
    