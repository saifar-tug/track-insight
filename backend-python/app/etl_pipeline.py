from .db_connect import fetch_table
import pandas as pd

def load_data():
    planning = fetch_table("day_tasks_planning")
    completed = fetch_table("day_tasks_completed")
    materials = fetch_table("materials_used")
    return planning, completed, materials

def prepare_data():
    planning, completed, materials = load_data()

    # planning and completed
    merged = planning.merge(
        completed,
        on='id',
        suffixes=('_plan', '_actual'),
        how='outer'
    )

    # materials
    merged = merged.merge(materials, on='id', how='left', suffixes=('', '_mat'))

    #columns
    merged['progress_percent'] = (merged['work_done'] / merged['planned_work_done']) * 100
    merged['material_efficiency'] = merged['quantity'] / merged['work_done']

    return merged
