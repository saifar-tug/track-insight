from fastapi import FastAPI
from fastapi.responses import FileResponse
from .etl_pipeline import prepare_data
from .analytics import compute_metrics
from .charts import generate_progress_chart, generate_materials_chart

app = FastAPI()

@app.get("/analytics")
def get_analytics():
    try:
        df = prepare_data()
        result = compute_metrics(df)
        return result
    except Exception as e:
        print("Error in /analytics:", e)
        return {"error": str(e)}


@app.get("/debug/data")
def get_sample_data():
    try:
        df = prepare_data()
        return df.head(5).to_dict(orient="records")
    except Exception as e:
        print("Error in /debug/data:", e)
        return {"error": str(e)}


@app.get("/charts/progress")
def get_progress_chart():
    try:
        df = prepare_data()
        chart_path = generate_progress_chart(df)
        return FileResponse(chart_path, media_type="image/png")
    except Exception as e:
        print("Error in /charts/progress:", e)
        return {"error": str(e)}


@app.get("/charts/materials")
def get_materials_chart():
    try:
        from .db_connect import fetch_table
        materials_df = fetch_table("materials_used")
        chart_path = generate_materials_chart(materials_df)
        return FileResponse(chart_path, media_type="image/png")
    except Exception as e:
        print("Error in /charts/materials:", e)
        return {"error": str(e)}
