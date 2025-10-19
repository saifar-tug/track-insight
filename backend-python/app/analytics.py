def compute_metrics(df):
    avg_productivity = round(df['productivity_index_actual'].mean(), 2)
    avg_progress = round(df['progress_percent'].mean(), 2)
    avg_material_eff = round(df['material_efficiency'].mean(), 2)

    result = {
        "avg_productivity_index": avg_productivity,
        "avg_progress": avg_progress,
        "avg_material_efficiency": avg_material_eff
    }
    return result
